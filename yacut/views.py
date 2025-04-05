from random import randrange
from urllib.parse import urlparse, urljoin

from flask import abort, flash, redirect, render_template, url_for

# from . import app, db
from yacut import app, db
# from .forms import ShortUrlForm
from yacut.forms import ShortUrlForm
# from .models import URLMap
from yacut.models import URLMap
# from .utils import get_unique_short_id
from yacut.utils import get_unique_short_id

# @app.route('/')
# def index_view():
#     quantity = URLMap.query.count()
#     if not quantity:
#         return 'В базе данных нет ссылок.'
#     offset_value = randrange(quantity)
#     opinion = URLMap.query.offset(offset_value).first()
#     return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def get_short_url_view():
    form = ShortUrlForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if short_url is None:
            short_url = get_unique_short_id()
        if URLMap.query.filter_by(short=short_url).first():
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('short_url.html', form=form)
        opinion = URLMap(
            original=form.original_link.data,
            short=short_url
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect(url_for('redirect_view', short_id=short_url))
        # return redirect(url_for('get_short_url_view', short_url=short_url))
        # return 200
    # return render_template('index.html', form=form)
    # return render_template('base.html', form=form)
    return render_template('short_url.html', form=form)


# @app.route('/opinions/<str:short_id>')
def redirect_view(short_id):
    url = URLMap.query.get_or_404(short_id)
    original = url.original
    parsed_url = urlparse(original)

    # Формируем базовый URL
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}/"

    # Объединяем базовый URL с short_id
    final_url = urljoin(base_url, short_id)

    # print(final_url)
    return final_url
    # return render_template('opinion.html', opinion=opinion)