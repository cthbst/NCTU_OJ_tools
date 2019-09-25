import requests
import json
import sys

from config import *

def add():
    parm={
        'problem_id': (None, pid),
        'sample': (None, 'false'),
        'time_limit': (None, '1000'),
        'memory_limit': (None, '262144'),
        'output_limit': (None, '262144'),
        'score': (None, '100')
    }
    rsp=s.post('https://api.oj.nctu.me/testdata/', files=parm, cookies=COOKIES)
    return json.loads(rsp.content)['msg']['id']

def upload(tid, inp, out, tim, mem, sample):
    parm={
        'problem_id': (None, pid),
        'sample': (None, str(sample)),
        'time_limit': (None, tim),
        'memory_limit': (None, mem),
        'output_limit': (None, '262144'),
        'score': (None, '100'),
        'input': open(inp),
        'output': open(out)
    }
    rsp=s.put('https://api.oj.nctu.me/testdata/{}/'.format(tid), files=parm, cookies=COOKIES)
    print(json.loads(rsp.content)['msg'])

def main():
    if len(sys.argv) < 4:
        print('argv need : <pid> <input_filename> <output-filename>')
        exit(0)

    print(*sys.argv)

    pid = sys.argv[1]

    with requests.session() as s:
        tim=str(1000)#time limit(ms)
        mem=str(512*1024)#memory limit(KiB)

        inp = sys.argv[2]
        out = sys.argv[3]

        try:
            open(inp)
            open(out)
        except FileNotFoundError:
            exit(0)
        print('uploading', inp, out)
        tid=add()
        upload(tid, inp, out, tim, mem, False)

if __name__ == '__main__':
    main()
