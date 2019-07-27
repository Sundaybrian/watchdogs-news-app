from flask import Flask
from .config import DevConfig

#initializing application
app =Flask(__name__)

#Setting up the configuration
app.config.from_object(DevConfig)


from app import views