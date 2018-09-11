#!/usr/bin/env python
# coding = utf-8

import pymysql
from django.db import connection
from ant import instance,tools,controller,sql

import sys

def fixed_sql_exec(v_sql):
    with connection.cursor() as cursor:
        cursor.execute(v_sql)
        row = cursor.fetchone()
    return row

db = 'information_schema'
db_server = {}

schema = {}
top10 = {}
notInnodb = {}

schema_list = []
top10_list = []
notInnodb_list = []

for list in instance.dblist:
    result = {}

    # config of DB
    ip = list['ip']
    port = list['port']
    user = list['user']
    passwd = list['password']

    # fetch sql
    schema_stat = sql.schema_stat
    top10_stat = sql.top10_stat
    notInnodb_stat = sql.notInnodb_stat

    # query
    try:
        con = pymysql.connect(host=ip,
                              user=user,
                              passwd=passwd,
                              db=db,
                              port=3306)
    except:
        print
        "Error!"
        continue

    cur1 = con.cursor()
    cur2 = con.cursor()
    cur3 = con.cursor()
    schema_res = cur1.execute(schema_stat)
    top10_res = cur2.execute(top10_stat)
    notInnodb_res = cur3.execute(notInnodb_stat)
    data1 = cur1.fetchall()
    data2 = cur2.fetchall()
    data3 = cur3.fetchall()
    con.commit()
    cur1.close()
    cur2.close()
    cur3.close()
    con.close()

    # analysis
    s_res = tools.fetchResult(schema_res)
    t_res = tools.fetchResult(top10_res)
    n_res = tools.fetchResult(notInnodb_res)

    # assemble data
    schema[ip] = tools.assembleResult('schema', s_res)
    top10[ip] = tools.assembleResult('top10', t_res)
    notInnodb[ip] = tools.assembleResult('notInnodb', n_res)

sorted_top10 = tools.sortTop10(top10)
db_server = {'schema': schema, 'top10': sorted_top10, 'notInnodb': notInnodb}

# send mail
content = controller.template_data(db_server)

