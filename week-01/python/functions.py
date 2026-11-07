"""Функции: аргументы по умолчанию, *args, аннотации типов."""

from collections import Counter


def count_words(text: str) -> dict[str, int]:
    """Частота слов в тексте. Регистр игнорируется, знаки препинания отбрасываются."""
    cleaned = (
        text.lower()
        .replace(".", " ").replace(",", " ").replace("!", " ")
        .replace("?", " ").replace(";", " ").replace(":", " ")
        .replace("\n", " ")
    )
    return dict(Counter(cleaned.split()))


def total(*args: float) -> float:
    """Сумматор произвольного числа позиционных аргументов."""
    return sum(args)


def describe(name: str, *traits: str, role: str = "user", **extra: object) -> str:
    """Демонстрация всех видов аргументов: обычный, *args, kw-only, **kwargs."""
    parts = [f"Имя: {name}", f"Роль: {role}"]
    if traits:
        parts.append("Черты: " + ", ".join(traits))
    if extra:
        parts.append("Прочее: " + ", ".join(f"{k}={v}" for k, v in extra.items()))
    return " | ".join(parts)


def safe_divide(a: float, b: float = 1.0) -> float | None:
    """Деление с защитой от нуля. Возвращает None вместо исключения."""
    if b == 0:
        return None
    return a / b


if __name__ == "__main__":
    print(count_words("Кот и пёс. Кот спит!"))        # {'кот': 2, 'и': 1, 'пёс': 1, 'спит': 1}
    print(total(1, 2, 3, 4.5))                        # 10.5
    print(describe("Аня", "добрая", "умная", role="admin", city="Москва"))
    print(safe_divide(10, 0))                         # None
    print(safe_divide(10, 4))                         # 2.5

    # Проверка аннотаций
    print(count_words.__annotations__)
    # {'text': <class 'str'>, 'return': dict[str, int]}