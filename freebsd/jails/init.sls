jailaudit:
  pkg.installed

# TODO: configure jailaudit to send mails

ezjail:
  pkg.installed:
    - name: ezjail
  service:
    - enable: True
    - running


ezjail_use_zfs:
  freebsdconf.set:
    - value: YES

ezjail_jailfs:
  freebsdconf.set:
    - value: zroot/ezjail

ezjail_use_zfs_for_jails:
  freebsdconf.set:
    - value: YES

# TODO: run only if /usr/jails is not yet populated
#Install the basejail:
#  cmd.run:
#    - name: ezjail-admin install
#    - cwd: /
