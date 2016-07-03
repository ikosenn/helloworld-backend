import click
import os
import sys
import json
import pkg_resources
from subprocess import call
import env_variables

backend_version = pkg_resources.require("emr-backend")[0].version
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


ssh_user = os.environ.get('USER', '')
private_key = os.environ.get('ANSIBLE_SSH_PRIVATE_KEY_FILE',
                             '~/.ssh/google_compute_engine')


def _fail_loudly(sarge_obj):
    """
    Throw an exit(1) error when the return code from sarge runs command is
    not zero
    """
    if sarge_obj.returncode:
        sys.exit(1)


def call_ansible_tag(server, playbook, extra_vars, tag):
    call([
        "ansible-playbook", "-i{},".format(server.strip()),
        "{}".format(playbook),
        "--extra-vars={}".format(extra_vars),
        "--ssh-extra-args=-o ServerAliveInterval=30",
        "--tags={}".format(tag)
    ])


@click.group()
def deploy():
    """Deploys the EMR application"""
    pass


@deploy.command()
@click.option('--server', default="slade360emr.com",
              help="The domain name of the server you're deploying to.")
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
              default=True)
@click.option('--ssl-on', help="Turn on ssl.",
              is_flag=True,
              default=True)
@click.option('--version',
              help="The version of emr-backend you'd like to deploy.",
              default=backend_version)
def backend(server, version, force, setup_new_db, ssl_on,
            setup_new_certs):
    """Deploys the backend application from the continuous\
 integration server."""

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
        'ansible_host': server,
        'server_domain': server,
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
domain {}!".format(version, server))

    call_ansible_tag(
        server, 'emrapi_staging.yml', json.dumps(extra_vars), "emrapi_staging")

if __name__ == '__main__':
    deploy()
