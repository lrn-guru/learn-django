#!/usr/bin/env python
from subprocess import check_output

files = check_output('find .'.split())
if 'manage.py' in files:
    exit(0)
else:
    exit(1)