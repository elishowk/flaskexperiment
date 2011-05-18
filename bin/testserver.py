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
    
from werkzeug.test import Client
from werkzeug.wrappers import BaseResponse


class COEserverTestCase(unittest.TestCase):
    data = {
        'user': {'id_txt': 'elishowk@nonutc.fr', 'firstname_txt':'elias'}
    }

    def setUp(self):
        self.c = Client(commonecouteserver.coeserver, BaseResponse)
        
    def test_create(self):
        response = self.c.post(path='user/', data=self.data['user'])
        print response.response
        
    def test_read(self):
        response = self.c.get(path='user/'+self.data['user']['id_txt'], content_type='application/json')
        print response.response
        self.assertTrue( isinstance( response, BaseResponse) )

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()