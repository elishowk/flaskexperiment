import os
import silk.fabfile
from fabric.api import *
from fabric.contrib.files import exists
import cuisine
    
def push():
    """
    Override silk's main function adding riaksearch installing and configuring
    """
    print "OVERIDDEN PUSH FUNCTION"
    silk.fabfile.archive()
    silk.fabfile.install_deps()
    #riaksearch_install()
    silk.fabfile.push_code()
    silk.fabfile.write_config()
    silk.fabfile.switch()
    silk.fabfile.restart()
    #riaksearch_config()
    silk.fabfile.cleanup()
    
def update():
    """
    update code and configs, but no installs
    """
    silk.fabfile.archive()
    silk.fabfile.push_code()
    silk.fabfile.write_config()
    silk.fabfile.switch()
    silk.fabfile.restart()
    silk.fabfile.cleanup()

def cleanup():
    silk.fabfile.cleanup()

def riaksearch_install():
    """
    installs riaksearch package and python lib
    """
    print "INSTALLING RIAK SEARCH"
    print "STOPPING RIAK SEARCH"
    sudo("riaksearch stop")
    build_dir = "/tmp/riak_build"
    gitdirname = "pythonriak"
    if not exists(build_dir, use_sudo=True):
        sudo('mkdir -p %s' % build_dir)
    with cd(build_dir):
        #download the tools
        sudo('wget %s -O riaksearch.deb'%env.config['site_deps']['riak']['deb'])
        #unpack
        sudo('dpkg -i riaksearch.deb')
        sudo('rm -rf %s'%gitdirname)
        sudo('git clone %s %s'%(env.config['site_deps']['riak']['python'],gitdirname))
    with cd(os.path.join(build_dir, gitdirname)):
        #install into the virtualenv
        sudo('%s setup.py install' % os.path.join(env.envdir, 'bin', 'python'))
    sudo('rm -rf %s' % build_dir)
    print "STARTING RIAK SEARCH"
    sudo("riaksearch start")

def riaksearch_config():
    #sudo("riaksearch start")
    print "ACTIVATING INDEXING ON ALL RIAK BUCKETS"
    for bucket in ['track','event','user','post','product','genre','artist']:
        run("""
        curl -X PUT -H "content-type:application/json" http://%s:8098/riak/%s --data '{"props":{"precommit":[{"mod":"riak_search_kv_hook","fun":"precommit"}]}}'
        """%(env.config['env']['COESERVER_DB_HOST'], bucket))