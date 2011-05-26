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

import logging
from logging.handlers import SMTPHandler, RotatingFileHandler

LOG_FILE = "log.txt"
ADMINS = ['elishowk@localhost']

def setlogger(coeserver):
    if not coeserver.debug:
        mail_handler = SMTPHandler('127.0.0.1',
                                   'commonecouteserver-error@commonecoute.com',
                                   ADMINS, 'coeserver Failed')
        mail_handler.setLevel(logging.ERROR)
        coeserver.logger.addHandler(mail_handler)
    else:
        # sets debugging formatting and handler
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            '%Y-%m-%d %H:%M:%S'
        )
        rotatingFileHandler = RotatingFileHandler(
            filename = LOG_FILE,
            maxBytes = 1024*100,
            backupCount = 2
        )
        rotatingFileHandler.setFormatter(formatter)
        rotatingFileHandler.setLevel(logging.DEBUG)
        coeserver.logger.addHandler(rotatingFileHandler)