from django.db import models, connection
from ant import  sql

# Create your models here.

def fixed_sql_exec(v_sql):
    with connection.cursor() as cursor:
        cursor.execute(v_sql)
        row = cursor.fetchone()
    return row



