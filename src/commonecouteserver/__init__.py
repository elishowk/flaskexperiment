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
bottle.debug(True)

coeserver = bottle.Bottle()

coebuckets={
    'concert': Concert(),
    'event': Event(),
    'user': User(),
    'post': Post(),
    'product': Product(),
    'genre': Genre()
}

# GET handlers
@coeserver.get('/concert/:id')
def get_concert(id):
    return coebuckets['concert'].read(id)
    
@coeserver.get('/event/:id')
def get_event(id):
    return coebuckets['event'].read(id)
    
@coeserver.get('/user/:id')
def get_user(id):
    return coebuckets['user'].read(id)
    
@coeserver.get('/post/:id')
def get_post(id):
    return coebuckets['post'].read(id)

@coeserver.get('/genre/:id')
def get_genre(id):
    return coebuckets['genre'].read(id)
    
@coeserver.get('/product/:id')
def get_product(id):
    return coebuckets['product'].read(id)
    
# POST handlers
@coeserver.post('/concert/')
def post_concert():
    return coebuckets['concert'].create(request.forms.dict)
    
@coeserver.post('/event/')
def post_event():
    return coebuckets['event'].create(request.forms.dict)
    
@coeserver.post('/user/')
def post_user():
    return coebuckets['user'].create(request.forms.dict)
    
@coeserver.post('/post/')
def post_post():
    return coebuckets['post'].create(request.forms.dict)

@coeserver.post('/genre/')
def post_genre():
    return coebuckets['genre'].create(request.forms.dict)
    
@coeserver.post('/product/')
def post_product():
    return coebuckets['product'].create(request.forms.dict)
    
# PUT handlers
@coeserver.put('/concert/:id')
def put_concert():
    return coebuckets['concert'].update(id)
    
@coeserver.put('/event/:id')
def put_event():
    return coebuckets['event'].update(id)
    
@coeserver.put('/user/:id')
def put_user():
    return coebuckets['user'].update(id, request.forms.dict)
    
@coeserver.put('/post/:id')
def put_post(id):
    return coebuckets['post'].update(id, request.forms.dict)

@coeserver.put('/genre/:id')
def put_genre(id):
    return coebuckets['genre'].update(id, request.forms.dict)
    
@coeserver.put('/product/:id')
def put_product(id):
    return coebuckets['product'].update(id, request.forms.dict)
    
# DELETE handlers
@coeserver.delete('/concert/:id')
def delete_concert(id):
    return coebuckets['concert'].delete(id)
    
@coeserver.delete('/event/:id')
def delete_event(id):
    return coebuckets['event'].delete(id)
    
@coeserver.delete('/user/:id')
def delete_user(id):
    return coebuckets['user'].delete(id)
    
@coeserver.delete('/post/:id')
def delete_post(id):
    return coebuckets['post'].delete(id)

@coeserver.delete('/genre/:id')
def delete_genre(id):
    return coebuckets['genre'].delete(id)
    
@coeserver.delete('/product/:id')
def delete_product(id):
    return coebuckets['product'].delete(id)  
 
def runserver(*args, **kwargs):
    bottle.run(coeserver, host='localhost', port=8080)