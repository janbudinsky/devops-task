# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/hello/<name>")
def say_hello(name):
    return f"Hello <b>{name}</b>"


@app.route("/metrics/cpu")
def metrics_cpu():
    pass


@app.route("/metrics/ram")
def metrics_ram():
    pass


@app.route("/metrics/disk")
def metrics_disk():
    pass


@app.route("/metrics/network")
def metrics_network():
    pass


@app.route("/metrics/services")
def metrics_services():
    pass


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
