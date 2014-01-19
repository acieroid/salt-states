if ( -d /etc/profile.d/ ) then
  foreach profile (/etc/profile.d/*.csh)
    test -r "$profile" && source "$profile"
  end
  unset profile
endif
