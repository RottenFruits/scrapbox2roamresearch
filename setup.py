#!/usr/bin/env python3
from setuptools import setup, find_packages

with open('requirements.txt') as requirements_file:
    install_requirements = requirements_file.read().splitlines()

setup(
    name = "scrapbox2roamresearch",
    version = "0.0.1",
    description = "",
    author = "Rotten Fruits",
    packages = find_packages(),
    install_requires=install_requirements,
    entry_points = {
        "console_scripts": [
            "scrapbox2roamresearch=scrapbox2roamresearch.main:main",
        ]
    },
    classifiers = [
        'Programming Language :: Python :: 3.7',
    ]
)