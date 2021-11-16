from datetime import time
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy import Column, String, Integer, Date
from sqlalchemy.sql.sqltypes import VARCHAR, Date, time, int

from base import Base


class atividades(Base):
    __tablename__ = 'atividades'

    id = Column(Integer, primary_key=True)
    tipo = Column(VARCHAR)
    dia = Column(Date)
    start = Column(time)
    end = Column(time)
    KMs_percorridos = Column(int)
    local = Column(VARCHAR)

    def __init__(self, tipo, dia, start, end, KMs_percorridos, local):
        self.tipo = tipo
        self.dia = dia
        self.start = start
        self.end = end
        self.KMs_percorridos = KMs_percorridos
        self.local = local