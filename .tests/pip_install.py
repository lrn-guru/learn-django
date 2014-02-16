from subprocess import check_output, CalledProcessError, STDOUT

try:
	check_output('django-admin.py --version'.split(), stdout=open('/dev/null', 'w', sterr=STDOUT))
	exit(0)
except CalledProcessError:
	exit(1)
