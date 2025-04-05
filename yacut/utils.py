import random
import string

from .models import URLMap
from .constants import MAX_SHORT_URL_LENGTH


def get_unique_short_id():
    """Функция генерации короткой ссылки рецепта."""
    letters_digits = string.digits + string.ascii_letters
    while True:
        short_url = ''.join(
            random.choice(letters_digits) for element in range(
                MAX_SHORT_URL_LENGTH
            )
        )
        if not URLMap.query.filter_by(short=short_url).exists():
            return short_url