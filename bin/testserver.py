# -*- coding: utf-8 -*-
# Copyright (c) 2011 CommOnEcoute
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
    
import commonecouteserver
import unittest
from webtest import TestApp
import webob
import json
from datetime import datetime
import urllib
import uuid

class COEserverTestCase(unittest.TestCase):
    data = {
        'event': {
            'id_txt': "%s"%uuid.uuid4(),
            'url_txt': "http://commonecoute.com/urleventunique.html",
            'title_txt': "Amon Tobin presents ISAM @ Le Bataclan, Paris",
            'location_txt': "Le Bataclan, Paris",
            'image': "http://commonecoute.com/assets/images/track/0125.png",
            'views': 0,
            'overview_txt': "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
            'start_date': str(datetime.utcnow().isoformat()),
            'end_date': str(datetime.now().isoformat()),
            'link_track': ["http://commonecoute.com/urltrackunique.html"]
        },
        'track': {
            'url_txt': "http://commonecoute.com/urltrackunique.html",
            'id_txt': "%s"%uuid.uuid4(),
            'title_txt': "Amon Tobin presents ISAM @ Le Bataclan, Paris",
            'views': 0,
            'video': "http://commonecoute.com/videoembedurl.mkv",
            'image': "http://commonecoute.com/assets/images/track/0125.png",
            'location_txt': "Le Bataclan, Paris",
            'overview_txt': "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
            'link_product': ["http://commonecoute.com/urlproduct1.html", "http://commonecoute.com/urlproduct2.html"],
            'link_user': ["labsynth@gmail.com"],
            'link_track': ["http://commonecoute.com/urltrackunique2.html"],
            'start_date': str(datetime.utcnow().isoformat()),
            'end_date': str(datetime.now().isoformat()),
            'link_artist': ["http://commonecoute.com/urlartistunique.html", "http://commonecoute.com/urlartistunique2.html"],
            'link_genre': ["http://commonecoute.com/urlelectronicunique.html"] 
        },
        'user': {
            'id_txt': 'elishowk@nonutc.fr',
            'firstname_txt':'elias',
            'lastname_txt': 'showk',
            'image': 'http://gravatar.com/elishowk@nonutc.fr',
            'genre': 'M',
            'birthday_date': "1984-07-18",
            'city_txt': "Paris",
            'country_txt': "France",
            'link_user': ["labsynth@gmail.com"],
            'link_genre': ["http://commonecoute.com/urlelectronicunique.html"],
            'link_artist': ["http://commonecoute.com/urlartistunique.html"]
        },
        'product': {
            'id_txt': "%s"%uuid.uuid4(),
            'url_txt': "http://commonecoute.com/urlproduct1.html",
            'title_txt': "ISAM",
            'release_date': "2011-03-28",
            'overview_txt': "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum",
            'image': "http://commonecoute.com/assets/images/product/025.png",
            'link_artist': ["http://commonecoute.com/urlartistunique.html"]
        },
        'artist': {
            'id_txt': "%s"%uuid.uuid4(),
            'url_txt': "http://commonecoute.com/urlartistunique.html",
            'name': "Amon Tobin",
            'link_product': ["http://commonecoute.com/urlproduct1.html", "http://commonecoute.com/urlproduct2.html"],
            'image': "http://commonecoute.com/assets/images/artist/025.png",
            'link_genre': ["http://commonecoute.com/urlelectronicunique.html"]
        },
        'genre': {
            'id_txt': "%s"%uuid.uuid4(),
            'url_txt': "http://commonecoute.com/urlelectronicunique.html",
            'name': "electronic"
        },
        'post': {
            'id_txt': "%s"%uuid.uuid4(),
            'link_track': ["http://commonecoute.com/urltrackunique.html"],
            'timingstart_date': str(datetime.utcnow().isoformat()),
            'timingend_date': str(datetime.utcnow().isoformat()),
            'votes': 0,
            'link_user': ['elishowk@nonutc.fr'],
            'content_txt': "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum"
        }
    }

    def setUp(self):
        self.c = TestApp(commonecouteserver.coeserver)
        
    def test_1create(self):
        """
        POST records
        """
        for bucket, record in self.data.iteritems():
            response = self.c.post('/%s'%bucket, json.dumps(record),
                                {'Content-Type':'application/json'})
            assert response.status == "200 OK"
        
    def test_2read(self):
        """
        GET initial records
        """
        for bucket, record in self.data.iteritems():
            response = self.c.get('/%s/%s'%(bucket, urllib.quote_plus(record['id_txt'])),
                                {'Accept': 'application/json'})
            data = response.json
            assert data == record

if __name__ == '__main__':
    unittest.main()
