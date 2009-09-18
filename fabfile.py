from fabric.api import *

def test():
    """
    This sets up the test server environment.
    """
    env.hosts = ["pisces.kgfamily.com"]
    env.dir = "/var/www/kgfamily.com/django/pisces"
    env.user = "highwind"
    env.settings = "settings_test.py"

def clone():
    """
    Checks out fresh copy of the project from github. No need to run this again.
    """
    run("git clone git@github.com:highwind/pisces.git " + env.dir)

def update():
    """
    Updates the code from the git repository.
    """
    with cd(env.dir):
        run("git pull origin master")

def syncdb():
    """
    Runs manage.py syncdb on the server.
    """
    with cd(env.dir):
        run("python manage.py --settings=%s syncdb" % env.settings)

def host_type():
    """
    Prints host type (via ``uname -s``) for a remote host.
    """
    run("uname -a")
