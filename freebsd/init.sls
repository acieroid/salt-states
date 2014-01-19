/etc/resolv.conf:
  - file.append:
    - text:
      - nameserver 8.8.8.8

/usr/local/etc/pkg.conf:
  - file.absent

/usr/local/etc/pkg/repos/FreeBSD.conf
  - file.managed:
    - source: salt://freebsd/pkgng-FreeBSD.conf
    - mode: 644
    - user: root
    - group: wheel
