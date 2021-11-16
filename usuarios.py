from sqlalchemy import Column, VARCHAR, Integer, Table, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

usuarios_atividades_association = Table(
    'usuarios_atividades', Base.metadata,
    Column('usuarios_id', Integer, ForeignKey('usuarios.id')),
    Column('atividades_id', Integer, ForeignKey('usuarios.id'))
)


class usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    login = Column(VARCHAR)
    senha = Column(VARCHAR)
    atividades = relationship("atividades", secondary=usuarios_atividades_association)

    def __init__(self, login, senha):
        self.login = login
        self.senha = senha