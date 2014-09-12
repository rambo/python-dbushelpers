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
    description='Helpers to wrap some of the boilerplate for creating DBUS enabled services in Python',
    install_requires=[
#        'dbus-python>=1.0', # You will most likely need this from the distro packages
        'PyGObject>=2.0', # You will most likely need this from the distro packages
        'PyYAML>=3.0', # This will be more performant if you install distro package compiled against libyaml
    ],
    url='https://github.com/rambo/python-dbushelpers',
)

