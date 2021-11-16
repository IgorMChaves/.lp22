from sqlalchemy import Column, Table, Integer, ForeignKey, VARCHAR
from sqlalchemy.orm import relationship

from base import Base

comentarios_atividades_association = Table(
    'comentarios_atividades', Base.metadata,
    Column('comentarios_id', Integer, ForeignKey('comentarios.id')),
    Column('atividades_id', Integer, ForeignKey('atividades.id'))
)

class curtidas (Base):
    __tablename__ = 'comentarios'

    id = Column(Integer, primary_key=True)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'))
    usuarios = relationship("usuarios", backref="comentarios")
    comentario = VARCHAR

    def __init__(self, usuarios, comentario):
        self.usuarios = usuarios
        self.comentario = comentario