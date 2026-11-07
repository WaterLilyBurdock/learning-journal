from collections import Counter
#Задача 1 - квадрат чисел
def count_nums(nums: list[int]) -> list[int]:
    return [num * num for num in nums if num % 2 ==0]
print(count_nums([1,2,3,4,5,6,7,8,9,10]))

#Задача 2 -  Поменять ключи и значения местами  
#dict - это словарь
def key(replace: dict) -> dict:
    return {f: i for i, f in replace.items()}
print(key({"key" : 4}))

#Задача 3 -Фильтрация слов с определенным количество символов
def filters_words(words: list[str], count : int) -> list[str]:
    return [word for word in words if len(word) == count]
print(filters_words(["Владик","Денис","Максим"],5))

#Задача 4 Словарь с длиной текста
def key_dict(word: dict) -> dict:
    return {i: len(i) for i in word}
print(key_dict({"Словарь" : "Привет меня зовут влад"}))

#Задача 5 Множество ключей двух словарей
def mnojest(word: dict, word2 : dict) -> set:
    return {i for i in word if i in word2}
print(mnojest({"a": 1, "b": 2}, {"b": 3, "c": 4}))


#Задача 6 Только положительные числа
def posizitive_nums(nums: list[int]) -> list[int]:
    return [i for i in nums if i > 0]
print(posizitive_nums([-1,2,5,-2,51,2,- 51]))

#Задача 7 только отрицательные числа
def negative_nums(nums: list[int]) -> list[int]:
    return [i for i in nums if i < 0]
print(negative_nums([1,2,-4,51,4,-5]))

#Задача 8 
def str_keys(d: dict) -> dict:
    return {k: v for k, v in d.items() if isinstance(k, str)}
print(str_keys({5: 4, "a": 1})) 

#Задача 9 """Слова длиной > min_len, приведённые к верхнему регистру."""
def upper_words(words: list[str],min_len : int) -> list[str]:
    return [word.upper() for word in words if len(word) >= min_len]
print(upper_words(["Слово","Абрикос","Максим","Ян"],3))

#Задача 10 первые буквы слов всего текста в нижнем регистре
def first_words(word : str) -> set[str]:
    return {i[0].lower() for i in word.split()}
print(first_words("Привет меня зовут Влад"))

#Задача 11 Множество последних букв всех слов текста (в нижнем регистре)
def last_words(word: str) -> set[str]:
    return {i[-1].lower() for i in word.split()}
print(last_words(" Привет Меня зовут Влад"))

#Задача 12 Множество первых букв только тех слов, чья длина больше 3.

def first_words_three(word: str) -> set[str]:
    return {i[0].lower() for i in word.split() if len(i) > 3}
print(first_words_three("Привет меня звать Ян"))

#Задача 13 Словарь {первая_буква: количество_слов_на_эту_букву} для текста.
def first_letter_counts(text: str) -> dict[str, int]:
    return dict(Counter(w[0].lower() for w in text.split()))
print(first_letter_counts("Cat dog apple ant"))

#Задача 14 Множество значения встречающихся в обеих словарях
def shared_values(d1: dict, d2: dict) -> set:
    return {i for i in d1 if i in d2}
print(shared_values({"a": 1, "b": 2}, {"b": 3, "c": 4}))