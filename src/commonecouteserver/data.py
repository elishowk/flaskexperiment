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

import riak

class GenericBucket(object):
    def __init__(self, bucketname, port=8070):
        """
        Connects to a particular bucket
        on the defaut port of riak protobuf interface
        """
        self.client = riak.RiakClient(port=port, transport_class=riak.RiakPbcTransport)
        self.bucket = client.bucket(bucketname)

    def _add_links(self, object, links):
        for linked_key in links:
            linked_object = self.bucket.get(linked_key)
            object.add_link(linked_object)
            linked_object.add_link(object)

    def create(self, key, data, links=[]):
        """
        Supply a key to store data under
        The 'data' can be any data Python's 'json' encoder can handle.
        """
        new_object = self.bucket.new(key, data=data)
        # eventually links to other objects
        self._add_links(new_object, links)
        # Save the object to Riak.
        new_object.store()
        
    def read(self, key):
        return self.bucket.get(key).get_data()
        
    def update(self, key, update_data, links=[]):
        update_object = self.bucket.get(key)
        old_data = update_object.get_data()
        data = old_data.update(update_data)
        update_object.set_data(data)
        self._add_links(update_object, links)
        #update_object.store()
        
    def delete(self, key):
        self.read(key).delete()
        
class Concert(GenericBucket):
    def __init__(self, *args, **kwargs):
        GenericBucket.__init__(self, "concert", *args, **kwargs)
        
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
 