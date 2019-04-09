# -*- coding: utf-8 -*-

from pathlib_mate import PathCls as Path
from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

db_yml_path = Path(Path.home(), ".db.yml")
data = load(db_yml_path.read_bytes(), Loader=Loader)
identifier = "redshift-dev"


class Config(object):
    host = data[identifier]["host"]
    port = data[identifier]["port"]
    database = data[identifier]["database"]
    username = data[identifier]["username"]
    password = data[identifier]["password"]
