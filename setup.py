import setuptools
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()
setuptools.setup(
	name="cdx-mol",
	version="0.0.4",
	description="This is a file conversion library: cdx-mol",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	package_data={'': ['*.yaml','*.yml','*.cdxml']},
	python_requires='>=3.6',
	install_requires=[
		'lxml>=4.9.2',
	],
)