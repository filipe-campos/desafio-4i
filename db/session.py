from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)

try:
    conn = engine.connect()
    conn.execute("create database 'desafio-4i';")

    create_user_query = f'CREATE TABLE IF NOT EXISTS "user" \
                            ( \
                             "id"              serial NOT NULL, \
                             cpf             varchar(11) NOT NULL, \
                             hashed_password text NOT NULL, \
                             full_name       varchar(200) NOT NULL, \
                             birthday        date NULL, \
                             cep             varchar(8) NULL, \
                             street          varchar(200) NULL, \
                             neighborhood    varchar(200) NULL, \
                             city            varchar(200) NULL, \
                             "state"           varchar(50) NULL, \
                             CONSTRAINT PK_user PRIMARY KEY ( "id" ) \
                            );'

    conn.execute(create_user_query)
except Exception as e:
    print('Erro ao criar banco de dados')
    print(e)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
