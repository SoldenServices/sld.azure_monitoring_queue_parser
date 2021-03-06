#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    "azure-storage-queue==12.1.5",
]

test_requirements = [
    'pytest>=3',
]

setup(
    author="Matthew Larsen",
    author_email='Matt Larsen <matt.larsen@connorgp.com>',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Library to read queue messages from Azure storage and interpret them as Nagios checks",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='nagios plugin azure queue',
    name='sld.azure_monitoring_queue_parser',
    packages=find_packages(include=['azure_monitoring_queue_parser', 'azure_monitoring_queue_parser.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/SoldenServices/sld.azure_monitoring_queue_parser',
    version='0.0.1',
    zip_safe=False,
)
