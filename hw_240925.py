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
from random import randint
import json
from typing import NoReturn


STATS_FILE = "stats.json"
_stats: dict[str, int] = {"wins": 0, "losses": 0}


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
        if not raw.lstrip("-").isdigit():
            print("Введіть ціле число.")
            continue

        guess = int(raw)
        if guess < secret:
            print("Загадане число більше.")
        elif guess > secret:
            print("Загадане число менше.")
        else:
            print("Вітаю! Ви вгадали число!")
            _stats["wins"] = _stats.get("wins", 0) + 1
            break

        attempts_left -= 1
    else:
        # Відпрацьовує, якщо не було break (користувач не вгадав)
        print(f"Спроби вичерпано. Число було: {secret}")
        _stats["losses"] = _stats.get("losses", 0) + 1


def show_results() -> None:
    """Вивести результат: кількість перемог та програшів."""
    print(f"Перемоги: {_stats.get('wins', 0)}, Програші: {_stats.get('losses', 0)}")


def save_stats_to_file(file_path: str | None = None) -> None:
    """Зберегти дані: кількості перемог та програшів у файл (JSON)."""
    path = file_path or STATS_FILE
    try:
        with open(path, "w", encoding="utf-8") as f:
            json.dump(_stats, f, ensure_ascii=False, indent=2)
        print(f"Статистику збережено у файл: {path}")
    except OSError as e:
        print(f"Помилка збереження у файл '{path}': {e}")


def load_stats_from_file(file_path: str | None = None) -> None:
    """Завантажити дані: кількості перемог та програшів з файлу (JSON)."""
    path = file_path or STATS_FILE
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        # Валідація та приведення
        wins = int(data.get("wins", 0))
        losses = int(data.get("losses", 0))
        if wins < 0 or losses < 0:
            raise ValueError("Числа мають бути невід’ємними.")
        _stats["wins"] = wins
        _stats["losses"] = losses
        print(f"Статистику завантажено з файлу: {path}")
    except FileNotFoundError:
        print(f"Файл '{path}' не знайдено. Використовую початкові значення.")
    except (OSError, ValueError, json.JSONDecodeError) as e:
        print(f"Помилка завантаження з файлу '{path}': {e}")


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
