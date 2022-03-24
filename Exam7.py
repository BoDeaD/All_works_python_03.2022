'''
Задание 11 и Задание 13

Нужно написать авторизацию пользователя (Логин)
Поля:
phone - телефон пользователя
password - пароль пользователя

При нажатии на кнопку "Login"
Должна пройти провера, что такой юзер уже есть в базе
и сравнить его пароль, если пароль не совпадает, то вывести ошибку.
Если пароль и почта совпадает, то вывести сообщение - "Ты успешно залогинился!"

|---------------------------------------|
|                Phone                  |
|          /-------------/              |
|          /             /              |
|          /-------------/              |
|             Password                  |
|          /-------------/              |
|          /             /              |
|          /-------------/              |
|                                       |
|        /---------------/              |
|        /     Логин     /              |
|        /---------------/              |
|---------------------------------------|

'''
from tkinter import *
import json
root = Tk()
root.geometry(f'{WIDTH}x{HEIGHT}')
root.title(TITLE)



WIDTH = 550
HEIGHT = 550
TITLE = 'Exam_register'


user = {
    'email': '',
    'password': '',
    'fio': '',
    'phone_number': '',
    'nickname': ''
}

fields = {
    'email': '',
    'fio': '',
    'phone number': '',
    'nickname': '',
    'password': '',
    'confirm password': ''
}


def set_field():
    global fields
    for key in fields:
        label = Label(text=f'{key.title()}: ',
                            font=('Arial', 20, 'bold'))
        label.pack()
        fields[key] = Entry(font=('Arial', 20))
        fields[key].pack()


def set_error(error_title):
    global error_field
    error_field.config(text=error_title)


def save_data():
    global fields, user
    f = open('data.txt', 'a')
    user['email'] = fields['email'].get()
    user['password'] = fields['password'].get()
    user['fio'] = fields['fio'].get()
    user['phone_number'] = fields['phone number'].get()
    user['nickname'] = fields['nickname'].get()
    f.write(json.dumps(user))
    f.close()


def registration():
    global fields, error_field
    for key in fields:
        if len(fields[key].get()) == 0:
            set_error('Нужно заполнить все поля')
            return False
    if fields['password'].get() != fields['confirm password'].get():
        set_error('Пароли не совпадают!')
        return False
    if fields['email'].get().find('@') == -1:
        set_error('Email должен содержать символ \'@\'!')
        return False
    save_data()
    return True




set_field()

error_field = Label(text='', font=('Arial', 20), fg='red')
error_field.pack()
registration_button = Button(
    text='Зарегистрироваться',
    font=('Arial', 20)
)
registration_button.config(command=registration)
registration_button.pack()

root.mainloop()
