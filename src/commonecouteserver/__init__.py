# -*- coding: utf-8 -*-
# Copyright (c) 2011 CommOnEcoute http://commonecoute.com
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/agpl.html>

from commonecouteserver.data import Concert, Event, User, Post, Product, Genre

import bottle
bottle.DEBUG = True
from bottle import request, response
from bottle.ext import werkzeug
import json

coeserver = bottle.Bottle()
werkzplugin = werkzeug.Plugin()
werkzplugin.evalex = True

coeserver.install(werkzplugin)

#werkzeugreq = werkzplugin.request # For the lazy.

coebuckets={
    'concert': Concert(),
    'event': Event(),
    'user': User(),
    'post': Post(),
    'product': Product(),
    'genre': Genre()
}

def _request_body(request):
    data = request.body.readline()
    print data
    if not data:
        abort(400, 'No data received')
    return json.loads(data)

# GET handlers
@coeserver.get('/concert/:id/')
def get_concert(id):
    return coebuckets['concert'].read(id)
    
@coeserver.get('/event/:id/')
def get_event(id):
    return coebuckets['event'].read(id)
    
@coeserver.get('/user/:id/')
def get_user(id):
    return coebuckets['user'].read(id)
    
@coeserver.get('/post/:id/')
def get_post(id):
    return coebuckets['post'].read(id)

@coeserver.get('/genre/:id/')
def get_genre(id):
    return coebuckets['genre'].read(id)
    
@coeserver.get('/product/:id/')
def get_product(id):
    return coebuckets['product'].read(id)
    
# POST handlers
@coeserver.post('/concert/')
def post_concert():
    coebuckets['concert'].create(_request_body(request))
    
@coeserver.post('/event/')
def post_event():
    coebuckets['event'].create(_request_body(request))
    
@coeserver.post('/user/')
def post_user():
    coebuckets['user'].create(_request_body(request))
    
@coeserver.post('/post/')
def post_post():
    coebuckets['post'].create(_request_body(request))

@coeserver.post('/genre/')
def post_genre():
    coebuckets['genre'].create(_request_body(request))
    
@coeserver.post('/product/')
def post_product():
    coebuckets['product'].create(_request_body(request))
    
# PUT handlers
@coeserver.put('/concert/:id/')
def put_concert(id):
    return coebuckets['concert'].update(id, _request_body(request))
    
@coeserver.put('/event/:id/')
def put_event(id):
    return coebuckets['event'].update(id, _request_body(request))
    
@coeserver.put('/user/:id/')
def put_user(id):
    return coebuckets['user'].update(id, _request_body(request))
    
@coeserver.put('/post/:id/')
def put_post(id):
    return coebuckets['post'].update(id, _request_body(request))

@coeserver.put('/genre/:id/')
def put_genre(id):
    return coebuckets['genre'].update(id, _request_body(request))
    
@coeserver.put('/product/:id/')
def put_product(id):
    return coebuckets['product'].update(id, _request_body(request))
    
# DELETE handlers
@coeserver.delete('/concert/:id/')
def delete_concert(id):
    coebuckets['concert'].delete(id)
    
@coeserver.delete('/event/:id/')
def delete_event(id):
    coebuckets['event'].delete(id)
    
@coeserver.delete('/user/:id/')
def delete_user(id):
    coebuckets['user'].delete(id)
    
@coeserver.delete('/post/:id/')
def delete_post(id):
    coebuckets['post'].delete(id)

@coeserver.delete('/genre/:id/')
def delete_genre(id):
    coebuckets['genre'].delete(id)
    
@coeserver.delete('/product/:id/')
def delete_product(id):
    coebuckets['product'].delete(id)  
 
def runserver(*args, **kwargs):
    bottle.run(coeserver, host='localhost', port=8080)