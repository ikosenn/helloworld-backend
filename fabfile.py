from __future__ import print_function

import os

from helloworld.config import settings
from fabric.api import local


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def manage(command, args=''):
    local('{}/manage.py {} {}'.format(BASE_DIR, command, args))


def test(*args, **kwargs):
    local('python setup.py check')
    local('tox -r -c tox.ini')


def psql(query, username=None, password=None):
    user = 'postgres'
    pwd_env = ''

    if username:
        user = username

    if password:
        pwd_env = 'PGPASSWORD={}'.format(password)

    local('{pwd} psql -U {user} -w -c "{cmd}"'.format(
        user=user, pwd=pwd_env, cmd=query))


def setup(db_su_user=None, db_su_pass=None, *args, **kwargs):
    db_name = settings.DATABASES.get('default').get('NAME')
    db_user = settings.DATABASES.get('default').get('USER')
    db_pass = settings.DATABASES.get('default').get('PASSWORD')
    psql("DROP DATABASE IF EXISTS {}".format(db_name),
         username=db_su_user, password=db_su_pass)
    psql("DROP USER IF EXISTS {}".format(db_user),
         username=db_su_user, password=db_su_pass)
    psql("CREATE USER {0} WITH SUPERUSER CREATEDB "
         "CREATEROLE LOGIN PASSWORD '{1}'".format(db_user, db_pass),
         username=db_su_user, password=db_su_pass)
    psql('CREATE DATABASE {}'.format(db_name),
         username=db_su_user, password=db_su_pass)

    manage('migrate')


def run():
    manage('runserver', args='8092')
