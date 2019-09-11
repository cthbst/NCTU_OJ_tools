import requests
import json
import sys

from config import *

def add_execute(pid, name='New Execute /', language_id=1, execute = '{}', filename='main.c'):
    parm={
        'name' : name,
        'problem_id' : pid,
        'language_id' : language_id,
        'execute' : execute,
        'filename' : filename
    }
    url = 'https://api.oj.nctu.me/executes/'
    rsp = requests.session().post(url, data=parm, cookies=COOKIES)
    print( pid, json.loads(rsp.content) )
    return json.loads(rsp.content)['msg']['id']

def add_executes(pid):
    print( add_execute(pid,'C++17',2,executes['cpp17'],'main.cpp') )
    print( add_execute(pid,'C11',1,executes['c11'],'main.c') )
    print( add_execute(pid,'Java',3,executes['java'],'Main.java') )
    print( add_execute(pid,'Python3',5,executes['py3'],'main.py') )
    print( add_execute(pid,'Python2',4,executes['py2'],'main.py') )

def add_problem(title="HWX-X"):
    parm={
        'group_id': config['group_id'],
        'title': title,
        'visible': 0,
        'group_read': 1,
        'group_write': 1,
        'use_pdf': 0,
        'description': '',
        'input': '',
        'output': '',
        'hint': '',
        'source': ''
    }
    rsp = requests.session().post('https://api.oj.nctu.me/problems/', data=parm, cookies=COOKIES)
    print(rsp)
    pid =  json.loads(rsp.content)['msg']['id']
    add_executes(pid)

if len(sys.argv) >= 2:
    add_problem(sys.argv[1])
else:
    add_problem()
