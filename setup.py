import os
import uuid

from pip.req import parse_requirements
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

install_reqs = parse_requirements(os.path.join(here, 'requirements.txt'), session=uuid.uuid1())
reqs = [str(ir.req) for ir in install_reqs]

with open(os.path.join(here, 'README.md')) as fp:
    long_description = fp.read()

setup(
    name='kim-test',
    version='0.0.1',,
    tests_require=['tox'],
    url='https://github.com/kimdhamilton/pyld-test',
    license='MIT',
    long_description=long_description,
    packages=find_packages(),
    install_requires=reqs
)
