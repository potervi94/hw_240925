# -*- coding: utf-8 -*-
# Курс: AI+Python
# Модуль 13. Пакування даних
# Тема: JSON. Частина 1
#  Завдання 1
# Напишіть гру вгадати число: комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до
# правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та
# програшів у файл
#  завантажити дані – завантажити кількості перемог
# та програшів
# Реалізуйте все функціями

import random
from typing import NoReturn

def generate_secret_number(low: int = 1, high: int = 100) -> int:
    """
    'Загадування числа': повертає випадкове число в діапазоні [low, high].
    """
    if low > high:
        raise ValueError(f"Невірний діапазон: {low} має бути <= {high}")
    return randint(low, high)


def start_new_game(tries: int = 5) -> None:
    """Почати нову гру: користувач вводить числа до правильної відповіді."""
    secret = generate_secret_number(1, 100)
    attempts_left = tries

    while attempts_left > 0:
        print(f"Залишилось спроб: {attempts_left}")
        raw = input("Вгадайте число (1..100): ").strip()
        if not raw.isdigit():
            print("Введіть ціле число.")
            continue

        guess = int(raw)
        if guess < secret:
            print("Загадане число більше.")
        elif guess > secret:
            print("Загадане число менше.")
        else:
            print("Вітаю! Ви вгадали число!")
            break

        attempts_left -= 1
    else:
        # Блок else виконається, якщо цикл не був перерваний break (спроби закінчились)
        print(f"Спроби вичерпано. Число було: {secret}")


def show_results() -> None:
    """Вивести результат: кількість перемог та програшів."""
    pass


def save_stats_to_file() -> None:
    """Зберегти дані: кількості перемог та програшів у файл."""
    pass


def load_stats_from_file() -> None:
    """Завантажити дані: кількості перемог та програшів з файлу."""
    pass


def print_menu() -> None:
    """Вивести текстове меню."""
    print("\nМеню:")
    print("1) Почати нову гру")
    print("2) Вивести результат")
    print("3) Зберегти дані у файл")
    print("4) Завантажити дані з файлу")
    print("0) Вихід")


def handle_choice(choice: str) -> bool:
    """
    Обробити вибір користувача.
    Повертає True, якщо слід продовжити роботу меню; False — для виходу.
    """
    if choice == "1":
        start_new_game()
    elif choice == "2":
        show_results()
    elif choice == "3":
        save_stats_to_file()
    elif choice == "4":
        load_stats_from_file()
    elif choice == "0":
        return False
    else:
        print("Невірний вибір. Спробуйте ще раз.")
    return True


def main() -> NoReturn:
    """Головний цикл меню."""
    while True:
        print_menu()
        user_input = input("Ваш вибір: ").strip()
        if not handle_choice(user_input):
            print("Вихід із програми.")
            raise SystemExit(0)


if __name__ == "__main__":
    main()
