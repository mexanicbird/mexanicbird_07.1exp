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
        try:
            data = conn.recv(4096)
        except:
            break
        print(colored("data from home server", 'green', attrs=['reverse', 'blink']))
        print(colored(str(time_now) + '\n', 'green', attrs=['reverse', 'blink']))
        #print(data)
        #print(type(data))

        """обрабатываем данные"""
        data_str = data.decode('utf-8')
        print(colored(data_str, 'green', ))
        data_str_num = len(data_str)
        print(colored("Длина массива: " + str(data_str_num), 'blue'))

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
        print(colored("aaa: " + str(num_data_a), 'blue'))
        print(colored("fff: " + str(num_data_f), 'blue'))
        print(colored("ccc: " + str(num_data_c), 'blue'))
        print(colored("ddd: " + str(num_data_d), 'blue'))
        print(colored("eee: " + str(num_data_e), 'blue'))
        print(colored("ggg: " + str(num_data_g), 'blue'))
        print(colored("hhh: " + str(num_data_h), 'blue'))
        print(colored("iii: " + str(num_data_i), 'blue'))
        print(colored("kkk: " + str(num_data_k), 'blue'))
        print(colored("lll: " + str(num_data_l), 'blue'))
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

            """Закрываем подключение"""
            if i == 'q':
                conn.close()

        print(colored("Полученные данные: ", 'yellow', attrs=['reverse', 'blink']))
        """обработка и печать выбранных строк"""

        """обнуляем массив"""
        try:
            del res_a_str[0]
            del res_f_str[0]
            del res_c_str[0]
            del res_d_str[0]
            del res_e_str[0]
            del res_g_str[0]
            del res_h_str[0]
            del res_i_str[0]
            del res_k_str[0]
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


        """переводим во флоат"""
        try:
            res_a_float = float(res_a_str_b)
            res_f_float = float(res_f_str_b)
            res_c_float = float(res_c_str_b)
            res_d_float = float(res_d_str_b)
            res_e_float = float(res_e_str_b)
            res_g_float = float(res_g_str_b)
            res_h_float = float(res_h_str_b)
            res_i_float = float(res_i_str_b)
            res_k_float = float(res_k_str_b)
            res_l_float = float(res_l_str_b)
        except:
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
        """печать переменных флоат"""
        print(colored(res_a_float, 'magenta'))
        res_a_str.clear()
        print(colored(res_f_float, 'magenta'))
        res_a_str.clear()
        print(colored(res_c_float, 'magenta'))
        res_a_str.clear()
        print(colored(res_d_float, 'magenta'))
        res_d_str.clear()
        print(colored(res_e_float, 'magenta'))
        res_e_str.clear()
        print(colored(res_g_float, 'magenta'))
        res_g_str.clear()
        print(colored(res_h_float, 'magenta'))
        res_h_str.clear()
        print(colored(res_i_float, 'magenta'))
        res_i_str.clear()
        print(colored(res_k_float, 'magenta'))
        res_k_str.clear()
        print(colored(res_l_float, 'magenta'))
        res_l_str.clear()
        print('')
        """если нет данных выход из цикла"""
        if not data:
            break

        """обратная отправка данных"""
        #conn.send(data)

    """Закрываем подключение"""
    #conn.close()

def print_Data_001(j):
    print(colored("Iteration  " + str(j) + ":", 'red', attrs=['reverse', 'blink']))


j = 0
while True:
    j = j + 1
    receive_data_from_server()
    print_Data_001(j)
    time.sleep(1)