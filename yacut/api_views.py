from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap


@app.route('/api/<int:id>/<string:short_id>/', methods=['GET'])
def get_opinions(short_id):
    opinions = URLMap.query.get(short_id)
    if opinions is None:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    format = opinions.to_dict()
    return jsonify({'url': format.original}), 200


@app.route('/api/<int:id>/', methods=['POST'])
def add_opinion(id):
    data = request.get_json()
    if 'url' not in data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if URLMap.query.filter_by(original=data['url']).first() is not None:
        raise InvalidAPIUsage('Такое мнение уже есть в базе данных')
    opinion = URLMap()
    opinion.from_dict(data)
    db.session.add(opinion)
    db.session.commit()
    result = opinion.to_dict()
    return jsonify({'url': result.original, 'short_link': result.short}), 201

@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    return jsonify(error.to_dict()), error.status_code