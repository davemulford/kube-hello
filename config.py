# A configuration class for the application

import os

class Config:
    BASE_URL = os.environ.get("BASE_URL")
    AUTH_TOKEN = os.environ.get("AUTH_TOKEN")
    MESSAGE = os.environ.get("MESSAGE") or "Hello from Kubernetes!"