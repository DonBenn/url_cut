import random
import string

from short_url.models import ShortLink
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
        if not ShortLink.objects.filter(short_url=short_url).exists():
            return short_url