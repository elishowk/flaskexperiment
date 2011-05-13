
from bottle import Bottle
coes = Bottle()

@coes.get('/song')
def song():
    return "Hello World!"

