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

from flask import abort, jsonify
import riak
import uuid
import datetime

class GenericBucket(object):
    def __init__(self, bucketname, port=8087):
        """
        Connects to a particular bucket
        on the defaut port of riak protobuf interface
        """
        self.client = riak.RiakClient(port=port, transport_class=riak.RiakPbcTransport)
        #self.client.set_r(1)
        #self.client.set_w(1)
        self.bucket = self.client.bucket(bucketname)

    def _encode(self, data):
        """
        on the fly encoding
        """
        encodeddata = {}
        for (key, value) in data.iteritems():
            if isinstance(value, unicode):
                encodeddata[key] = value.encode('utf-8', errors='replace')
            else:
                encodeddata[key] = value
        return encodeddata

    def _add_links(self, object, links):
        for linked_key in links:
            linked_object = self.bucket.get(linked_key)
            object.add_link(linked_object)
            linked_object.add_link(object)

    def create(self, data, links=[]):
        """
        Supply a key to store data under
        The 'data' can be any data Python's 'json' encoder can handle
        Except unicode values with protobuf
        """
        if not self.client.is_alive():
            abort(501, "database is dead")
        try:
            if 'id_txt' not in data:
                data['id_txt'] = "%s"%uuid.uuid4()
            encodeddata = self._encode(data)
            new_object = self.bucket.new(encodeddata['id_txt'], data=encodeddata)
            # eventually links to other objects
            self._add_links(new_object, links)
            # Save the object to Riak.
            new_object.store()
        except Exception, exc:
            abort(501, "error occured during data creation : %s"%exc)
        
    def read(self, key):
        response = self.bucket.get(key.encode('utf-8', errors='replace')).get_data()
        if response is None:
            abort(404, "object not found in database")
        else:
            return jsonify(response)
        
    def update(self, key, update_data, links=[]):
        """
        Gets an updates an item for database
        """
        try:
            update_object = self.bucket.get(key)
            if update_object is None:
                abort(404, "object not found in database")
            old_data = update_object.get_data()
            data = old_data.update(update_data)
            update_object.set_data(self._encode(data))
            # eventually links to other objects
            self._add_links(update_object, links)
            #update_object.store()
            return jsonify(update_object.get_data())
        except Exception, exc:
            abort(501, "error occured during data update : %s"%exc)

    def delete(self, key):
        try:
            response = self.bucket.get(key).get_data()
            if response is None:
                abort(404, "object not found in database")
            else:
                response.delete()
        except Exception, exc:
            abort(501, "error occured during data deletion : %s"%exc)
        
class Track(GenericBucket):
    def __init__(self, *args, **kwargs):
        GenericBucket.__init__(self, "track", *args, **kwargs)
        
class Event(GenericBucket):
    def __init__(self, *args, **kwargs):
        GenericBucket.__init__(self, "event", *args, **kwargs)

class User(GenericBucket):
    def __init__(self, *args, **kwargs):
        GenericBucket.__init__(self, "user", *args, **kwargs)
        
class Post(GenericBucket):
    def __init__(self, *args, **kwargs):
        GenericBucket.__init__(self, "post", *args, **kwargs)
 
class Product(GenericBucket):
    def __init__(self, *args, **kwargs):
        GenericBucket.__init__(self, "product", *args, **kwargs)
 
class Genre(GenericBucket):
    def __init__(self, *args, **kwargs):
        GenericBucket.__init__(self, "genre", *args, **kwargs)

class Artist(GenericBucket):
    def __init__(self, *args, **kwargs):
        GenericBucket.__init__(self, "artist", *args, **kwargs)