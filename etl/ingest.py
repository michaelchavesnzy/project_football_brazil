from api.football import FootballApi
from config.settings import DATABASE_URL
from etl import transform
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from database.connection import Base
from database.models import Standings

def run_ingest():

    api = FootballApi()
    json_classificacao = api.get_standings()
    df_classificacao = transform.transform_standings(json_classificacao)

    engine = create_engine(DATABASE_URL, echo=True)
    Session = sessionmaker(bind=engine)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    objects = []
    for _, row in df_classificacao.iterrows():
        s = Standings(
                id_time=row["id_time"],
                posicao=row["posicao"],
                nome_time=row["nome_time"],
                pontos=row["pontos"],
                PJ=row["PJ"],
                VIT=row["VIT"],
                E=row["E"],
                DER=row["DER"],
                GM=row["GM"],
                GC=row["GC"],
                SG=row["SG"],
                link_escudo=row.get("link_escudo")  # caso a coluna venha vazia
            )
        objects.append(s)

    with Session() as session:
        session.add_all(objects)
        session.commit()

    #df_classificacao.to_sql(name='tb_classificacao', con=engine, if_exists='replace', index=False)

    print("ETL completo: tabelas populadas no banco!")









