/etc/login.conf:
  file.managed:
    - source: salt://conf/freebsd/login.conf
    - mode: 644
    - user: root
    - group: wheel

/etc/profile:
  file.managed:
    - source: salt://conf/freebsd/profile
    - mode: 644
    - user: root
    - group: wheel

/etc/profile.d/utf8.sh:
  file.managed:
    - source: salt://conf/freebsd/profile-utf8.sh
    - mode: 755
    - user: root
    - group: wheel

/etc/csh.login:
  file.managed:
    - source: salt://conf/freebsd/csh.login
    - mode: 644
    - user: root
    - group: wheel

/etc/profile.d/utf8.csh:
  file.managed:
    - source: salt://conf/freebsd/profile-utf8.csh
    - mode: 755
    - user: root
    - group: wheel
