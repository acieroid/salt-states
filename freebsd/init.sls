/etc/resolv.conf:
  - file.managed:
    - source: salt://freebsd/resolv.conf
    - mode: 644
    - user: root
    - group: wheel

/usr/local/etc/pkg.conf:
  - file.absent

/usr/local/etc/pkg/repos/FreeBSD.conf
  - file.managed:
    - source: salt://freebsd/pkgng-FreeBSD.conf
    - mode: 644
    - user: root
    - group: wheel
