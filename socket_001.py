"""импорт библиотек"""
import socket
from termcolor import colored
import datetime

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



        """перебор массива"""
        for i in data_str:
            print(i)
            if i == 'a':
                for i in data_str:
                   if i == '\n':
                       break
                   else:
                       res_a_str.append(i)

        for i in data_str:
            print(i)
            if i == 'f':
                print('ffff')
                for i in data_str:
                    if i == '\n':
                        print('cccc')
                        break
                    else:
                        print('eeee')
                        res_f_str.append(i)





        print(colored("Полученные данные: ", 'yellow', attrs=['reverse', 'blink']))
        """обработка и печать выбранных строк"""
        del res_a_str[0]
        #res_a_str.pop(0)
        res_a_str_b = ''.join(res_a_str)
        res_a_float = float(res_a_str_b)
        print(colored(res_a_str, 'cyan', ))
        print(colored(res_a_str_b, 'cyan', ))


        print(colored(res_f_str, 'green', ))



        print(colored(res_c_str, 'cyan', ))

        """печать переменных"""
        print(colored(res_a_float, 'magenta'))
        res_a_str.clear()
        print(colored(res_f_float, 'magenta'))
        res_a_str.clear()
        print(colored(res_c_float, 'magenta'))
        res_a_str.clear()
        print('')
        """если нет данных выход из цикла"""
        if not data:
            break

        """обратная отправка данных"""
        #conn.send(data)

    """Закрываем подключение"""
    conn.close()

#j = 0
#for j in range(7):
    #j = j + 1
receive_data_from_server()