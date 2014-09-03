from distutils.core import setup
import subprocess

git_version = str(subprocess.check_output(['git', 'rev-parse', '--verify', '--short', 'HEAD'])).strip()

setup(
    name='dbushelpers',
    version='0.5.dev-%s' % git_version,
    author='Eero "rambo" af Heurlin',
    author_email='rambo@iki.fi',
    packages=['dbushelpers',],
    license='GNU LGPL',
    long_description=open('README.md').read(),
    install_requires=[
        'dbus-python>=1.0', # You will most likely need this from the distro packages
        'PyGObject>=2.0', # You will most likely need this from the distro packages
    ],
    url='https://github.com/rambo/python-dbushelpers',
)

