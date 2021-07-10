from sqlalchemy import Table, Column, Integer, String, MetaData, TIMESTAMP, create_engine
from dynaconf import settings


def create_database_url():
    return f'postgresql://{settings.DB_USER}:' \
           f'{settings.DB_PASSWORD}@{settings.DB_HOST}:' \
           f'{settings.DB_PORT}/{settings.DB_NAME}'


metadata = MetaData()

engine = create_engine(create_database_url())

birthday = Table('birthday', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('fio', String),
                 Column('birthday', TIMESTAMP(timezone=True)),
                 Column('birthday_timezone', String),
                 Column('residence_timezone', String),
                 )

metadata.create_all(engine)
