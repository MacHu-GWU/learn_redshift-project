# -*- coding: utf-8 -*-

"""
psql -h analytics-dev.caddas6ru6aa.us-west-2.redshift.amazonaws.com -p 5439 -d dev -U awsuser --password;
"""

from sqlalchemy_mate import engine_creator
from .config import Config

engine = engine_creator.create_postgresql_psycopg2(
    username=Config.username,
    password=Config.password,
    host=Config.host,
    port=Config.port,
    database=Config.database,
)




