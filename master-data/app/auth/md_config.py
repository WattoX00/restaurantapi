import os

SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-dev-key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
