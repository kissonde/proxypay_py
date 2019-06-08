

from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='proxypay_py',

    version='1.0.0',

    description='A Python client to use with ProxyPay API (www.proxypay.co.ao)',

    long_description=long_description,

    long_description_content_type='text/markdown',

    url='https://github.com/kissonde/proxypay_py',

    author='Timeboxed Lda.',

    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Multicaixa Payments',
        'License :: OSI Approved :: GPL',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='multicaixa proxypay api',  # Optional

    py_modules=["proxypay"],
    #packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required

    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',

    #install_requires=[],  # Optional

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/kissonde/proxypay_py/issues',
        'Source': 'https://github.com/kissonde/proxypay_py',
    },
)