from flask_socketio import SocketIO
import time
from termcolor import colored
import schedule
import datetime
print(datetime.datetime.now())


def printer1():
    print(datetime.datetime.now())


schedule.every(2).seconds.do(printer1)

#while True:
    #schedule.run_pending()

#schedule.run_pending()
schedule.every(10)



#"""цикл функции"""
#j = 0
#while True:
  # j = j + 1
    #"""Подсчет времени выполнения"""
    #start_time = time.time()
    #if time.time() - start_time >= 5:
      #  print(j)
        #start_time = time.time()



#time_now = datetime.datetime.now()
   # print(colored("Время выполнения:  " + str(round((time.time() - start_time), 3)) +
                #  " секунд", 'white', attrs=['reverse', 'blink']))



#import schedule
#import time

#def job():
   # print("I'm working...")

#schedule.every(10).minutes.do(job)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)

#while True:
    #schedule.run_pending()
    #time.sleep(1)



