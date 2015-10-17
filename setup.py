from setuptools import setup, find_packages
import re

VERSIONFILE = "src/alight/__init__.py"
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
except EnvironmentError:
    print "unable to find version in %s" % (VERSIONFILE,)
    raise RuntimeError("if %s exists, it is required to be well-formed" % (VERSIONFILE,))

setup(
    name='aLight-server',
    version=verstr,
    description='Python-based server designed to be compatible with MiLight devices',
    author='James Muscat',
    author_email='jamesremuscat@gmail.com',
    url='https://github.com/jamesremuscat/aLight-server',
    packages=find_packages('src', exclude=["*.test*"]),
    package_dir = {'':'src'},
      long_description="""\
      Python-based server designed to be compatible with MiLight devices
      """,
    install_requires=["socket", "enum34"],
    entry_points={
        'console_scripts': [
            # 'avx-controller = org.muscat.avx.controller.Controller:main',
            ],
        }
      )
