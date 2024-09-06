# setup.py
import io

from setuptools import setup, find_packages

with io.open("README.md", encoding="utf-8") as fileObj:
    long_description = fileObj.read()

setup(
    name='terminal_input',
    version='0.1',
    author="Mahmoud Raouf",
    author_email="mahmoud.raouf21@gmail.com",
    description="provides secure displays **** for password input for both Windows and Unix-like systems.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT",
    install_requires=[],
    packages=find_packages(where="terminal_input"),
    package_dir={"": "terminal_input"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'termipass=terminal_input.termipass:main'
        ]
    }
)
