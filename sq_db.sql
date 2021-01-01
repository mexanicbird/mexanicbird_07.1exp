CREATE TABLE IF NOT EXISTS mainmenu (
id integer PRIMARY KEY AUTOINCREMENT,
title text NOT NULL,
url text NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
id integer PRIMARY KEY AUTOINCREMENT,
name text NOT NULL,
users text NOT NULL,
psw text NOT NULL
);

CREATE TABLE IF NOT EXISTS Ambient_St1 (
id integer PRIMARY KEY AUTOINCREMENT,
tempIN float NOT NULL,
himIN float NOT NULL,
PresIN float NOT NULL,
RainA integer NOT NULL,
RainD integer NOT NULL,
tempOUT float NOT NULL,
himOUT float NOT NULL,
time integer NOT NULL
);