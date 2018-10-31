#!/usr/bin/env python3
import re
from pathlib import Path  # pathlib can't be imported in Python < 3.4.

from setuptools import setup


def get_version(string):
    """ Retrieve the ``__version__`` attribute. """
    flags = re.S
    pattern = r".*__version__ = '(.*?)'"
    match = re.match(pattern=pattern, string=string, flags=flags)

    if match:
        return match.group(1)

    raise RuntimeError('No version string could be matched')


here = Path(__name__).cwd()
version = get_version((here / 'yacht.py').read_text())

# Requirements.
install_reqs = []
test_reqs = ['flake8', 'mypy', 'pytest', 'pytest-cov']
docs_reqs = ['Sphinx', 'sphinx-autodoc-typehints']
dev_reqs = test_reqs + docs_reqs

setup(
    name='yacht',
    version=version,
    description='Score a game of Yacht.',
    author='Reilly Tucker Siemens',
    author_email='reilly@tuckersiemens.com',
    url='https://github.com/reillysiemens/yacht',
    install_requires=install_reqs,
    license='ISCL',
    py_modules=['yacht'],
    keywords='Yacht game',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries',
    ],
    test_suite='tests',
    tests_require=test_reqs,
    python_requires='>=3.6',
    extras_require={
        'dev': dev_reqs,
        'docs': docs_reqs,
        'test': test_reqs,
    },
)
