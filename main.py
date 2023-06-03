"""Урок 8. Работа с файлами
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.

Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной"""
import os

def input_contact():
    """Функция для добавления нового контакта"""
    surname = input("Фамилия:")
    name = input("Имя:")
    middle_name = input("Отчество:")
    phone_number = input("Номер телефона:")
    return surname + " " + name + " " + middle_name + " " + phone_number

def save_contact(contact, file):
    """Функция для сохранения контакта в файл"""
    with open(file, "a") as f:
        f.write(contact + "\n")

def search_contacts(file):
    """Функция для поиска контактов"""
    print("Выберите параметр для поиска:\n1. Фамилия\n2. Имя\n3. Отчество\n4. Номер телефона")
    option = input()
    query = input("Введите значение для поиска:\n")
    with open(file, "r") as f:
        for line in f:
            if option == "1" and query in line.split()[0]:
                print(line)
            elif option == "2" and query in line.split()[1]:
                print(line)
            elif option == "3" and query in line.split()[2]:
                print(line)
            elif option == "4" and query in line.split()[3]:
                print(line)

def export_contacts(file):
    """Функция для экспорта всех контактов в файл"""
    with open(file, "r") as f_read:
        with open("exported_contacts.txt", "w") as f_write:
            f_write.write(f_read.read())

def main():
    filename = "file.txt"
    while True:
        print("1. Добавить контакт\n2. Поиск контактов\n3. Экспорт контактов\n4. Выход")
        choice = input("Введите номер действия:\n")
        if choice == "1":
            contact = input_contact()
            save_contact(contact, filename)
        elif choice == "2":
            search_contacts(filename)
        elif choice == "3":
            export_contacts(filename)
        elif choice == "4":
            break
        else:
            print("Некорректный выбор")
def search_contacts(file):
    """Функция для поиска контактов"""
    print("Выберите параметр для поиска:\n1. Фамилия\n2. Имя\n3. Отчество\n4. Номер телефона")
    option = input()
    query = input("Введите значение для поиска:\n")
    found = 0
    with open(file, "r") as f:
        for line in f:
            if option == "1" and query in line.split()[0]:
                print(line)
                found += 1
            elif option == "2" and query in line.split()[1]:
                print(line)
                found += 1
            elif option == "3" and query in line.split()[2]:
                print(line)
                found += 1
            elif option == "4" and query in line.split()[3]:
                print(line)
                found += 1
    print(f"Найдено {found} записей.")
if __name__ == "__main__":
    main()
