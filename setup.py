import sys
from setuptools.command.test import test as TestCommand
from setuptools import setup


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='geogate',
    version='0.1',
    url='http://github.com/SP7-Ritmare/geogate',
    license='GPL3',
    author='Stefano Menegon',
    author_email='ste.menegon@gmail.com',
    description='geogate',
#    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.md').read(),
    tests_require=['pytest-django>=3.0,<3.1', 'pytest>=3.0,<3.1', 'coveralls', 'flake8'],
    cmdclass={'test': PyTest},
    py_modules=['geogate'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)
