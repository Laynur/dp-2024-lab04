# Лабораторная работа №4. Реализация шаблона Adapter.
# Цели и задачи
    - Практическое закрепление знаний полученных при изучении шаблона Adapter;
    - Закрепление навыков по написанию unit-тестов, настройке Continious Integration (CI);
# Задание и порядок выполнения
- Освежить в памяти шаблон Adapter:
        - проблема, которую решает шаблон;
        - UML-диаграмма паттерна;
        - преимущества и недостатки.
- В качестве примера реализации шаблона предлагается реализовать Адаптер, который бы позволял адаптировать интерфейс "Аналоговые часы" под клиентский код, который работает со стандартным типом DateTime.
- Дан интерфейс BaseAnalogClock по работе с аналоговыми часами (в git-репозитарии проекта), и его реализация в виде класса AnalogClock. Интерфейс "Аналоговые часы":
```class BaseAnalogClock(ABC):
    @abstractmethod
    def set_date_time(self, year: int, month: int, day: int, hour_angle: float, minute_angle: float,
                      second_angle: float, day_night_division: DayNightDivision):
        """
        Устанавливает текущую дату

        :param year: год
        :param month: месяц
        :param day: день
        :param hour_angle: угол стрелки часов
        :param minute_angle: угол минутной стрелки
        :param second_angle: угол секундной стрелки
        :param day_night_division: текущее время суток (день / ночь)
        """
        raise NotImplementedError()

    @abstractmethod
    def get_hour_angle(self) -> float:
        """
        Возвращает текущий угол стрелки часов
        """
        raise NotImplementedError()

    @abstractmethod
    def get_minute_angle(self) -> float:
        """
        Возвращает текущий угол минутной стрелки
        """
        raise NotImplementedError()

    @abstractmethod
    def get_second_angle(self) -> float:
        """
        Возвращает текущий угол секундной стрелки
        """
        raise NotImplementedError()

    @abstractmethod
    def get_year(self) -> int:
        """
        Возвращает текущий год (от установленного пользователем)
        """
        raise NotImplementedError()

    @abstractmethod
    def get_month(self) -> int:
        """
        Возвращает текущий месяц (от установленного пользователем)
        """
        raise NotImplementedError()

    @abstractmethod
    def get_day(self) -> int:
        """
        Возвращает текущий день (от установленного пользователем)
        """
        raise NotImplementedError()
```
- Необходимо разработать приложение, кототорое бы работало с интерфейсом, который схож с обычными цифровыми часами:
```class BaseDigitalClock(ABC):
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
```
но для хранения использовался бы класс AnalogClock через его интерфейс BaseAnalogClock. Для преобразования интерфейса BaseAnalogClock в BaseDigitalClock, следует воспользоваться шаблоном Адаптер.

- Порядок выполнения работы:
    - Создайте новый проект;
    - разработайте клиентский код, который демонстрирует работу с интерфейсом BaseDigitalClock (например принимает от пользователя время, выводит его в консоль);
    - организуйте реальное хранение времени в классе AnalogClock (к примеру того, времени которое ввёл пользователь). Для того чтобы работать с AnalogClock через интерфейс BaseDigitalClock, используйте шаблон Адаптер;    
    - создайте новый проект под unit-тесты;
    - напишите несколько unit-тестов, которые бы позволили вам убедиться, что разработанный вами Адаптер работает корректно;
    - изучите понятие Continious Integration (CI) (1, 2, 3), и реализуйте автоматический запуск ваших тестов на GitHub (docs). В качестве примера, посмотрите как это сделано в ЛР №2, ЛР №3
