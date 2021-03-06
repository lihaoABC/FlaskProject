from info.modules.index import index_blue
from flask import render_template, current_app


@index_blue.route('/')
def index():

    return render_template('news/index.html')


@index_blue.route('/favicon.ico')
def get_ico():

    return current_app.send_static_file('news/favicon.ico')
