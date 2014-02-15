from subprocess import check_output, CalledProcessError

try:
	check_output('django-admin.py --version'.split())
	exit(0)
except CalledProcessError:
	exit(1)
