#!/usr/bin/env python3
import cgi
import json
from pathlib import Path

from typing import Dict

_PROJECT_PATH = Path('cgi-bin')
_TEMPLATES_PATH = _PROJECT_PATH / 'templates'

_TEMPLATES = {'response': _TEMPLATES_PATH / "Response.html",
              'bad_request': _TEMPLATES_PATH / "BadRequest.html"}

_DATABASES = {'posts': _PROJECT_PATH / 'posts.json'}


class Printer:
    __STYLES = {'response': _TEMPLATES_PATH / 'main-style.css'}

    @staticmethod
    def print_response():
        pass

    @staticmethod
    def get_style(element: str) -> str:
        return Printer.__load_style(element)

    @staticmethod
    def __load_style(key: str) -> str:
        with open(Printer.__STYLES[key], 'r') as f:
            return f.read()


class DB:
    pass


def print_response(path_to_template: Path, params: Dict[str, str]):
    print("Content-type: text/html\n")
    with open(str(path_to_template), 'r', encoding='utf-8') as t:
        print(t.read().format(**params))


def process_request(key: str):
    with open(_DATABASES['posts'], 'r', encoding='utf-8') as db:
        posts = json.load(db)
        for post in posts:
            if key == post['title']:
                return post['text']
        return None


form = cgi.FieldStorage()
req = form.getvalue("input_key")
result = process_request(req)
if result is not None:
    p = {'title': req, 'data': result, 'style': Printer.get_style('response')}
    print_response(_TEMPLATES['response'], p)
else:
    print_response(_TEMPLATES['bad_request'], {'title': 'Статья не найдена', 'request': req})
