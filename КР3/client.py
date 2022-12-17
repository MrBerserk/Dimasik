""" Клиент для тестирования сервера """

import socket
import json

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5064))


def prepare_message(data):
    # подготовливаем данные для отправки
    return (json.dumps(data, ensure_ascii=False) + ";").encode('utf-8')


def send(data):
    # отправляем данные на сервер
    client.send(prepare_message(data))


def get_tickets():
    send({'type': 'get_tickets'})
    tickets = json.loads(client.recv(1024).decode('utf-8'))
    print('tickets:', tickets)
    return tickets


def add_ticket(text):
    print('add ticket', text)
    send({'type': 'add_ticket', 'text': text})


def delete_ticket(ticket_id):
    print('delete ticket', ticket_id)
    send({'type': 'delete', 'ticket_id': ticket_id})


def edit_ticket(ticket_id, text):
    print('edit ticket', ticket_id, text)
    send({'type': 'edit', 'ticket_id': ticket_id, 'text': text})


# Тестирование функциональности
if __name__ == '__main__':
    print("""
        print
        add <text>
        delete <id>
        edit <id> <text>
    """)

    while True:
        command = input()
        if command == 'print':
            get_tickets()
        elif command.startswith('add '):
            add_ticket(command[4:])
        elif command.startswith('delete '):
            delete_ticket(command[7:])
        elif command.startswith('edit '):
            msg = command[5:].split()
            edit_ticket(msg[0], msg[1])


