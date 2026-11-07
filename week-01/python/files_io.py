"""Чтение файла, подсчёт строк/слов, запись отчёта."""

from pathlib import Path

BASE = Path(__file__).parent
INPUT = BASE / "sample.txt"
REPORT = BASE / "report.txt"


def ensure_sample(path: Path) -> None:
    """Создать демо-файл, если его нет."""
    if not path.exists():
        path.write_text(
            "Python — это просто.\n"
            "Python читают и пишут.\n"
            "Файлы, строки, слова!\n",
            encoding="utf-8",
        )


def analyze(path: Path) -> dict[str, int]:
    """Вернуть статистику по текстовому файлу."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    words = text.split()
    return {
        "lines": len(lines),
        "words": len(words),
        "chars": len(text),
        "chars_no_spaces": len("".join(words)),
        "empty_lines": sum(1 for line in lines if not line.strip()),
    }


def write_report(path: Path, stats: dict[str, int]) -> None:
    """Записать отчёт в файл."""
    lines = [f"{k}: {v}" for k, v in stats.items()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    ensure_sample(INPUT)
    stats = analyze(INPUT)

    print(f"Файл: {INPUT.name}")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    write_report(REPORT, stats)
    print(f"Отчёт записан в {REPORT.name}")