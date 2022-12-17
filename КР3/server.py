import socket
import threading
import json
import uuid

# создаем сокет
host = '127.0.0.1'
port = 5064
server = socket.socket()
server.bind((host, port))
server.listen()


# хранилище данных
data = {}


def listen_messages(socket):
    """ Функция для получения json-сообщений от клиента (разделителем является ';') """

    buffer = ''
    while True:
        binary = socket.recv(1024)
        if len(binary) == 0:

            continue
        message = binary.decode('utf-8')
        buffer += message

        messages = buffer.split(';')
        buffer = messages[-1]
        for msg in messages[:-1]:
            yield json.loads(msg)


def handle(client, key):
    """ Функция обработки данных клиента """

    # если возникает ошибка - закрываем соединение
    try:
        for msg in listen_messages(client):
            print('get', msg)
            if msg['type'] == 'get_tickets':
                result = data[key]['tickets']
                client.send(json.dumps(result, ensure_ascii=False).encode('utf-8'))

            elif msg['type'] == 'add_ticket':
                data[key]['tickets'].append({
                    'ticket_id': str(uuid.uuid4()),
                    'text': msg['text'],
                })

            elif msg['type'] == 'delete':
                new_tickets = []
                for ticket in data[key]['tickets']:
                    if ticket['ticket_id'] != msg['ticket_id']:
                        new_tickets.append(ticket)
                data[key]['tickets'] = new_tickets

            elif msg['type'] == 'edit':
                for ticket in data[key]['tickets']:
                    if ticket['ticket_id'] == msg['ticket_id']:
                        ticket['text'] = msg['text']

    except Exception as e:
        print(e)
        client.close()


def receive():
    """ Бесконечно подключаем клиентов и запускаем поток с их обработкой """

    while True:
        client, address = server.accept()
        key = str(address)
        if key not in data:
            # создаем ячейку для хранения данных клиента
            data[key] = {
                'tickets': [],
            }

        thread = threading.Thread(target=handle, args=(client, key))
        thread.start()


if __name__ == '__main__':
    receive()