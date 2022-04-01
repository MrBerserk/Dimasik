import csv
import datetime

class User:
    def __init__(self, id, name, second_name, age):
        self.id = id
        self.name = name
        self.second_name = second_name
        self.age = age

    def get_dict_from_user(self):
        return {
            'id': self.id,
            'name': self.name,
            'second_name': self.second_name,
            'age': self.age,
        }

class UsersData:

    def __init__(self, file_path, columns):
        self.file_path = file_path
        self.columns = columns

    def clear(self):
        with open(self.file_path, 'w') as file:
            pass

    def add_user(self, user_obj):
        with open(self.file_path, 'a') as file:
            writer = csv.DictWriter(
                file, delimiter=';', fieldnames=self.columns)
            writer.writerow(user_obj.get_dict_from_user())

    def delete_user(self, user_id):
        users_list_csv = self.get_list_of_users()
        index = None
        for idx, user in enumerate(users_list_csv):
            if int(user['id']) == user_id:
                index = idx
        if index is not None:
            users_list_csv.pop(index)
            with open(self.file_path, 'w') as file:
                writer = csv.DictWriter(
                    file, delimiter=';', fieldnames=self.columns)
                writer.writerows(users_list_csv)
        else:
            raise Exception(f'cant find user with id {user_id}')

    def get_list_of_users(self):
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)
            return [line for line in reader]

    def get_user(self, user_id):
        with open(self.file_path, 'r') as file:
            user = None
            reader = csv.DictReader(
                file, delimiter=';', fieldnames=self.columns)

            for user_csv in reader:
                if int(user_csv['id']) == user_id:
                    user = user_csv

            return user

    def go_messages(self, user_obj1, user_obj2):
        """Метод передачи сообщения пользователю от другого"""
        with open("../../Projects/Инфа/message.csv", "a+", newline='') as message:
            otpravitel = user_obj1
            poluchatel = user_obj1
            sender = input("Сообщение:")
            w = csv.w(message, delimiter =';', lineterminator="")
            w.writerow(f'Время сообщения:{datetime.datetime.now()},'
                    f'Отправитель:{otpravitel}, '
                    f'Получатель:{poluchatel}, '
                    f'Сообщение{sender})'
            )
            w.writerow("\n")

    def deleate_message(self):
        """Метод удаления всех сообщений"""
        with open("../../Projects/Инфа/message.csv", newline="") as input_file:
            with open("../../Projects/Инфа/message.csv", "w", newline="") as out_file:
                w = csv.reader(input_file):
                for row in csv.reader(input_file)
                    if any(row):
                        w.writerow(row)

    def give_all_message(self):
        """Отображает все сообщения"""
        with open("message_file.csv", "r") as message_file:
            reader = csv.reader(message_file)
            Name = set(row[2] for row in reader)
        with open("message_file.csv", "r") as message_file:
            reader = csv.reader(message_file)
            Text = set(row[0] for row in reader)
        return f'Сообщения: {Text}\nОтправители: {Name}'

    def show_message(self):





data_obj = UsersData(
    'users.csv', ['id', 'name', 'second_name', 'age', ])

user1 = User(1, 'Vasya', 'Vaskin', 18, )
user2 = User(2, 'Vasya2', 'Vaskin2', 18,)

data_obj.add_user(user1)
data_obj.add_user(user2)

print(data_obj.get_list_of_users())
print(data_obj.get_user(2))
data_obj.delete_user(2)
print(data_obj.get_list_of_users())