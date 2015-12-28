try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python client for Microsoft\'s Project Oxford web language model',
    'author': 'Will Fitzgerald',
    'url': 'https://github.com/willf/oxford_language_model',
    'download_url': 'https://github.com/willf/oxford_language_model',
    'author_email': 'Will.Fitzgerald@gmail.com',
    'version': '0.1',
    'install_requires': ['requests'],
    'packages': ["oxford_language_model"],
    'scripts': [],
    'name': 'oxford_language_model'
}

setup(**config)