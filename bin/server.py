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
import bottle
bottle.debug(True)
from bottle import run
import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)-8s %(message)s")

if __name__ == "__main__":
    run(commonecouteserver.coes, host='localhost', port=8080)
