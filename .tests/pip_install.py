#!/usr/bin/env python
from subprocess import check_output, CalledProcessError, STDOUT

try:
	check_output('django-admin.py --version'.split(), stdout=open('/dev/null', 'w'), stderr=STDOUT)
	exit(0)
except CalledProcessError:
	exit(1)
