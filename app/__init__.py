from flask import Flask
from flask_caching import Cache

from config import Config

app = Flask(__name__)
app.config.from_object(Config())
cache = Cache(app, config={ "CACHE_TYPE": "SimpleCache" })

from app import routes
