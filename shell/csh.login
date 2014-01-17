if test -d /etc/profile.d/; then
  foreach profile (/etc/profile.d/*.csh)
    test -r "$profile" && . "$profile"
  done
  unset profile
fi
