"""Файл предназначен для реализации класса пользователя"""


class Users:
    user = dict()

    def __init__(self, chat_id, name, surname, last_name):

        self.id_chat = chat_id         # id чата *
        self.name = name               # имя пользователя *
        self.surname = surname         # ник пользователя *
        self.last_name = last_name     # фамилия пользователя *


    @classmethod
    def get_user(cls, chat_id, name, surname, last_name):
        if chat_id in cls.user.keys():
            return cls.user[chat_id]
        else:
            return cls.add_user(chat_id, name, surname, last_name)

    @classmethod
    def add_user(cls, chat_id, name, surname, last_name):
        cls.user[chat_id] = Users(chat_id, name, surname, last_name)
        return cls.user[chat_id]