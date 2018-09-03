import requests

import selenium

import wheel

import aiohttp

import lxml

import pyquery

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FOptions
from selenium.webdriver.chrome.options import Options as COptions
import tesserocr

import pymysql

import pymongo

import redis

from flask import Flask

import tornado.ioloop
import tornado.web
import gerapy
# driver = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe")
# driver1 = webdriver.Firefox(executable_path="D:\PDF\py包\geckodriver_win64\geckodriver.exe")

# Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
# 分手了  可以采用浏览器无头模式
# browser = webdriver.PhantomJS(executable_path="D:\PDF\py包\phantomjs\phantomjs.exe")
# browser.get("www.baidu.com")
"""
无头模式
"""
# options = COptions()
# options.add_argument('-headless')
# driver = webdriver.Chrome(executable_path="D:\PDF\py包\chromedriver_win32\chromedriver.exe",
#                           chrome_options=options)
# driver.get("http://www.sina.com")
# print(driver.current_url)

# soup = BeautifulSoup("<p>HELLO<p/>", "lxml")
# print(soup.p.string)
# 验证码
# print(tesserocr.file_to_text("../pic/1.png"))
# SQL
# print(pymysql.version_info)
# print(pymongo.version)
# print(redis.VERSION)
#flask
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello():
#     return "hello world"
#
#
# if __name__ == "__main__":
#     app.run()


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")


def make_app():
    return tornado.web.Application([(r"/", MainHandler), ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()