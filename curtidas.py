from sqlalchemy import Column, Table, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

curtidas_atividades_association = Table(
    'curtidas_atividades', Base.metadata,
    Column('curtidas_id', Integer, ForeignKey('curtidas.id')),
    Column('atividades_id', Integer, ForeignKey('atividades.id'))
)

class curtidas (Base):
    __tablename__ = 'curtidas'

    id = Column(Integer, primary_key=True)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship("usuarios", backref="curtidas")

    def __init__(self, usuarios):
        self.usuarios = usuarios