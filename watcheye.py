"""
Main module of the server file
"""
import connexion
import logging
from logging.handlers import RotatingFileHandler
from flask import render_template, request

app = connexion.App(__name__, specification_dir="./")

app.add_api("swagger.yml")

@app.route("/")
def home():
    app.app.logger.warning('%s A warning occurred (%d apples)', request.remote_addr, 42)
    app.app.logger.error('An error occurred')
    app.app.logger.info('%'request.remote_addr)
    return render_template("home.html")

if __name__ == '__main__':
    handler = RotatingFileHandler('logs/log.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.app.logger.addHandler(handler)
    app.run(debug=True)
