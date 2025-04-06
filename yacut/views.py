from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import ShortUrlForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def get_short_url_view():
    form = ShortUrlForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if not short_url:
            short_url = get_unique_short_id()
        if URLMap.query.filter_by(short=short_url).first():
            flash(
                'Предложенный вариант короткой ссылки уже существует.',
                'error')
            return render_template('short_url.html', form=form)
        link_exists = URLMap.query.filter_by(
            original=form.original_link.data).first()
        if link_exists:
            flash(url_for("redirect_view", short_id=link_exists.short),
                  'success')
        else:
            link = URLMap(
                original=form.original_link.data,
                short=short_url
            )
            db.session.add(link)
            db.session.commit()
            flash(short_url, 'success')
    return render_template('short_url.html', form=form)


@app.route('/<string:short_id>', methods=['GET'])
def redirect_view(short_id):
    url = URLMap.query.filter_by(short=short_id).first_or_404()
    return redirect(url.original)