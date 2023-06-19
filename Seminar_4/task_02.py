#Напишите функцию, которая принимает строку текста.
#Сформируйте список с уникальными кодами Unicode каждого
#символа введённой строки отсортированный по убыванию.#


def ord_char(text):
    result = set()
    for item in text:
        result.add(ord(item))
        
    return sorted(result, reverse=True)

str = input ('Введите текст: ')
print(ord_char(str))
