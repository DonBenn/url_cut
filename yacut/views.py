from random import randrange

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import ShortUrlForm
from .models import URLMap


@app.route('/')
def index_view():
    quantity = URLMap.query.count()
    if not quantity:
        return 'В базе данных нет ссылок.'
    offset_value = randrange(quantity)
    opinion = URLMap.query.offset(offset_value).first()
    return render_template('index.html')