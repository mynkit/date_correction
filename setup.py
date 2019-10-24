# -*- coding: utf-8 -*-

from setuptools import find_packages, setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name='date_correction',
    version='0.0.2',
    python_requires='>=3.5',
    author='mynkit',
    author_email='dcm5124289@gmail.com',
    packages=[
        'date_correction',
    ],
    url='https://github.com/mynkit/date_correction',
)
