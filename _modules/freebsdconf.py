# -*- coding: utf-8 -*-
'''
Module that manages FreeBSD configuration files (in the same format as
/etc/rc.conf). Do *not* use to enable services, use the service module
instead.
'''

import fileinput
import os
import sys
import salt.utils

def _comment(line):
    splitted = line.split()
    return len(splitted) > 0 and len(splitted[0]) > 0 and splitted[0][0] == '#'

log = []
def _get_value(path, key):
    with open(path, 'r') as f:
        for line in f.readlines():
            if '=' in line:
                [k, eq, v] = line.partition('=')
                log.append([k, eq, v])
                if k == key:
                    return v
    return False

def _add(path, key, value):
    with open(path, 'a') as f:
        f.write('{}="{}"\n'.format(key, value))

def _replace(path, key, value):
    for line in fileinput.input(path, inplace = 1):
        if '=' in line:
            [k, eq, v] = line.partition('=')
            if k == key:
                sys.stdout.write('{}="{}"\n'.format(key, value))
            else:
                sys.stdout.write(line)
        else:
            sys.stdout.write(line)

def set(path, key='', value=''):
    '''
    Set or update a value for a configuration key

    CLI Example::

        salt '*' freebsdconf.set /etc/rc.conf ezjail_jaifs zroot/ezjail
    '''
    ret = {'name': path,
           'changes': {}}
    prev = _get_value(path, key)
    if prev:
        # drop quotes and newline
        if len(prev) > 1 and prev[0] == '"':
            prev = prev[1:-2]
        else:
            prev = prev[:-1]

        if prev == value or prev == '"{}"'.format(value):
            ret['result'] = True
            ret['comment'] = 'Same value was already set'
        else:
            _replace(path, key, value)
            ret['result'] = True
            ret['comment'] = 'Value replaced'
            ret['changes'][path] = {key: '{} -> {}'.format(prev, value)}
    else:
        _add(path, key, value)
        ret['changes'][path] = {key: value}
        ret['result'] = True
        ret['comment'] = 'Value added'
    return ret

