from setuptools import setup, find_packages


config = {
    'description': 'Read hackernews right from your terminal!',
    'author': 'Pratyush Prakash',
    'version': '0.1',
    'install_requires': ['colorama', 'requests'],
    'packages': find_packages(),
    'scripts': ['bin/hfeed'],
    'name': 'hackerfeed'
    }

setup(**config)
