#!/usr/bin/python3
"""Uses Fabric to execute the Cmds locally"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Creates a directory and compresses files
        as a specified name
    """
    time_test = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_" + time_test + ".tgz"
    comm1 = "mkdir -p versions"
    comm2 = "tar -czvf " + file_name + " web_static"
    local(comm1)
    com = local(comm2)
    if com.return_code == 0:
        return (file_name)
    else:
        return None
