from subprocess import check_output, CalledProcessError


def run():
    try:
        check_output('django-admin.py --version'.split())
        return 'success'
    except CalledProcessError:
        return 'failure'
