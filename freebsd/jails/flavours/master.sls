cmd.run:
  - /bin/cp -Rp /usr/jails/flavours/default /usr/jails/flavours/master
    - require:
      - sls: freebsd.jails.flavours.default
