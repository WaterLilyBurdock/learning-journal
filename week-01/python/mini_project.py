"""CLI: путь к файлу → топ-5 самых частых слов.

Использование:
    python mini_project.py sample.txt
    python mini_project.py sample.txt --top 10
    python mini_project.py sample.txt --ignore-stopwords
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

STOPWORDS = {
    "и", "в", "во", "не", "что", "он", "на", "я", "с", "со", "как",
    "а", "то", "все", "она", "так", "его", "но", "да", "ты", "к", "у",
    "the", "a", "an", "and", "or", "of", "to", "in", "is", "it",
}


def read_text(path: Path) -> str:
    """Прочитать текст, понятно сообщив об ошибках."""
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise SystemExit(f"Ошибка: файл не найден: {path}")
    except UnicodeDecodeError:
        raise SystemExit(f"Ошибка: файл не в UTF-8: {path}")
    except IsADirectoryError:
        raise SystemExit(f"Ошибка: это директория, а не файл: {path}")


def tokenize(text: str) -> list[str]:
    """Разбить текст на слова: только буквы/цифры, в нижнем регистре."""
    return re.findall(r"\w+", text.lower(), flags=re.UNICODE)


def top_words(
    words: list[str],
    top: int = 5,
    ignore_stopwords: bool = False,
) -> list[tuple[str, int]]:
    """Топ-N слов по частоте. При равенстве — лексикографический порядок."""
    filtered = [w for w in words if w not in STOPWORDS] if ignore_stopwords else words
    counter = Counter(filtered)
    return sorted(counter.items(), key=lambda kv: (-kv[1], kv[0]))[:top]


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Топ слов по частоте в файле")
    p.add_argument("path", type=Path, help="путь к текстовому файлу (.txt)")
    p.add_argument("--top", type=int, default=5, help="сколько слов вывести (по умолчанию 5)")
    p.add_argument(
        "--ignore-stopwords",
        action="store_true",
        help="игнорировать предлоги, союзы и т.п.",
    )
    args = p.parse_args(argv)
    if args.top <= 0:
        p.error("--top должен быть положительным")
    return args


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    text = read_text(args.path)
    words = tokenize(text)

    if not words:
        print("Файл не содержит слов.")
        return 0

    print(f"Файл: {args.path}  (слов: {len(words)})")
    for i, (word, count) in enumerate(
        top_words(words, args.top, args.ignore_stopwords), start=1
    ):
        print(f"{i}. {word:<15} {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())