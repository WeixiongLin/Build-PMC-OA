""" Setup
"""
from setuptools import setup, find_packages
import codecs
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with codecs.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


exec(codecs.open('src/version.py').read())
setup(
    name='build_pubmed',
    version=__version__,
    description='PubMed',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitee.com/lin_wei_hung/build-pubmed',
    author='',
    author_email='',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # Note that this is a string of words separated by whitespace, not a list.
    keywords='PubMed Dataset',
    scripts = [
        'src/fetch_oa.py'
    ],
    package_dir={'': 'src'},
    packages=find_packages(where='src', exclude=['training']),
    include_package_data=True,
    install_requires=[
        'pandas>=1.1.3',
        'beautifulsoup4',
        'lxml',
        'tqdm',
        'jsonlines'
    ],
    python_requires='>=3.7',
)
