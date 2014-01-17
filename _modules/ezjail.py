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

def _status(name):
    cmd = 'ezjail-admin list'
    out = __salt__['cmd.run'](cmd).splitlines()
    for line in out[2:]:
        content = line.split()
        if len(content) == 5:
            [status, jid, ip, hostname, root] = content
            if hostname == name:
                return {'status': status,
                        'jid': jid,
                        'hostname': hostname,
                        'root': root}
    return {'status': '',
            'jid': 'N/A',
            'hostname': name,
            'root': ''}

def _start_jail(name):
    status = _status(name)
    ret = {'name': name,
           'changes': {}}
    if 'R' in status['status']:
        ret['result'] = True
        ret['comment'] = 'Jail was already started'
    else:
        cmd = 'ezjail-admin start {0}'.format(name)
        if __salt__['cmd.retcode'](cmd) == 0:
            ret['changes']['running'] = True
            ret['result'] = True
            ret['comment'] = 'Jail successfully started'
        else:
            ret['result'] = False
            ret['comment'] = 'Error when starting jail'
    return ret

def _start_all_jails():
    cmd = 'ezjail-admin start'
    ret['name'] = ''
    ret['result'] = __salt__['cmd.retcode'](cmd) == 0
    ret['comment'] = ''
    ret['changes'] = {}
    return ret

def _stop_jail(name):
    status = _status(name)
    ret = {'name': name,
           'changes': {}}
    if 'S' in status['status'] or 'D' in status['status']:
        ret['result'] = True
        ret['comment'] = 'Jail was not running'
    else:
        cmd = 'ezjail-admin stop {0}'.format(name)
        if __salt__['cmd.retcode'](cmd) == 0:
            ret['changes']['stopped'] = True
            ret['result'] = True
            ret['comment'] = 'Jail successfully stopped'
        else:
            ret['result'] = False
            ret['comment'] = 'Error when stopping jail'
    return ret

def _stop_all_jails():
    cmd = 'ezjail-admin stop'
    ret['name'] = ''
    ret['result'] = __salt__['cmd.retcode'](cmd) == 0
    ret['comment'] = ''
    ret['changes'] = {}
    return ret

def _restart_jail(name):
    status = _status(name)
    ret = {'name': name,
           'changes': {}}
    cmd = 'ezjail-admin restart {0}'.format(name)
    if __salt__['cmd.retcode'](cmd) == 0:
        ret['result'] = True
        ret['comment'] = 'Jail successfully restarted'
    else:
        ret['result'] = False
        ret['comment'] = 'Error when stopping jail'
    return ret

def _restart_all_jails():
    cmd = 'ezjail-admin restart'
    ret['name'] = ''
    ret['result'] = __salt__['cmd.retcode'](cmd) == 0
    ret['comment'] = ''
    ret['changes'] = {}

def start(name=''):
    '''
    Start the specified jail or all, if none specified

    CLI Example::

        salt '*' ezjail.start [<jail name>]
    '''
    if name == '':
        return _start_all_jails()
    else:
        return _start_jail(name)

def stop(name=''):
    '''
    Stop the specified jail or all, if none specified

    CLI Example::

        salt '*' ezjail.stop [<jail name>]
    '''
    if name == '':
        return _stop_all_jails()
    else:
        return _stop_jail(name)

def restart(name=''):
    '''
    Restart the specified jail or all, if none specified

    CLI Example::

        salt '*' ezjail.restart [<jail name>]
    '''
    if name == '':
        return _restart_all_jails()
    else:
        return _restart_jail(name)

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
