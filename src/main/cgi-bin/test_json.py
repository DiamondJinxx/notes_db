import json
from pathlib import Path

with open('posts.json', 'r') as posts:
    print(json.load(posts)[0]['tittle'])

_PROJECT_PATH = Path('cgi-bin')
_TEMPLATES_PATH = _PROJECT_PATH / 'templates'

_TEMPLATES = {'response':_TEMPLATES_PATH / "Respons.html",
              'bad_request': _TEMPLATES_PATH / "BadRequest.html"}


print(str(_TEMPLATES['response']))