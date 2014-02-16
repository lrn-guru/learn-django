#!/usr/bin/env python
import sys

command = sys.argv[-1]
if 'cat' in command and 'urls.py' in command:
	exit(0)
else:
	exit(1)
