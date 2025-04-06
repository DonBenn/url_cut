import string

from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id
from .constants import MAX_SHORT_ID_LENGTH


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    link = URLMap.query.filter_by(short=short_id).first()
    if link is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': link.to_dict()['original']}), 200


@app.route('/api/id/', methods=['POST'])
def get_short_link():
    data = request.get_json(silent=True)

    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    if 'custom_id' not in data or not data['custom_id']:
        data['custom_id'] = get_unique_short_id()

    if len(data['custom_id']) > MAX_SHORT_ID_LENGTH:
        raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки')

    if URLMap.query.filter_by(original=data['url']).first() is not None:
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.'
        )

    if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
        raise InvalidAPIUsage(
            'Эта ссылка уже есть в базе данных'
        )

    for element in data['custom_id']:
        if element not in string.digits + string.ascii_letters:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки')

    link = URLMap()
    link.from_dict(data)
    db.session.add(link)
    db.session.commit()
    result = link.to_dict()
    return jsonify(
        {'url': result['original'], 'short_link': url_for(
            "redirect_view", short_id=result['short'], _external=True)}), 201