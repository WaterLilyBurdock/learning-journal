"""Обработка исключений: ZeroDivisionError, ValueError, своё NegativeNumberError."""

import math


class NegativeNumberError(ValueError): #ValueError в скобках — это родительский класс (base class, superclass). NegativeNumberError — дочерний (subclass, derived).
    """Своё исключение: аргумент не может быть отрицательным."""

    def __init__(self, value: float) -> None:
        self.value = value
        super().__init__(f"Отрицательное значение недопустимо: {value}")


def safe_div(a: str | float, b: str | float) -> float: # | - значение(или) - анотация типов
    """Делит a на b, приводит строки к float и обрабатывает ошибки явно."""
    try:
        x = float(a)
        y = float(b)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Не удалось преобразовать к числу: a={a!r}, b={b!r}") from e

    if y == 0:
        raise ZeroDivisionError(f"Деление на ноль: {x} / {y}")

    return x / y


def sqrt_safe(x: float) -> float:
    """Корень, но отрицательные — через своё исключение."""
    if x < 0:
        raise NegativeNumberError(x)
    return math.sqrt(x) #Квадратный корень x


def demo() -> None:
    cases = [
        ("10", "2"),     # ok
        ("10", "0"),     # ZeroDivisionError
        ("abc", "2"),    # ValueError
    ]
    for a, b in cases:
        try:
            print(f"{a} / {b} = {safe_div(a, b)}")
        except ZeroDivisionError as e:
            print(f"[ZeroDivision] {e}")
        except ValueError as e:
            print(f"[Value] {e}")

    for value in (16, -4):
        try:
            print(f"sqrt({value}) = {sqrt_safe(value)}")
        except NegativeNumberError as e:
            print(f"[Negative] {e} (value={e.value})")


if __name__ == "__main__":
    demo()