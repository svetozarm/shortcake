import os

base_dir = os.path.abspath(os.path.dirname(__file__))
sqlite_db_file = os.path.join(base_dir, "app.db")


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "not-really-secret"
    SQLALCHEMY_DATABASE_URI = (
        os.environ.get("DATABASE_URI") or f"sqlite:///{sqlite_db_file}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
