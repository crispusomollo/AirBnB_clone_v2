#!/usr/bin/python3
"""
This module will use fabric to
deploy your files to the server
"""


from fabric.api import env, run, put
import os


env.hosts = ['35.237.123.100', '3.237.25.182']


def do_deploy(archive_path):
    """ Takes the path of the archive
        and uploads it to server
    """
    if not os.path.exists(archive_path):
        return False

    file_ext = archive_path[archive_path.find('/') + 1:]
    file_name = archive_path[archive_path.find('/') + 1: -4]

    result = put(archive_path, '/tmp/' + file_ext)
    if result.failed:
        return False

    result = run('mkdir -p /data/web_static/releases/' + file_name + '/')
    if result.failed:
        return False

    result = run('tar -xzf /tmp/' + file_ext +
                 ' -C /data/web_static/releases/' + file_name + '/')
    if result.failed:
        return False

    result = run('rm /tmp/' + file_ext)
    if result.failed:
        return False

    result = run('mv /data/web_static/releases/' + file_name +
                 '/web_static/* /data/web_static/releases/' + file_name + '/')
    if result.failed:
        return False

    result = run('rm -rf /data/web_static/releases/' + file_name +
                 '/web_static')
    if result.failed:
        return False

    result = run('rm -rf /data/web_static/current')
    if result.failed:
        return False

    result = run('ln -s /data/web_static/releases/' +
                 file_name + '/ /data/web_static/current')
    if result.failed:
        return False

    print('New version deployed!')
    return True
