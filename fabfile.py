from fabric.api import *

def test():
    """
    This sets up the test server environment.
    """
    env.hosts = ["pisces.kgfamily.com"]
    env.dir = "/var/www/kgfamily.com/pisces/django"
    env.user = "pisces"
    env.settings = "settings_test"

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
        run("python manage.py syncdb --settings=%s" % env.settings)

def runtest():
    """
    Run unit test on the remote machine
    """
    print("Not ready yet... sorry!")

def restart():
    """
    Restart the remote test Apache server. You can't used this for production server.
    """
    sudo("apache2ctl graceful")


def ping():
    """
    Makes a connection to server and prints host type (via ``uname -monisr``).
    """
    print("Testing connection...")
    run("uname -monisr")
