from flask import Flask, g
from cookiespool.config import *

app = Flask(__name__)


@app.route('/')
def index():
    return '<h2>欢迎来到cookies池</h2>'


def get_conn():
    for website in GENERATOR_MAP:
        if not hasattr(g, website):
            setattr(g, website + '_cookies', eval('RedisClient' + '("cookies", "' + website + '")'))
    return g


@app.route('/<website>/random')
def random(website):
    g = get_conn()
    cookies = getattr(g, website + '_cookies').random()
    return cookies