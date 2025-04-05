from random import randrange
from urllib.parse import urlparse, urljoin

from flask import abort, flash, redirect, render_template, url_for

from yacut import app, db
from yacut.forms import ShortUrlForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def get_short_url_view():
    form = ShortUrlForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if not short_url:
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
        # flash({url_for("redirect_view", short_id=short_url, _external=True)})
        flash(short_url)
    return render_template('short_url.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def redirect_view(short_id):
    url = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url.original)