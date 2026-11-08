def div(a, b):
    try:
        x = float(a)
        y = float(b)
    except (TypeError, ValueError) as e:
        raise ValueError(f"не число: a={a!r}, b={b!r}") from e
    if y == 0:
        raise ZeroDivisionError(f"деление на ноль: {x} / {y}")
    return x / y


if __name__ == "__main__":
    cases = [("10", "2"), ("abc", "2"), ("10", "0")]
    for a, b in cases:
        try:
            print(f"{a} / {b} = {div(a, b)}")
        except ZeroDivisionError as e:
            print(f"[Zero] {e}")
        except ValueError as e:
            print(f"[Value] {e}")