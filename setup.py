from setuptools import setup, find_packages
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='hackerfeed',
    version='0.1',
    description='Read hackernews right from your terminal!',
    long_description=long_description,
    author='Pratyush Prakash',
    author_email='pratyushprakash@live.co.uk',
    url='https://github.com/pratyushprakash/HackerFeed',
    license='MIT',
    keywords='news hacker hackernews terminal',
    packages=find_packages(),
    install_requires=['colorama', 'requests'],
    scripts=['bin/hfeed']
    )
