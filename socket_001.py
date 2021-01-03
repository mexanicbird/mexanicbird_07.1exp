import socket
from termcolor import colored
import datetime

"""переменные"""
i = 0
res_a_str = None
res_f_str = None
res_c_str = None
res_d_str = None
res_e_str = None
res_g_str = None
res_h_str = None
res_i_str = None
res_k_str = None
res_l_str = None

res_a_float = None
res_f_float = None
res_c_float = None
res_d_float = None
res_e_float = None
res_g_float = None
res_h_float = None
res_i_float = None
res_k_float = None
res_l_float = None


"""функция получения данных от домашнего сервера"""
def receive_data_from_server():
    global res_a_str
    """подключение сокета"""
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    print('connected:', addr)

    """цикл передачи данных"""
    while True:
        """Запрос точного времени"""
        time_now = datetime.datetime.now()
        data = conn.recv(4096)
        print(colored("data from home server", 'green', attrs=['reverse', 'blink']))
        print(colored(str(time_now), 'green', attrs=['reverse', 'blink']))
        print(data)
        print(type(data))

        """обрабатываем данные"""
        data_str = data.decode('utf-8')
        print(colored(data_str, 'green', ))
        data_str_num = len(data_str)
        print(colored("Длина массива: " + str(data_str_num), 'blue'))



        """перебор массива"""

        for i in data_str:
            print(i)
            if i == 'a':
                print('333333')
                for i in data_str:
                    print('22222')
                    res_a_str = data_str[3:7]
                    res_a_float = float(res_a_str)




        print(colored("Полученные данные: ", 'yellow', attrs=['reverse', 'blink']))
        """печать выбранных строк"""
        print(colored(res_a_str, 'cyan', ))
        print(colored(res_f_str, 'cyan', ))
        print(colored(res_c_str, 'cyan', ))

        """печать переменных"""
        print(colored(res_a_float, 'magenta'))
        print(colored(res_f_float, 'magenta'))
        print(colored(res_c_float, 'magenta'))
        print('')
        """если нет данных выход из цикла"""
        if not data:
            break

        """обратная отправка данных"""
        #conn.send(data)

    """Закрываем подключение"""
    conn.close()

#j = 0
#for j in range(1):
    #j = j + 1


receive_data_from_server()