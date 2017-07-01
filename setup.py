from setuptools import setup


config = {
    'description': 'Read hackernews right from your terminal!',
    'author': 'Pratyush Prakash',
    'version': '0.1',
    'install_requires': ['colorama', 'requests'],
    'packages': ['hfeedlib', 'hfeedlib/parsing'],
    'scripts': ['bin/hfeed'],
    'name': 'hackerfeed'
    }

setup(**config)
