#!/usr/bin/env python3

import docker
import time

client = docker.from_env()

try:
    rockylinux = client.containers.run('rockylinux:9', detach=False,
            volumes=['/home/steph/dev/pysyncoffline.git/repos:/repos', 
            '/home/steph/dev/pysyncoffline.git/commands:/commands',
            '/media/steph/dd_sp/repos:/data'],
        command='bash /commands/syncrockylinux.bash', name='rockylinux')
        #command='sleep 1d', name='rockylinux')
except:
    rockylinux.logs()
    rockylinux.remove(force=True)

#client.containers.run("rockylinux:9-minimal", detach=True)
