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

from commonecouteserver.data import Track, Event, User, Post, Product, Genre, Artist

from flask import Flask, abort, jsonify, json
coeserver = Flask(__name__)

import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=logging.DEBUG)

coebuckets={
    'track': Track(),
    'event': Event(),
    'user': User(),
    'post': Post(),
    'product': Product(),
    'genre': Genre(),
    'artist': Artist()
}

def _request_body(request):
    return request.json

@coeserver.after_request
def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return jsonify(response)
    
#@coeserver.before_request
#def before_request():
#    response.headers['Access-Control-Allow-Origin'] = '*'
    
# default handler
@coeserver.route('/*', methods=['GET','POST','PUT','DELETE'])
def default():
    return {}
    
# GET handlers
@coeserver.route('/track/<id>/', methods=['GET'])
def get_track(id):
    return coebuckets['track'].read(id)
    
@coeserver.route('/event/<id>/', methods=['GET'])
def get_event(id):
    return coebuckets['event'].read(id)
    
@coeserver.route('/user/<id>/', methods=['GET'])
def get_user(id):
    return coebuckets['user'].read(id)
    
@coeserver.route('/post/<id>/', methods=['GET'])
def get_post(id):
    return coebuckets['post'].read(id)

@coeserver.route('/genre/<id>/', methods=['GET'])
def get_genre(id):
    return coebuckets['genre'].read(id)
    
@coeserver.route('/product/<id>/', methods=['GET'])
def get_product(id):
    return coebuckets['product'].read(id)
 
@coeserver.route('/artist/<id>/', methods=['GET'])
def get_artist(id):
    return coebuckets['artist'].read(id)
   
# POST handlers
@coeserver.route('/track/', methods=['POST'])
def post_track():
    coebuckets['track'].create(_request_body(request))
    
@coeserver.route('/event/', methods=['POST'])
def post_event():
    coebuckets['event'].create(_request_body(request))
    
@coeserver.route('/user/', methods=['POST'])
def post_user():
    coebuckets['user'].create(_request_body(request))
    
@coeserver.route('/post/', methods=['POST'])
def post_post():
    coebuckets['post'].create(_request_body(request))

@coeserver.route('/genre/', methods=['POST'])
def post_genre():
    coebuckets['genre'].create(_request_body(request))
    
@coeserver.route('/product/', methods=['POST'])
def post_product():
    coebuckets['product'].create(_request_body(request))
    
@coeserver.route('/artist/', methods=['POST'])
def post_artist():
    return coebuckets['artist'].create(_request_body(request))
    
# PUT handlers
@coeserver.route('/track/<id>/', methods=['PUT'])
def put_track(id):
    return coebuckets['track'].update(id, _request_body(request))
    
@coeserver.route('/event/<id>/', methods=['PUT'])
def put_event(id):
    return coebuckets['event'].update(id, _request_body(request))
    
@coeserver.route('/user/<id>/', methods=['PUT'])
def put_user(id):
    return coebuckets['user'].update(id, _request_body(request))
    
@coeserver.route('/post/<id>/', methods=['PUT'])
def put_post(id):
    return coebuckets['post'].update(id, _request_body(request))

@coeserver.route('/genre/<id>/', methods=['PUT'])
def put_genre(id):
    return coebuckets['genre'].update(id, _request_body(request))
    
@coeserver.route('/product/<id>/', methods=['PUT'])
def put_product(id):
    return coebuckets['product'].update(id, _request_body(request))

@coeserver.route('/artist/<id>/', methods=['PUT'])
def put_artist(id):
    return coebuckets['artist'].update(id, _request_body(request))
  
# DELETE HANDLERS
@coeserver.route('/track/<id>/', methods=['DELETE'])
def delete_track(id):
    coebuckets['track'].delete(id)
    
@coeserver.route('/event/<id>/', methods=['DELETE'])
def delete_event(id):
    coebuckets['event'].delete(id)
    
@coeserver.route('/user/<id>/', methods=['DELETE'])
def delete_user(id):
    coebuckets['user'].delete(id)
    
@coeserver.route('/post/<id>/', methods=['DELETE'])
def delete_post(id):
    coebuckets['post'].delete(id)

@coeserver.route('/genre/<id>/', methods=['DELETE'])
def delete_genre(id):
    coebuckets['genre'].delete(id)
    
@coeserver.route('/product/<id>/', methods=['DELETE'])
def delete_product(id):
    coebuckets['product'].delete(id)  

@coeserver.route('/artist/<id>/', methods=['DELETE'])
def delete_artist(id):
    coebuckets['artist'].delete(id)
