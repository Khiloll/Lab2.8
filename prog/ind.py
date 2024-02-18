#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решить индивидуальное задание лабораторной работы 2.6,
# оформив каждую команду в виде отдельной функции.

# Функция для добавления записи в список и сортировки по датам рождения
def add_person_to_list(people_list):
    person = {}
    print("\nВведите данные о человеке:")
    person["фамилия"] = input("Фамилия: ")
    person["имя"] = input("Имя: ")
    person["знак Зодиака"] = input("Знак Зодиака: ")
    birthday = list(map(int, input("Дата рождения (через пробел дд мм гггг): ").split()))
    person["дата рождения"] = birthday
    people_list.append(person)
    people_list.sort(key=lambda x: tuple(x["дата рождения"]))
    print("Данные добавлены и упорядочены по датам рождения.")


# Функция для отображения информации о людях с определенным знаком Зодиака
def display_people_by_zodiac_sign(people_list, search_zodiac_sign):
    found = False
    print(f"\nЛюди с знаком Зодиака '{search_zodiac_sign}':")
    for person in people_list:
        if person["знак Зодиака"] == search_zodiac_sign:
            print(f"{person['фамилия']} {person['имя']} - {person['дата рождения'][0]}.{person['дата рождения'][1]}.{person['дата рождения'][2]}")
            found = True
    if not found:
        print(f"Нет людей с знаком Зодиака '{search_zodiac_sign}'.")


# Создание списка людей в виде словарей
people_data = []

# Добавление данных о людях и сортировка по датам рождения
add_person_to_list(people_data)
add_person_to_list(people_data)

# Ввод знака Зодиака для поиска
searched_zodiac_sign = input("\nВведите знак Зодиака для поиска: ")
display_people_by_zodiac_sign(people_data, searched_zodiac_sign)
