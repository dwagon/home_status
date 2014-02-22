#!/usr/bin/env python

from fabric.api import sudo, task, run
from fabric.context_managers import lcd
from fabric.operations import put


@task
def initialize_system():
    sudo('apt-get install -y nginx git python-dev')
    put('sck.nginx', '/etc/nginx/sites-enabled/sck', use_sudo=True)


@task
def deploy():
    run('git clone https://github.com/dwagon/home_status.git')
    with lcd('home_status'):
        put('../apikey.py', 'apikey.py')
        sudo('pip install -r requirements.txt')


@task
def runserver():
    with lcd('home_status'):
        run('gunicorn -w 4 -b 127.0.0.1:8000 sck:app')
        sudo('/etc/init.d/nginx restart')

#EOF
