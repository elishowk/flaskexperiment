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
    #install_riak()
    silk.fabfile.push_code()
    silk.fabfile.write_config()
    silk.fabfile.switch()
    silk.fabfile.restart()
    #riaksearchrestart()
    #riaksearchconfig()
    silk.fabfile.cleanup()
    
def update():
    """
    update code and configs, but not deps
    NOT TESTED
    """
    silk.fabfile.archive()
    silk.fabfile.push_code()
    silk.fabfile.write_config()
    silk.fabfile.switch()
    silk.fabfile.reload()
    silk.fabfile.cleanup()

def cleanup():
    silk.fabfile.cleanup()

def install_riak():
    """
    installs riaksearch package and python lib
    """
    print "INSTALLING RIAK SEARCH"
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

def riaksearchrestart():
    print "RESTARTING RIAK SEARCH"
    sudo("service riaksearch stop")
    sudo("service riaksearch start")

def riaksearchconfig():
    print "ACTIVATING INDEXING ON ALL RIAK BUCKETS"
    sudo("service riaksearch start")
    for bucket in ['track','event','user','post','product','genre','artist']:
        run("""
        curl -X PUT -H "content-type:application/json" http://localhost:8098/riak/%s --data '{"props":{"precommit":[{"mod":"riak_search_kv_hook","fun":"precommit"}]}}'
        """%bucket)