#coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_head(title):
    head = "<title>" + title + "</title>"
    head += '<meta charset="utf-8">'
    return "<head>" + head + "</head>"

def generate_body(header, paragraphs: list):
    body = "<h1>" + header + "</h1>"
    for p in paragraphs:
        body += "<p>" + p + "</p>"
    return "<body>" + body + "<body>"

def save_page():
    prophecies = generate_prophecies()
    today = dt.now().date()
    body = generate_body(header= "Гороскоп на " + str(today), paragraphs=prophecies)
    head = generate_head(title= "Гороскоп")
    page = head + body



    fp = open("in.html", "w")
    print(page, file=fp)
    fp.close()

save_page()

#;fdvdfbjjkdfnbjndjkfbnjmdfnb