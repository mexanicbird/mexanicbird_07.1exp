"""импорт библиотек"""
import socket
from termcolor import colored
import datetime
import time

"""переменные"""
res_a_str = []
res_f_str = []
res_c_str = []
res_d_str = []
res_e_str = []
res_g_str = []
res_h_str = []
res_i_str = []
res_k_str = []
res_l_str = []

res_a_fl = None
res_f_fl = None
res_c_fl = None
res_d_fl = None
res_e_fl = None
res_g_fl = None
res_h_fl = None
res_i_fl = None
res_k_fl = None
res_l_fl = None
time_now = []

"""функция получения данных от домашнего сервера"""
def receive_data_from_server():
    global res_a_fl, res_f_fl, res_c_fl, res_d_fl, res_e_fl, res_g_fl, res_h_fl, res_i_fl, \
        res_k_fl, res_l_fl, time_now
    """подключение сокета"""
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept()
    print(colored("connected:" + str(addr), 'green', attrs=['reverse', 'blink', 'bold']))
    """цикл опроса получения данных"""

    """Запрос точного времени"""
    time_now = datetime.datetime.now()

    while True:
        """пытаемся получить"""
        try:
            data = conn.recv(256)
            print(colored("Данные получены ", 'green', attrs=['reverse', 'blink']))
            """обрабатываем данные"""
            data_str = data.decode('utf-8')
            print(colored(data_str, 'green', ))
            data_str_num = len(data_str)
            print('\n')
            print(colored("data from home server", 'green', attrs=['reverse', 'blink']))
            print(colored(str(time_now) + '\n', 'green', attrs=['reverse', 'blink']))
            print(colored("Длина массива: " + str(data_str_num), 'blue', attrs=['reverse', 'blink']))

            '''условия выхода из цикла'''
            for i in data_str:
                if i == 'q':
                    print(colored("Выход по заполнению ", 'blue', attrs=['reverse', 'blink']))
                    """Закрываем подключение"""
                    conn.close()
                    break
            if not data:
                print(colored("Выход по отсутсвию данных ", 'blue', attrs=['reverse', 'blink']))
                """Закрываем подключение"""
                conn.close()
                break
        except:
            """Закрываем подключение"""
            conn.close()
            print(colored("Выход по except ", 'blue', attrs=['reverse', 'blink']))
            break

        """начало строк по меткам"""
        try:
            num_data_a = data_str.index('a')
        except:
            num_data_a = None
        try:
            num_data_f = data_str.index('f')
        except:
            num_data_f = None
        try:
            num_data_c = data_str.index('c')
        except:
            num_data_c = None
        try:
            num_data_d = data_str.index('d')
        except:
            num_data_d = None
        try:
            num_data_e = data_str.index('e')
        except:
            num_data_e = None
        try:
            num_data_g = data_str.index('g')
        except:
            num_data_g = None
        try:
            num_data_h = data_str.index('h')
        except:
            num_data_h = None
        try:
            num_data_i = data_str.index('i')
        except:
            num_data_i = None
        try:
            num_data_k = data_str.index('k')
        except:
            num_data_k = None
        try:
            num_data_l = data_str.index('l')
        except:
            num_data_l = None

        """печать положений строк"""
        print(colored("number a: " + str(num_data_a), 'blue'))
        print(colored("number f: " + str(num_data_f), 'blue'))
        print(colored("number c: " + str(num_data_c), 'blue'))
        print(colored("number d: " + str(num_data_d), 'blue'))
        print(colored("number e: " + str(num_data_e), 'blue'))
        print(colored("number g: " + str(num_data_g), 'blue'))
        print(colored("number h: " + str(num_data_h), 'blue'))
        print(colored("number i: " + str(num_data_i), 'blue'))
        print(colored("number k: " + str(num_data_k), 'blue'))
        print(colored("number l: " + str(num_data_l), 'blue'))
        print('\n')

        """перебор массива"""
        for i in data_str:
            if i == 'a':
                for i in data_str[num_data_a:data_str_num]:
                    if i == '\n':
                        break
                    else:
                        res_a_str.append(i)
            if i == 'f':
                for i in data_str[num_data_f:data_str_num]:
                    if i == '\n':
                        break
                    else:
                        res_f_str.append(i)
            if i == 'c':
                for i in data_str[num_data_c:data_str_num]:
                    if i == '\n':
                        break
                    else:
                        res_c_str.append(i)
            if i == 'd':
                for i in data_str[num_data_d:data_str_num]:
                    if i == '\n':
                        break
                    else:
                        res_d_str.append(i)
            if i == 'e':
                for i in data_str[num_data_e:data_str_num]:
                    if i == '\n':
                        break
                    else:
                        res_e_str.append(i)
            if i == 'g':
                for i in data_str[num_data_g:data_str_num]:
                    if i == '\n':
                        break
                    else:
                        res_g_str.append(i)
            if i == 'h':
                for i in data_str[num_data_h:data_str_num]:
                    if i == '\n':
                        break
                    else:
                        res_h_str.append(i)
            if i == 'i':
                for i in data_str[num_data_i:data_str_num]:
                    if i == '\n':
                        break
                    else:
                        res_i_str.append(i)
            if i == 'k':
                for i in data_str[num_data_k:data_str_num]:
                    if i == '\n':
                        break
                    else:
                        res_k_str.append(i)
            if i == 'l':
                for i in data_str[num_data_l:data_str_num]:
                    if i == '\n':
                        break
                    else:
                        res_l_str.append(i)

            #"""Закрываем подключение"""
            #if i == 'q':
               #conn.close()

        """обработка и печать выбранных строк"""

        try:
            del res_a_str[0]
        except:
            break
        try:
            del res_f_str[0]
        except:
            break
        try:
            del res_c_str[0]
        except:
            break
        try:
            del res_d_str[0]
        except:
            break
        try:
            del res_e_str[0]
        except:
            break
        try:
            del res_g_str[0]
        except:
            break
        try:
            del res_h_str[0]
        except:
            break
        try:
            del res_i_str[0]
        except:
            break
        try:
            del res_k_str[0]
        except:
            break
        try:
            del res_l_str[0]
        except:
            break

        """собираем в одну строку из списка"""
        res_a_str_b = ''.join(res_a_str)
        res_f_str_b = ''.join(res_f_str)
        res_c_str_b = ''.join(res_c_str)
        res_d_str_b = ''.join(res_d_str)
        res_e_str_b = ''.join(res_e_str)
        res_g_str_b = ''.join(res_g_str)
        res_h_str_b = ''.join(res_h_str)
        res_i_str_b = ''.join(res_i_str)
        res_k_str_b = ''.join(res_k_str)
        res_l_str_b = ''.join(res_l_str)

        print(colored("Полученные данные: ", 'green', attrs=['reverse', 'blink']))
        print(colored("Переменные в строках: ", 'green', attrs=['reverse', 'blink']))
        """печать переменных в строках"""
        print(colored(res_a_str, 'green', ))
        print(colored(res_f_str, 'green', ))
        print(colored(res_c_str, 'green', ))
        print(colored(res_d_str, 'green', ))
        print(colored(res_e_str, 'green', ))
        print(colored(res_g_str, 'green', ))
        print(colored(res_h_str, 'green', ))
        print(colored(res_i_str, 'green', ))
        print(colored(res_k_str, 'green', ))
        print(colored(res_l_str, 'green', ))
        print('\n')

        """переводим во флоат"""
        try:
            res_a_fl = float(res_a_str_b)
            res_a_str.clear()
        except:
            res_a_fl = None
        try:
            res_f_fl = float(res_f_str_b)
            res_f_str.clear()
        except:
            res_f_fl = None
        try:
            res_c_fl = float(res_c_str_b)
            res_c_str.clear()
        except:
            res_c_fl = None
        try:
            res_d_fl = float(res_d_str_b)
            res_d_str.clear()
        except:
            res_d_fl = None
        try:
            res_e_fl = float(res_e_str_b)
            res_e_str.clear()
        except:
            res_e_fl = None
        try:
            res_g_fl = float(res_g_str_b)
            res_g_str.clear()
        except:
            res_g_fl = None
        try:
            res_h_fl = float(res_h_str_b)
            res_h_str.clear()
        except:
            res_h_fl = None
        try:
            res_i_fl = float(res_i_str_b)
            res_i_str.clear()
        except:
            res_i_fl = None
        try:
            res_k_fl = float(res_k_str_b)
            res_k_str.clear()
        except:
            res_k_fl = None
        try:
            res_l_fl = float(res_l_str_b)
            res_l_str.clear()
        except:
            res_l_fl = None

        """печать переменных флоат"""
        print(colored("Переменные флоат: ", 'magenta', attrs=['reverse', 'blink']))
        print(colored(res_a_fl, 'magenta'))
        print(colored(res_f_fl, 'magenta'))
        print(colored(res_c_fl, 'magenta'))
        print(colored(res_d_fl, 'magenta'))
        print(colored(res_e_fl, 'magenta'))
        print(colored(res_g_fl, 'magenta'))
        print(colored(res_h_fl, 'magenta'))
        print(colored(res_i_fl, 'magenta'))
        print(colored(res_k_fl, 'magenta'))
        print(colored(res_l_fl, 'magenta'))
        print('')

        """обратная отправка данных"""
        # conn.send(data)

    """обнуляем массивы"""
    res_a_str.clear()
    res_f_str.clear()
    res_c_str.clear()
    res_d_str.clear()
    res_e_str.clear()
    res_g_str.clear()
    res_h_str.clear()
    res_i_str.clear()
    res_k_str.clear()
    res_l_str.clear()

    """Закрываем подключение"""
    #conn.close()

    """Возвращаем переменные"""
    return res_a_fl, res_f_fl, res_c_fl, res_d_fl, res_e_fl, res_g_fl, res_h_fl, res_i_fl, \
        res_k_fl, res_l_fl, time_now

def print_Data_001(y):
    print(colored("Итерация:  " + str(y) + "                ", 'white', attrs=['reverse', 'blink']))
    print(colored("Время выполнения:  " + str(round((time.time() - start_time), 3)) +
                  " секунд", 'white', attrs=['reverse', 'blink']))


"""цикл функции"""
j = 0
while True:
    j = j + 1
    """Подсчет времени выполнения"""
    start_time = time.time()

    """основная функция"""
    try:
        receive_data_from_server()
    except:
        print(colored("Ошибка выполнения функции", 'yellow', attrs=['reverse', 'blink']))

    """печать сведений функции"""
    print_Data_001(j)
    print('\n')
