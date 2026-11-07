"""Чтение файла, подсчёт строк/слов, запись отчёта."""

from pathlib import Path

BASE = Path(__file__).parent #Base - это папка текущего файла
INPUT = BASE / "sample.txt" # Переменная с выводомм текстового файла
REPORT = BASE / "report.txt"  #Переменная файла с информацией


def sample(path: Path) -> None:
    #Создаём файл если его нет
    if not path.exists():
        path.write_text(
            "Владик бежал по дорожке,\n"
            "В друг у него запутались ножки, \n"
            "ХА-ХА-ХА-ХА",
            encoding="utf-8",
        )

def analyze(path: Path) -> dict[str,int]:
    text = path.read_text(encoding="utf-8") #Читает текст
    lines = text.splitlines() #Разбивает на список строк, убирая символы переноса
    words = text.split() #Убирает отступы
    return {
        "Строк" : len(lines),
        "Слов" : len(words),
        "Символов" : len(text),
        "Символов без пробелов": len("".join(words)),
        "Пустых строк" : sum(1 for line in lines if not line.strip())
    }

def write_report(path: Path, stats: dict[str,int]) -> None:
    #Записываем отчёт в файл
    lines = [f"{k}:{i}" for k,i in stats.items()]
    path.write_text("\n".join(lines) + "\n", encoding ="utf-8")

if __name__ == "__main__":
    sample(INPUT)
    stats = analyze(INPUT)

    print(f"Файл: {INPUT.name}")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    write_report(REPORT, stats)
    print(f"Отчёт записан в {REPORT.name}")