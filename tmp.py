from sqlalchemy import MetaData, Table, Column
from sqlalchemy import String, Integer, Float, DateTime
from sqlalchemy_mate.crud.inserting import smart_insert
from datetime import datetime
import rolex
from learn_redshift.db import engine
from learn_redshift.fake_data import create_fake_data

metadata = MetaData()
t_event = Table(
    "events", metadata,
    Column("id", String),
    Column("name", String),
    Column("time", DateTime),
)
try:
    t_event.drop(engine)
except:
    pass
metadata.create_all(engine)

data = create_fake_data()
smart_insert(engine, t_event, data)
