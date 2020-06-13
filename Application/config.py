import os

class Config(object):
	DEBUG = True
	DEVELOPMENT = True
	SECRET_KEY = os.urandom(32)
	FLASK_SECRET = SECRET_KEY

class ProductionConfig(Config):
	DEVELOPMENT = False
	DEBUG = False
