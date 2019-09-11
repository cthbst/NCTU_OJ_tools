import requests
import sys

from config import *

def rm_problem(tid):
    parm={
        'problemId': tid
    }
    rsp = requests.session().delete('https://api.oj.nctu.me/problems/'+str(tid)+'/', data=parm, cookies=COOKIES)
    print( tid, rsp )

if len(sys.argv) >= 2:
    rm_problem(int(sys.argv[1]))
