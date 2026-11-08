text = "Кот, пёс и кот! А пёс — не кот. И снова кот..."

def split_text(text: str) -> list[str]:
    puncts = "?,.:!"
    return [w.lower().strip(puncts) for w in text.split()]

def counter(words: list[str]) -> dict[str, int]:
    count = {}
    for w in words:
        if w not in count:
            count[w] = 1
        else:
            count[w] += 1
    return count

def top3(top: dict[str, int]) -> list[tuple[str, int]]:
    pairs = sorted(top.items(), key=lambda p: -p[1])
    return pairs[:3]

splitter_text = split_text(text)
counter_text = counter(splitter_text)
tops = top3(counter_text)

for i, (word, n) in enumerate(tops, start=1):
    print(f"{i}. {word} — {n}")