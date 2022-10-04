#!/usr/bin/env python3
import cgi
import json
from pathlib import Path

from typing import Dict

_PROJECT_PATH = Path('cgi-bin')
_TEMPLATES_PATH = _PROJECT_PATH / 'templates'

_TEMPLATES = {'response':_TEMPLATES_PATH / "Response.html",
              'bad_request': _TEMPLATES_PATH / "BadRequest.html"}

_DATABASES = {'posts': _PROJECT_PATH / 'posts.json'}


def print_response(path_to_template: Path, params: Dict[str, str]):
    print("Content-type: text/html\n")
    with open(str(path_to_template), 'r', encoding='utf-8') as t:
        print(t.read().format(**params))


def print_respons(req: str, data: str):
    print("Content-type: text/html\n")
    with open(_TEMPLATES['response']) as resp:
        print(resp.read().format(tittle=req, data=data))


def process_requedst(key: str):
    with open(_DATABASES['posts'], 'r', encoding='utf-8') as db:
        posts = json.load(db)
        for post in posts:
            if key == post['tittle']:
                return post['text']
        return None


form = cgi.FieldStorage()
req = form.getvalue("input_key")
result = process_requedst(req)
if result is not None:
    p = {'tittle': req, 'data': result}
    print_response(_TEMPLATES['response'], p)
else:
    print_response(_TEMPLATES['bad_request'], {'tittle': req})
