#Задача 1 - квадрат чисел
def num(nums: list[int]) -> list[int]:
    return [x * x for x in nums if x % 2 ==0]
print(num([1,2,3,4,5,6,7,8,9,10]))

#Задача 2 -  Поменять ключи и значения местами  
#dict - это словарь
def key(replace: dict) -> dict:
    return {f: i for i, f in replace.items()}
print(key({"key" : 4}))

#Задача 3 -Фильтрация слов с определенным количество символов
def filter_word(words: list[str],count: int) -> list[str]:
    return [word for word in words if len(word) == count]
print(filter_word(["Максим","Денис","Влад"], 4))

#Задача 4 Словарь с длиной текста
def key_lengths(d: dict) -> dict:
    return {key: len(key) for key in d}
print(key_lengths({"Слово": "Влад ", "Влад": "слово"}))

#Задача 5 Множество ключей двух словарей
def mnojest(word: dict, word2 : dict) -> set:
    return {i for i in word if i in word2}
print(mnojest({"a": 1, "b": 2}, {"b": 3, "c": 4}))