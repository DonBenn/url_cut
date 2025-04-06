from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL

from .constants import (MAX_SHORT_URL_LENGTH, MIN_SHORT_URL_LENGTH,
                        MAX_ORIGINAL_LINK_LENGTH, MIN_ORIGINAL_LINK_LENGTH)


class ShortUrlForm(FlaskForm):
    original_link = URLField(
        'Добавьте ссылку',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(MIN_ORIGINAL_LINK_LENGTH, MAX_ORIGINAL_LINK_LENGTH), URL()]
    )
    custom_id = StringField('Введите короткую ссылку',
        validators = [Length(MIN_SHORT_URL_LENGTH, MAX_SHORT_URL_LENGTH), Optional()])
    submit = SubmitField('Добавить')