from setuptools import setup, find_packages

setup(
	name='HC-AWS-Packaging',
	version='1.0',
	description='Packaging scripts for AWS Python Lambdas',
	packages=find_packages(exclude=['tests'])
)