from abc import abstractmethod, ABC
from datetime import datetime


class BaseDigitalClock(ABC):
    """Абстрактный класс для цифровых часов"""
    @abstractmethod
    def set_date_time(self, date: datetime) -> None:
        """
        Задает текущую дату

        :param date: дата в формате datetime
        """
        raise NotImplementedError()

    @abstractmethod
    def get_date_time(self) -> datetime:
        """
        Возвращает текущую дату в формате datetime
        """
        raise NotImplementedError()