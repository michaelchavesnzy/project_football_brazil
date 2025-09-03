from sqlalchemy import Column, Integer, String, DateTime, Float
from database.connection import Base

class Standings(Base):

    __tablename__ = "tb_classificacao"

    id_time = Column("id_time", Integer, primary_key=True)
    posicao = Column("posicao", Integer)
    nome_time = Column("nome_time", String)
    pontos = Column("pontos", Integer)
    PJ = Column("PJ", Integer)
    VIT = Column("VIT", Integer)
    E = Column("E", Integer)
    DER = Column("DER", Integer)
    GM = Column("GM", Integer)
    GC = Column("GC", Integer)
    SG = Column("SG", Integer)
    link_escudo = Column("link_escudo", String)




