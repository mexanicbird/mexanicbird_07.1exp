"""импорт библиотек"""
from socket_001 import res_a_fl, res_f_fl, res_c_fl, res_d_fl, res_e_fl, res_g_fl,\
    res_h_fl, res_i_fl, res_k_fl, res_l_fl, time_now

'''объявляем переменные'''
t1 = 11.1
t2 = 22.2
h1 = 33.3
h2 = 44.4
p1 = 555.5
s1_t1 = None
s1_t2 = None
s1_h1 = None
s1_h2 = None
s1_p1 = None
s2_t1 = None
s2_t2 = None
s2_h1 = None
s2_h2 = None
s2_p1 = None
time_recive_data = []

'''присваиваем значения'''
if res_a_fl != None:
    s1_t1 = res_a_fl

if res_f_fl != None:
    s1_t2 = res_f_fl

if res_c_fl != None:
    s1_h1 = res_c_fl

if res_d_fl != None:
    s1_h2 = res_d_fl

if res_e_fl != None:
    s1_p1 = res_e_fl

if res_g_fl != None:
    s2_t1 = res_g_fl

if res_h_fl != None:
    s2_t2 = res_h_fl

if res_i_fl != None:
    s2_h1 = res_i_fl

if res_k_fl != None:
    s2_h2 = res_k_fl

if res_l_fl != None:
    s2_p1 = res_l_fl

if time_now != None:
    time_recive_data = time_now




