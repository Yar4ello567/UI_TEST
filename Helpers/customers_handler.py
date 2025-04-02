"""Этот файл отвечает за логику выбора клиента для удаления."""
from typing import List


class CustomerHandler:
    """Класс для методов логики выбора."""

    @staticmethod
    def get_avg_len(names: List[str]) -> float:
        """
        Метод нахождения среднего арифметического длин имен.
        """
        name_lengths = [len(name) for name in names]
        avg = sum(name_lengths) / len(name_lengths)
        return avg

    @staticmethod
    def get_closest_avg(names: List[str], avg: float) -> str:
        """
        Метод нахождения имени близкого по длине к среднему арифметическому.
        """
        closest_avg = min(names, key=lambda name: abs(len(name) - avg))
        return closest_avg

    @staticmethod
    def get_name_to_delete(names: List[str]) -> str:
        """
        Получает имя для удаления на основе бизнес-логики.
        """
        avg = CustomerHandler.get_avg_len(names)
        return CustomerHandler.get_closest_avg(names, avg)
