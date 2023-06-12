from postgres import Postgres


def h():
    print("""
    crt       - создать таблицы базы данных (clients, phones)
    del_all   - удалить таблицы базы данных, созданные командой crt
    q         - прервать выполенение программы
    add_cl    - добавить нового клиента
    add_ph    - добавить телефон для существующего клиента (по id клиента)
    change    - изменить данные клиента (по id клиента)
    del_ph    - удалить телефон клиента (по id телефона)
    del_cl    - удалить все данные клиента (по id клиента)
    find      - найти клиента по его данным
    info_cl   - показать информацию о клиенте (по id клиента)
    phones_cl - показать все телефоны клиента (по id клиента)
    all_cl    - показать id всех клиентов
    """)


def add_cl():
    name = input("Введите имя клиента: ")
    s_name = input("Введите фамилию клиента: ")
    email = str(input("Введите email клиента: "))
    if post.find_with_email(email):
        print("Ошибка: клиент с таким email уже существует")
    else:
        post.add_client(name, s_name, email)


def add_ph():
    client_id = input("Введите id клиента: ")
    if post.is_id_real(client_id)[0]:
        phone = input("Введите телефон клиента: ")
        if post.have_phone(client_id, phone)[0]:
            print("Ошибка: у клиента уже зарегестрирован этот телефон")
        else:
            post.add_phone(client_id, phone)
    else:
        print("Ошибка: клиента с таким id не существует")


def change():
    while True:
        client_id = input("Введите id клиента: ")
        if post.is_id_real(client_id)[0]:
            print("""1 - имя
            2 - фамилия
            3 - email
            4 - телефон
            5 - вернуться в предыдущее меню""")
            anything = str(input("Что меняем?: "))
            if anything == "1":
                anything = input("Введите имя: ")
                post.edit_f_name(client_id, anything)
                break
            if anything == "2":
                anything = input("Введите фамилию: ")
                post.edit_s_name(client_id, anything)
                break
            if anything == "3":
                anything = input("Введите email: ")
                post.edit_email(client_id, anything)
                break
            if anything == "4":
                phone_id = input("Введите id телефона клиента")
                if post.have_phone(client_id, anything)[0]:
                    anything = input("Введите новый номер телефона: ")
                    post.edit_phone(phone_id, anything)
                    break
                else:
                    print("Ошибка: номер телефона с таким id отсутствует в базе данных")
                    break
            if anything == "q":
                break
        else:
            print("Ошибка: клиента с таким id не существует")
            break


def del_ph():
    phone_id = input("Введите id телефона: ")
    if post.is_phone(phone_id)[0]:
        post.delete_phone(phone_id)
    else:
        print("Ошибка: телефона с таким id не существует")


def del_cl():
    client_id = input("Введите id клиента: ")
    if post.is_id_real(client_id)[0]:
        if post.is_client_phones(client_id)[0]:
            post.delete_all_phones(client_id)
        post.delete_client(client_id)
    else:
        print("Ошибка: клиента с таким id не существует")


def find():
    print("""1 - имя
2 - фамилия
3 - email
4 - телефон""")
    anything = str(input("По каким данным будем искать?: "))
    if anything == "1":
        anything = str(input("Введите имя: "))
        anything = post.find_with_name(anything)
        if anything:
            if type(anything) is list:
                print("Клиентов с таким именем: ", len(anything))
                print("Их id: ", ", ".join([str(i[0]) for i in anything]))
            else:
                print(anything[0])
                print("id клиента: ", anything[0])
        else:
            print("Клиента с таким именем не существует")
    if anything == "2":
        anything = str(input("Введите фамилию: "))
        anything = post.find_with_s_name(anything)
        if anything:
            if type(anything) is list:
                print("Клиентов с такой фамилией: ", len(anything))
                print("Их id: ", ", ".join([str(i[0]) for i in anything]))
            else:
                print("id клиента: ", anything[0])
        else:
            print("Клиента с такой фамилией не существует")
    if anything == "3":
        anything = str(input("Введите email: "))
        anything = post.find_with_email(anything)
        if anything:
            print("id клиента: ", anything[0])
        else:
            print("Клиента с таким email не существует")
    if anything == "4":
        anything = int(input("Введите телефон: "))
        anything = post.find_with_phone(anything)
        if anything:
            if type(anything) is list:
                print("Клиентов с таким телефоном: ", len(anything))
                print("Их id: ", ", ".join([str(i[0]) for i in anything]))
            else:
                print("id клиента: ", anything[0])
        else:
            print("Клиента с таким телефоном не существует")


def info_cl():
    client_id = input("Введите id клиента: ")
    if post.is_id_real(client_id)[0]:
        cl_info = post.client_info(client_id)
        print("id:", cl_info[0], " Имя:", cl_info[1], " Фамилия", cl_info[2], " Email", cl_info[3])
    else:
        print("Ошибка: клиента с таким id не существует")


def phones_cl():
    client_id = input("Введите id клиента: ")
    if post.is_id_real(client_id)[0]:
        cl_phones = post.client_phones(client_id)
        if type(cl_phones) is list:
            for i in cl_phones:
                print("id телефона:", i[0], "Номер телефона :", i[1])
        else:
            print("id телефона:", cl_phones[0], "Номер телефона :", cl_phones[1])
    else:
        print("Клиента с таким телефоном не существует")


def all_cl():
    anything = post.all_clients()
    if type(anything) is list:
        for i in anything:
            print(i[0])
    else:
        print(anything[0])


if __name__ == "__main__":
    post = Postgres()
    while True:
        print()
        print("Для справки по видам комманд введите: help")
        command = input("Ожидание команды: ")
        if command == "help":
            h()
        if command == "crt":
            post.create_tables()
        if command == "del_all":
            post.delete_all()
        if command == "q":
            break
        if command == "add_cl":
            add_cl()
        if command == "add_ph":
            add_ph()
        if command == "change":
            change()
        if command == "del_ph":
            del_ph()
        if command == "del_cl":
            del_cl()
        if command == "find":
            find()
        if command == "info_cl":
            info_cl()
        if command == "phones_cl":
            phones_cl()
        if command == "all_cl":
            all_cl()
