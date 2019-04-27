"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
import sys
from pympler.asizeof import asizeof

class Connection:
    """
    Класс Соединение. Эмулирет работу socket-соединений методом классов
    """
    def __init__(self, pid: int, socket: int, ip: str, priority: int):
        self.pid = pid
        self.socket = socket
        self.ip = ip
        self.priority = priority

    def check_state(self):
        """Проверка состояния соединения"""
        return "OK"

    def change_priority(self, priority):
        """Сменить приоритет"""
        self.priority = priority


class ConnectionS:
    """
    Класс Соединение. Эмулирет работу socket-соединений методом классов.
    Класс реализован с помощью слотов
    """

    __slots__ = ["pid", "socket", "ip", "priority"]

    def __init__(self, pid: int, socket: int, ip: str, priority: int):
        self.pid = pid
        self.socket = socket
        self.ip = ip
        self.priority = priority

    def check_state(self):
        """Проверка состояния соединения"""
        return "OK"

    def change_priority(self, priority):
        """Сменить приоритет"""
        self.priority = priority


if __name__ == '__main__':

    print(f"Класс через __dict__: {sys.getsizeof(Connection)}")  # 1056
    print(f"Класс через __slots__: {sys.getsizeof(ConnectionS)}")  # 888

    init_params = (4358, 5535, "10.0.43.54", 3)
    con = Connection(*init_params)
    con_s = ConnectionS(*init_params)
    print(f"Размер объекта через класс со словарем: {asizeof(con)}")
    print(f"Размер объекта через класс со слотами: {asizeof(con_s)}")

    """
    Класс через __dict__: 1056
    Класс через __slots__: 888
    Размер объекта через класс со словарем: 560
    Размер объекта через класс со слотами: 232
    """
    # В данном случае, экономия памяти при использования слотов почти двухкратная

    # Отображение словаря и атрибутов для объекта обычного класса
    for key, val in con.__dict__.items():
        print(f"{key}: {val}")
    """
    pid: 4358
    socket: 5535
    ip: 10.0.43.54
    priority: 3
    """

    # Отображение списка атрибутов для объекта класса через слоты
    print(con_s.__slots__)
    """
    ['pid', 'socket', 'ip', 'priority']
    """

