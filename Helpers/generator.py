"""Этот файл помогает сгенерировать тестовые вводные данные."""
from random import randint
from typing import Tuple


class Generator:
    """Класс для генерации данных."""

    @staticmethod
    def generate_info() -> Tuple[str]:
        """
        Генерирует код из 10 цифр, по коду генерируется имя.
        """
        post_code = ''
        for _ in range(0, 10):
            post_code += str(randint(0, 9))

        first_name = ''
        for i in range(0, 10, 2):
            first_name += chr(97 + int(post_code[i:i+2]) % 26)
        # В задании не сказано про фамилию, указываю свою
        return (first_name, "Irbahtin", post_code)
