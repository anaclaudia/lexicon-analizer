try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
		'description': 'My project',
		'author': 'Your name',
		'url': 'URL to get it at',
		'download_url': 'Where to download it',
		'author_email': 'Your email',
		'version': '0.1',
		'install_requires': ['nose'],
		'packages': ['name'],
		'scripts':[],
		'name': 'project_name'
}
