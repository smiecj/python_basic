#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# flask demo
## https://flask.palletsprojects.com/en/2.2.x/quickstart/

from flask import Flask
import logging

app = Flask(__name__)
LOG = logging.getLogger(__name__)


@app.route("/")
def hello_world():
    app.logger.info("[main] hello world!")
    LOG.info("[main] hello world from LOG")
    return "<p>Hello, World!</p>"


if __name__ != '__main__':
    # server log to gunicorn error log: https://stackoverflow.com/a/61990966
    gunicorn_error_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers.extend(gunicorn_error_logger.handlers)
    app.logger.setLevel(gunicorn_error_logger.level)
    # use pid as worker id: https://stackoverflow.com/a/55613705
    import os
    file_handler = logging.FileHandler('/tmp/smiecj_{}.log'.format(os.getpid()))
    # log file handler: https://stackoverflow.com/a/63197627
    app.logger.addHandler(file_handler)

    from flask.logging import default_handler
    app.logger.removeHandler(default_handler)

    app.logger.info("[test] not main finish init")


if __name__ == '__main__':
    # app.run(debug=True, host="0.0.0.0", port=5000)
    app.run(host="0.0.0.0", port=5000)