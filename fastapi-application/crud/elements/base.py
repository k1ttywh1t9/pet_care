from sqlalchemy.orm import DeclarativeBase


class ServiceBase:
    def __init__(self, model):
        self.model: DeclarativeBase = model
