from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='restgios',
    version='0.1',
    description='Serve Nagios status file as a json resource',
    long_description=long_description,
    url='',
    author='Leonardo',
    author_email='leofiore@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),

    install_requires=[
        'inotify-simple==1.1.7',
        'tornado'
    ],


    entry_points={
        'console_scripts': [
            'restgios=restgios:main',
        ],
    },
)
