vim:
  pkg.installed

/usr/local/share/vim/vimrc:
  file.managed:
    - source: salt://conf/vim/vimrc
    - mode: 644
    - user: root
    - group: wheel

/usr/local/share/vim/vimrc.bepo:
  file.managed:
    - source: salt://conf/vim/vimrc.bepo
    - mode: 644
    - user: root
    - group: wheel

