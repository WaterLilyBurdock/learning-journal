from pathlib import Path

BASE = Path(__file__).parent
INPUT = BASE / "report2.txt"
REPORT = BASE / "Analyze.txt"


def ensure_sample_file(path: Path) -> None:
    """Создать демо-файл, если его ещё нет."""
    if not path.exists():
        path.write_text(
            "Максим и Денис бежали по дорожке\n"
            "И упали\n"
            "Ха-Ха-Ха\n",
            encoding="utf-8",
        )


def analyze(path: Path) -> dict[str, int]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    words = text.split()
    return {
        "Строк": len(lines),
        "Слов": len(words),
        "Символов": len(text),
        "Символов без пробельных": len("".join(words)),
        "Пустых строк": sum(1 for line in lines if not line.strip()),
    }


def save_report(path: Path, stats: dict[str, int]) -> None:
    lines = [f"{k} : {v}" for k, v in stats.items()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    ensure_sample_file(INPUT)
    stats = analyze(INPUT)

    print(f"Файл: {INPUT.name}")
    for k, v in stats.items():
        print(f"{k} : {v}")

    save_report(REPORT, stats)