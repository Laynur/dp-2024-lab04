import datetime
from clocks.analog_clock import AnalogClock
from clocks.analog_to_digital_adapter import AnalogToDigitalAdapter


clock_adapter = AnalogToDigitalAdapter(AnalogClock())
print(clock_adapter.get_date_time())

clock_adapter.set_date_time(datetime.datetime.now())
print(clock_adapter.get_date_time())