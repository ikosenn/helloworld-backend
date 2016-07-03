import click
from subprocess import call
import os
import json
import pkg_resources

import env_variables

backend_version = pkg_resources.require("helloworld-backend")[0].version
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ssh_user = 'kosen_deploy'
private_key = './.ssh/id_rsa'


def call_ansible(server, playbook, extra_vars):
    call([
        "ansible-playbook", "-i{},".format(server.strip()),
        "{}".format(playbook),
        "--extra-vars={}".format(extra_vars),
        "--ssh-extra-args=-o ServerAliveInterval=30",
    ])


def call_ansible_tag(server, playbook, extra_vars, tag):
    call([
        "ansible-playbook", "-i{},".format(server.strip()),
        "{}".format(playbook),
        "--extra-vars={}".format(extra_vars),
        "--ssh-extra-args=-o ServerAliveInterval=30",
        "--tags={}".format(tag)
    ])


def run_acceptance_test():
    call(["py.test", "deployment_acceptance.py"])


@click.group()
def deploy():
    """Deploys the hello world application"""
    pass


@deploy.command()
@click.option('--api-server', default="slade360emr.com",
              prompt="Server domain",
              help="The domain name of the server you're deploying to.")
@click.option('--frontend-server', default="www.slade360emr.com",
              prompt="Frontend server domain",
              help="The domain name of the server frontend.")
@click.option('--force',
              help="Ignore the lock file that prevents parallel deploys, \
if a previous deploy was aborted.",
              is_flag=True,
              default=False)
@click.option('--setup-new-certs',
              help="Copy SSL certificates from a local directory to the \
server's tls directory",
              is_flag=True,
              default=False)
@click.option('--setup-new-db',
              help="Drop the existing database and rebuild the entire \
application from default data. This is irreversible.",
              is_flag=True,
              prompt="If you are deploying to a new server or want to \
rebuild the application's database from default data, \
              please respond [y], otherwise [n]",
              default=True)
@click.option('--ssl-on', help="Turn on ssl.",
              is_flag=True,
              prompt="Would you like to turn on SSL? This only changes \
nginx sites-available settings for your app, and \
requires ssl certificates.",
              default=True)
@click.option('--version', prompt="emr-backend's version",
              help="The version of emr-backend you'd like to deploy.",
              default=backend_version)
def backend(api_server, frontend_server, version, force, setup_new_db, ssl_on,
            setup_new_certs):
    """Deploys the backend application."""

    if force:
        ignore_lock = 'true'
    else:
        ignore_lock = 'false'

    if setup_new_certs:
        setup_ssl_certs = 'true'
    else:
        setup_ssl_certs = 'false'

    if ssl_on:
        deploy_https = 'true'
    else:
        deploy_https = 'false'

    if setup_new_db:
        setup_new_database = 'true'
    else:
        setup_new_database = 'false'

    extra_vars = {
        'emrapi_staging_version': version,
        'ansible_ssh_user': ssh_user,
        'ansible_ssh_private_key_file': private_key,
        'pg_login_user': env_variables.login_user,
        'pg_login_password': env_variables.login_password,
        'db_user': env_variables.db_user,
        'db_pass': env_variables.db_pass,
        'db_name': env_variables.db_name,
        'setup_new_db': setup_new_database,
        'ansible_host': api_server,
        'api_server_domain': api_server,
        'server_domain': frontend_server,
        'emrapi_secret_key': env_variables.secret_key,
        'libcloud_user': env_variables.libcloud_user,
        'libcloud_key': env_variables.libcloud_key,
        'sudo_magick_needed': 'true',
        'force_ignore_lock': ignore_lock,
        'setup_new_ssl_certs': setup_ssl_certs,
        'ssl_on': deploy_https,
        'aws_key_id': env_variables.aws_key_id,
        'aws_secret': env_variables.aws_secret,
        'front_end_url': env_variables.front_end_url,
        'libcloud_storage': env_variables.libcloud_storage,
        'libcloud_provider': env_variables.libcloud_provider,
        'libcloud_type': env_variables.libcloud_type,
        'libcloud_bucket': env_variables.libcloud_bucket
    }

    click.echo(extra_vars)
    click.echo("Deploying EMR API version {} to \
domain {}!".format(version, api_server))

    call_ansible(api_server, 'emrapi_staging.yml', json.dumps(extra_vars))
    run_acceptance_test()


@deploy.command()
@click.option('--frontend-server',
              default="helloworld.co.ke",
              prompt="Server domain",
              help="The domain name of the server you're deploying to.")
@click.option('--api-server',
              default="api.helloworld.co.ke",
              prompt="API server domain",
              help="The domain name of the API which serves this frontend.")
@click.option('--force',
              help="Ignore the lock file that prevents parallel deploys, \
if a previous deploy was aborted.",
              is_flag=True)
@click.option('--version', prompt="Version",
              help="The version you'd like to deploy.")
@click.option('--setup-new-certs',
              help="Copy SSL certificates from a local directory to the \
server's tls directory",
              is_flag=True,
              default=False)
@click.option('--ssl-on', help="Turn on ssl.",
              is_flag=True,
              default=True,
              prompt="Would you like to turn on SSL? This only changes nginx \
sites-available settings for your app, and requires ssl \
certificates.")
def frontend(
        frontend_server, version, force, api_server, ssl_on, setup_new_certs):
    """Deploys the frontend application."""

    if force:
        ignore_lock = 'true'
    else:
        ignore_lock = 'false'

    if ssl_on:
        deploy_https = 'true'
    else:
        deploy_https = 'false'

    if setup_new_certs:
        setup_ssl_certs = 'true'
    else:
        setup_ssl_certs = 'false'

    extra_vars = {
        'helloworld_frontend_version': str(version),
        'ansible_ssh_user': ssh_user,
        'ansible_ssh_private_key_file': private_key,
        'ansible_host': frontend_server,
        'server_domain': frontend_server,
        'api_server_domain': api_server,
        'sudo_magick_needed': 'true',
        'force_ignore_lock': ignore_lock,
        'ssl_on': deploy_https,
        'setup_new_ssl_certs': setup_ssl_certs,
    }

    click.echo(extra_vars)
    click.echo("Deploying helloworld frontend version {} to \
domain {}!".format(version, frontend_server))
    call_ansible(
        frontend_server, 'helloworld_frontend.yml', json.dumps(extra_vars))


if __name__ == '__main__':
    deploy()
