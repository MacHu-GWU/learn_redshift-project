# -*- coding: utf-8 -*-

from chalice import Chalice
from learn_redshift.lbd import hello

app = Chalice(app_name="learn_redshift")


@app.lambda_function(name="hello")
def handler_hello(event, context):
    return hello.high_level_api(event, context)
