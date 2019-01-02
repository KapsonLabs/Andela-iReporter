from flask import Flask
import logging
from logging.handlers import SMTPHandler

# create an instance of Flask
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

from app.routes.urls import api_rules

#production mode error messaging 
mail_handler = SMTPHandler(
    mailhost='127.0.0.1',
    fromaddr='server-error@example.com',
    toaddrs=['kapsonkatongole@gmail.com'],
    subject='Application Error'
)
mail_handler.setLevel(logging.ERROR)
mail_handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
))

if not app.debug:
    app.logger.addHandler(mail_handler)