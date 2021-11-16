from sqlalchemy import Column, Table, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base import Base

curtidas_comentarios_comentarios_association = Table(
    'curtidas_comentarios_comentarios', Base.metadata,
    Column('curtidas_comentarios_id', Integer, ForeignKey('curtidas_comentarios.id')),
    Column('comentarios_id', Integer, ForeignKey('comentarios.id'))
)

class curtidas (Base):
    __tablename__ = 'curtidas_comentarios'

    id = Column(Integer, primary_key=True)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship("usuarios", backref="curtidas_comentarios")

    def __init__(self, usuarios):
        self.usuarios = usuarios