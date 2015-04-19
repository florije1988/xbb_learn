# -*- coding: utf-8 -*-
__author__ = 'kiwi'

app = Flask(__name__)
    DEBUG = True
    TESTING = True
    app.congfig.from_object(__name__)
    app.config.from_pyfile('/path/to/config/file')


if __name == '__main__':
    app.run()