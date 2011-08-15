import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "MercuryFein",
    version = "0.0.1",
    author = "Leon van der Ree",
    author_email = "leon@fun4me.demon.nl",
    description = ("MercuryFein is a FeinCMS extension that provides the Mercury Editor to edit your richtText content"),
    long_description=read('README'),
    license = "BSD",
    keywords = "Mercury Editor FeinCMS richtext",
    url = "http://packages.python.org/mercury_fein",

    requires=[
        'FeinCMS (>=1.3.0)',
    ],
    packages=[
        'mercury'
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
