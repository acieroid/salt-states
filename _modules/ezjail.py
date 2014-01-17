# -*- coding: utf-8 -*-
'''
Jail module that uses ezjail, for FreeBSD
'''

import os
import salt.utils

__virtualname__ = 'ezjail'

def __virtual__():
    '''
    Only runs on FreeBSD systems
    '''
    return __virtualname__ if __grains__['os'] == 'FreeBSD' else False

def start(jail=''):
    '''
    Start the specified jail or all, if none specified

    CLI Example::

        salt '*' ezjail.start [<jail name>]
    '''
    cmd = 'ezjail-admin start {0}'.format(jail)
    return not __salt__['cmd.retcode'](cmd)

def stop(jail=''):
    '''
    Stop the specified jail or all, if none specified

    CLI Example::

        salt '*' ezjail.stop [<jail name>]
    '''
    cmd = 'ezjail-admin stop {0}'.format(jail)
    return not __salt__['cmd.retcode'](cmd)

def restart(jail=''):
    '''
    Restart the specified jail or all, if none specified

    CLI Example::

        salt '*' ezjail.restart [<jail name>]
    '''
    cmd = 'ezjail-admin restart {0}'.format(jail)
    return not __salt__['cmd.retcode'](cmd)

def list():
    '''
    Return the list of jails and their status

    CLI Example::

        salt '*' ezjail.list
    '''
    cmd = 'ezjail-admin list'
    ret = {}
    out = __salt__['cmd.run'](cmd).splitlines()
    for line in out[2:]:
        content = line.split()
        if len(content) == 5:
            [status, jid, ip, hostname, root] = content
            ret[hostname] = {'status': status,
                             'jid': jid,
                             'ip': ip,
                             'hostname': hostname,
                             'root': root}

    return ret
