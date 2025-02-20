"""
Flask-Ask
-------------

Easy Alexa Skills Kit integration for Flask
"""
from setuptools import setup

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]

setup(
    name='Flask-Ask',
    version='0.9.9',
    author='Animesh Kundu',
    description='Rapid Alexa Skills Kit Development for Amazon Echo Devices in Python',
    packages=['flask_ask'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=parse_requirements('requirements.txt'),
)
