import socket
from termcolor import colored



"""функция получения данных от домашнего сервера"""
def receive_data_from_server():
    """подключение сокета"""
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected:', addr)

    """цикл передачи данных"""
    while True:
        data = conn.recv(4096)
        print(colored("data from home server", 'green', attrs=['reverse', 'blink']))
        print(data)
        if not data:
            break
        """обратная отправка данных"""
        conn.send(data)

    """Закрываем подключение"""
    conn.close()

i = 0
for i in range(7):
    i = i + 1
    receive_data_from_server()