import unittest
from unittest.mock import MagicMock
from clocks.analog_clock import AnalogClock
from clocks.analog_to_digital_adapter import AnalogToDigitalAdapter
from consts.date_consts import DayNightDivision


class TestClockAdapter(unittest.TestCase):
    """Класс для проверки адаптера"""

    def setUp(self):
        """Настройка"""
        self.analog_clock_mock = MagicMock(spec=AnalogClock)
        self.analog_to_digital_adapter = AnalogToDigitalAdapter(self.analog_clock_mock)
