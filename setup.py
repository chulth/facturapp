#!/usr/bin/env python
import os
import re
import sys

from setuptools import setup


def get_version(*file_paths):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version('productdataapi', '__init__.py')

if sys.argv[-1] == 'tag':
    print("Tagging the version on github:")
    os.system("git tag -a %s -m 'version %s'" % (VERSION, VERSION))
    os.system("git push --tags")
    sys.exit()

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='productdataapi',
    version=VERSION,
    description="""service where we store product data""",
    long_description=README,
    author='John Bulla',
    author_email='chulth@gmail.com',
    url='https://github.com/chulth/productdataapi',
    packages=[
        'productdataapi',
    ],
    include_package_data=True,
    install_requires=[
        "Django>=3.2"
    ],
    zip_safe=False,
    keywords='Django',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
    ],
)
