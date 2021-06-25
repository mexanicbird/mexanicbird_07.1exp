"""импорт библиотек"""
from flask import Flask, render_template, url_for, request, session, redirect, abort, g, flash
from var import t1, t2, h1, h2, p1
import sqlite3
import os
from FDataBase import FDataBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required
from UserLogin import UserLogin
from socket_001 import start_server
import socket_001

"""Конфигурация"""
DATABASE = 'tmp/dtsite.db'
DEBUG = True
SECRET_KEY = 'fnfuk3h46havhdi68kyop35ergc'
application = Flask(__name__)
application.config.from_object(__name__)
application.config.update(dict(DATABASE=os.path.join(application.root_path, 'dtsite.db')))
login_manager = LoginManager(application)


@login_manager.user_loader
def load_user(user_id):
    print("load user")
    return UserLogin().fromDB(user_id, dbase)

    '''Подключаем базу данных'''
def connect_db():
    conn = sqlite3.connect(application.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

    """Вспомогательная функция для создания БД для создания"""
def create_db():
    db = connect_db()
    with application.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
        db.commit()
        db.close()

    """Вспомогательная функция установления связи с БД"""
def get_db():
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db

    '''устанавливаем соединение с базой данных перед каждым запросом'''
dbase = None

@application.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)

    """Вспомогательная функция завершения связи с БД"""
@application.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()

    '''страница логина и начальная'''
@application.route("/")
@application.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = dbase.getUserByUsers(request.form['users'])
        if user and check_password_hash(user['psw'], request.form['psw']):
            userlogin = UserLogin().create(user)
            login_user(userlogin)
            return redirect(url_for("main"))
        flash('Неверная пара логин/пароль', 'error')
    return render_template("login.html", title='Авторизация')

    '''страница'''
@application.route("/main", methods=["POST", "GET"])
@login_required
def main():
    start_server()
    print(url_for("main"))
    return render_template("main.html", title='Главный экран')

    '''страница'''
@application.route("/moskowhole")
@login_required
def moskowhole():
    '''итеррация сервера получения данных'''
    start_server()
    print(url_for("moskowhole"))
    return render_template("moskowhole.html", title='Московская нора',
                           t1=socket_001.s1_t1, t2=socket_001.s1_t2,
                           h1=socket_001.s1_h1, h2=socket_001.s1_h2, p1=socket_001.s1_p1)

    '''страница'''
@application.route("/southhole")
@login_required
def southhole():
    start_server()
    print(url_for("southhole"))
    return render_template("southhole.html", title='Южная нора', test = dbase.GetMenu())

    '''страница'''
@application.route("/work_1")
@login_required
def work_1():
    start_server()
    print(url_for("work_1"))
    return render_template("work_1.html", title='Рабочий проект_1')

    '''страница'''
@application.route("/work_2")
@login_required
def work_2():
    start_server()
    print(url_for("work_2"))
    return render_template("work_2.html", title='Рабочий проект_2')

'''активация сервера получения данных'''
#start_server()
#start_server()
#start_server()


'''для запуска на локальном хосте + включение отладки в браузере'''
if __name__ =="__main__":
    application.run(debug=True, host = '127.0.0.1')


#if __name__ == "__main__":
    #application.run(host='31.31.196.213')