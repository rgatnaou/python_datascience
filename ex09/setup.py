# setup.py
from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    test_suite='nose.collector',
    tests_require=['nose'],
    author="Your Name",
    author_email="your.email@example.com",
    description="A brief description of your package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
