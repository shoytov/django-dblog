import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="django-logging-into-db",  # Replace with your own username
	version="0.0.2",
	author="Dmitry Shoytov",
	author_email="shoytov@gmail.com",
	description="Log http errors or custom logs with loguru library into db",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/shoytov/django-dblog",
	packages=setuptools.find_packages(),
	install_requires=[
		'loguru',
	],
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)
