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

class COEserverTestCase(unittest.TestCase):
    data = {
        'user': {'id_txt': 'elishowk@nonutc.fr', 'firstname_txt':'elias'}
    }

    def setUp(self):
        self.c = TestApp(commonecouteserver.coeserver)
        
    def test_create(self):
        response = self.c.post('/user/', json.dumps(self.data['user']),
                            {'Content-Type':'application/json'})
        self.assertTrue( isinstance( response, webob.Response) )
        
    def test_read(self):
        response = self.c.get('/user/'+self.data['user']['id_txt']+'/',
                            {}, {'Content-Type':'application/json', 'Accept': 'application/json'})
        print response.json
        self.assertTrue( isinstance( response, webob.Response) )

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()