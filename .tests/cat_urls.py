from subprocess import check_output, CalledProcessError

try:
	watch_for_command('cat urls.py')
	exit(0)
except CalledProcessError:
	exit(1)
