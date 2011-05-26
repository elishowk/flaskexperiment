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

from flask import abort, make_response, json

import riak
import uuid
from datetime import datetime

class GenericBucket(object):
    def __init__(self, bucketname, port=8087):
        """
        initiate a riak bucket
        """
        self.bucketname = bucketname
        self._connect(bucketname, port)

    def _connect(self, bucketname, port=8087):
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
        """
        add links to an object given a list of identifiers
        """
        for linked_key in links:
            linked_object = self.bucket.get(linked_key)
            object.add_link(linked_object)
            linked_object.add_link(object)

    def _genUUID(self):
        return "%s:::%s"%(datetime.utcnow().isoformat(), uuid.uuid4())

    def create(self, data, links=[]):
        """
        Supply a key to store data under
        The 'data' can be any data Python's 'json' encoder can handle (except unicode values with protobuf)
        Returns the json object created
        """
        if not self.client.is_alive():
            abort(500, "database is dead")
        try:
            if 'id_txt' not in data:
                data['id_txt'] = self._genUUID()
            encodeddata = self._encode(data)
            new_object = self.bucket.new(encodeddata['id_txt'], data=encodeddata)
            # eventually links to other objects
            self._add_links(new_object, links)
            # Save the object to Riak.
            return new_object.store().get_data()
            #return new_object.get_key()
        except Exception, exc:
            abort(500, {"error": "%s"%exc})
            #return make_response((json.dumps({"error": "%s"%exc}), 500, None, 'application/json', 'application/json', False))
        
    def read(self, key):
        """
        Returns json object for a given key
        """
        try:
            response = self.bucket.get(key.encode('utf-8', errors='replace')).get_data()
            return response or abort(404, {})
        except Exception, exc:
            abort(500, {"error": "%s"%exc})        
        
    def update(self, key, update_data, links=[]):
        """
        Gets an updates an item for database
        Returns the updated json object
        """
        try:
            update_object = self.bucket.get(key)
            if not update_object:
                abort(404, "object not found in database")
            old_data = update_object.get_data()
            data = old_data.update(update_data)
            update_object.set_data(self._encode(data))
            # eventually links to other objects
            self._add_links(update_object, links)
            #update_object.store()
            return update_object.get_data() or abort(500, {})
        except Exception, exc:
            abort(500, {"error": "%s"%exc})

    def delete(self, key):
        """
        Deletes a record
        """
        try:
            response = self.bucket.get(key).get_data()
            if not response:
                abort(404, {})
            else:
                response.delete()
        except Exception, exc:
            abort(500, {"error": "%s"%exc})
        
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