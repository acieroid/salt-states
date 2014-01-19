/usr/jails/flavours/default:
  - file.directory
    - mode: 755
    - user: root
    - group: wheel

/usr/jails/flavours/default/etc/make.conf:
  - file.managed:
    - source: salt://freebsd/jails/flavours/default/make.conf
    - mode: 644
    - user: root
    - group: wheel
    - makedirs: True

/usr/jails/flavours/default/etc/periodic.conf:
  - file.managed
    - source: salt://freebsd/jails/flavours/default/periodic.conf
    - mode: 644
    - user: root
    - group: wheel
    - makedirs: True

/usr/jails/flavours/default/etc/rc.conf:
  - file.managed
    - source: salt://freebsd/jails/flavours/default/rc.conf
    - mode: 644
    - user: root
    - group: wheel
    - makedirs: True

/usr/jails/flavours/default/etc/resolv.conf:
  - file.managed
    - source: salt://freebsd/resolv.conf
    - mode: 644
    - user: root
    - group: wheel
    - makedirs: True

# TODO: install salt in the jail