from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():

    return ''


if __name__ == '__main__':
    app.run()