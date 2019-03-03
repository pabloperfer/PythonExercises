python3 find.py -h
usage: find.py [-h] path name {-,d,l}

positional arguments:
  path        Enter the path where you want to search the file
  name        Enter the name of the file you look for
  {-,d,l}     Enter the type of file you are looking for from the above
              choices

optional arguments:
  -h, --help  show this help message and exit

$ sudo python3 find.py /tmp pp l
/tmp/pp


$ sudo python3 find.py / sysctl.conf -
/etc/sysctl.conf
/etc/test/sysctl.conf

$ sudo python3 find.py / lvm d
/var/run/lvm
/var/lock/lvm
/etc/lvm

