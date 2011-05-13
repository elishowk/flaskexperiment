
import commonecouteserver
import bottle
bottle.debug(True)
from bottle import run
import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)-8s %(message)s")

if __name__ == "__main__":
    run(commonecouteserver.coes, host='localhost', port=8080)
