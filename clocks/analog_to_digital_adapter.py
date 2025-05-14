from datetime import datetime

from interfaces.base_digital_clock import BaseDigitalClock

from clocks.analog_clock import AnalogClock
from clocks.time_coverter import TimeConverter
from consts.time_consts import TimeConsts
from consts.date_consts import DayNightDivision


class AnalogToDigitalAdapter(BaseDigitalClock):
    """Адапатер для перевода аналоговых часов в цифровые"""

    def __init__(self, analog_clock: AnalogClock):
        """Инициализация"""
        self._analog_clock = analog_clock

    def set_date_time(self, date: datetime) -> None:
        """
        Задает текущую дату
        :param date:
        :return:
        """
        year = date.year
        month = date.month
        day = date.day
        hour_angle = TimeConverter.hour_to_angle(date.hour, date.minute)
        minute_angle = TimeConverter.minute_to_angle(date.minute, date.second)
        second_angle = date.second * TimeConsts.DEG_FOR_SEC
        if TimeConsts.MIDNIGHT <= date.hour < TimeConsts.MIDDAY:
            day_night_division = DayNightDivision.AM
        else:
            day_night_division = DayNightDivision.PM
        self._analog_clock.set_date_time(year, month, day, hour_angle, minute_angle, second_angle, day_night_division)

    def get_date_time(self) -> datetime:
        """Возвращает текущую дату в формате datetime"""

        year = self._analog_clock.get_year()
        month = self._analog_clock.get_month()
        day = self._analog_clock.get_day()
        day_night_division = self._analog_clock.get_day_night_division()
        hour = TimeConverter.angle_to_hour(self._analog_clock.get_hour_angle(), day_night_division)
        minute = TimeConverter.angle_to_minute(self._analog_clock.get_minute_angle())
        second = int(self._analog_clock.get_second_angle() / TimeConsts.DEG_FOR_SEC)
        return datetime(year,month,day,hour,minute,second)
