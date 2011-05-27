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
from commonecouteserver import logger

from flask import Flask, request, jsonify
#from flaskext.jsonify import jsonify
coeserver = Flask(__name__)
logger.setlogger(coeserver)

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
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Headers'] = 'content-type'
    return response
    
@coeserver.before_request
def before_request():
    """
    checks each bucket 
    """
    for bucketname, bucketinstance in coebuckets.iteritems():
        if not bucketinstance.client.is_alive():
            try:
                bucketinstance._connect(bucketname)
            except Exception, exc:
                abort(500, "%s"%exc)
    
# default handler
#@coeserver.route('/*', methods=['GET','POST','PUT','DELETE'])
#def default():
#    return {}

@coeserver.route('/*', methods=['OPTIONS'])
def options_handler():
    return jsonify(None)
    
@coeserver.errorhandler(404)
def not_found(error):
    return u"circulez, rien à voir", 404

### GET bucket keys
@coeserver.route('/track/', methods=['GET'])
def get_keys_track():
    return jsonify(coebuckets['track'].keys())
    
@coeserver.route('/event/', methods=['GET'])
def get_keys_event():
    return jsonify(coebuckets['event'].keys())
    
@coeserver.route('/user/', methods=['GET'])
def get_keys_user():
    return jsonify(coebuckets['user'].keys())
    
@coeserver.route('/post/', methods=['GET'])
def get_keys_post():
    res=coebuckets['post'].keys()
    coeserver.logger.debug(res)
    return jsonify(coebuckets['post'].keys())

@coeserver.route('/genre/', methods=['GET'])
def get_keys_genre():
    return jsonify(coebuckets['genre'].keys())
    
@coeserver.route('/product/', methods=['GET'])
def get_keys_product(id):
    return jsonify(coebuckets['product'].keys())
 
@coeserver.route('/artist/', methods=['GET'])
def get_keys_artist(id):
    return jsonify(coebuckets['artist'].keys())

### GET records handlers
@coeserver.route('/track/<id>/', methods=['GET'])
def get_track(id):
    return jsonify(coebuckets['track'].read(id))
    
@coeserver.route('/event/<id>/', methods=['GET'])
def get_event(id):
    return jsonify(coebuckets['event'].read(id))
    
@coeserver.route('/user/<id>/', methods=['GET'])
def get_user(id):
    return jsonify(coebuckets['user'].read(id))
    
@coeserver.route('/post/<id>/', methods=['GET'])
def get_post(id):
    return jsonify(coebuckets['post'].read(id))

@coeserver.route('/genre/<id>/', methods=['GET'])
def get_genre(id):
    return jsonify(coebuckets['genre'].read(id))
    
@coeserver.route('/product/<id>/', methods=['GET'])
def get_product(id):
    return jsonify(coebuckets['product'].read(id))
 
@coeserver.route('/artist/<id>/', methods=['GET'])
def get_artist(id):
    return jsonify(coebuckets['artist'].read(id))
   
# POST handlers
@coeserver.route('/track/', methods=['POST'])
def post_track():
    return jsonify(coebuckets['track'].create(_request_body(request)))
    
@coeserver.route('/event/', methods=['POST'])
def post_event():
    return jsonify(coebuckets['event'].create(_request_body(request)))
    
@coeserver.route('/user/', methods=['POST'])
def post_user():
    return jsonify(coebuckets['user'].create(_request_body(request)))
    
@coeserver.route('/post/', methods=['POST'])
def post_post():
    return jsonify(coebuckets['post'].create(_request_body(request)))

@coeserver.route('/genre/', methods=['POST'])
def post_genre():
    return jsonify(coebuckets['genre'].create(_request_body(request)))
    
@coeserver.route('/product/', methods=['POST'])
def post_product():
    return jsonify(coebuckets['product'].create(_request_body(request)))
    
@coeserver.route('/artist/', methods=['POST'])
def post_artist():
    return jsonify(coebuckets['artist'].create(_request_body(request)))
    
# PUT handlers
@coeserver.route('/track/<id>/', methods=['PUT'])
def put_track(id):
    return jsonify(coebuckets['track'].update(id, _request_body(request)))
    
@coeserver.route('/event/<id>/', methods=['PUT'])
def put_event(id):
    return jsonify(coebuckets['event'].update(id, _request_body(request)))
    
@coeserver.route('/user/<id>/', methods=['PUT'])
def put_user(id):
    return jsonify(coebuckets['user'].update(id, _request_body(request)))
    
@coeserver.route('/post/<id>/', methods=['PUT'])
def put_post(id):
    return jsonify(coebuckets['post'].update(id, _request_body(request)))

@coeserver.route('/genre/<id>/', methods=['PUT'])
def put_genre(id):
    return jsonify(coebuckets['genre'].update(id, _request_body(request)))
    
@coeserver.route('/product/<id>/', methods=['PUT'])
def put_product(id):
    return jsonify(coebuckets['product'].update(id, _request_body(request)))

@coeserver.route('/artist/<id>/', methods=['PUT'])
def put_artist(id):
    return jsonify(coebuckets['artist'].update(id, _request_body(request)))
  
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
    