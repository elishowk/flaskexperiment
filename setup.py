from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()

version = '0.1'

install_requires = [
    'flask',
    'pymongo',
    'silk-deployment',
    'simplejson'
    # For more details, see:
    # http://packages.python.org/distribute/setuptools.html#declaring-dependencies
]


setup(
    name='commonecouteserver',
    version=version,
    description="Core CommOnEcoute Server",
    long_description=README,
    classifiers=[
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Server"
      # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords='http web server riak',
    author='Elias Showk',
    author_email='elishowk@nonutc.fr',
    url='http://commonecoute.com',
    license='GNU AGPL v3',
    packages=find_packages('.'),
    #package_dir = {'': '.'},
    include_package_data=True,
    scripts = ['bin/coeserver.py'],
    zip_safe=False,
    install_requires=install_requires,
    #entry_points={
    #    'console_scripts':
    #        ['commonecouteserver=commonecouteserver:main']
    #}
)
