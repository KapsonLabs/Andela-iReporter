from flask import Flask

# create an instance of Flask
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

from app.routes.urls import incident_api
# Routes.fetch_urls(app)