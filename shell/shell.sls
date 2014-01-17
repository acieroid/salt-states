/etc/profile:
  file.managed:
    - source: salt://conf/freebsd/profile
    - mode: 644
    - user: root
    - group: wheel

/etc/csh.login:
  file.managed:
    - source: salt://conf/freebsd/csh.login
    - mode: 644
    - user: root
    - group: wheel
