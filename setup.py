from setuptools import setup

setup(
    name = 'wadget',
    version = '0.0.5',
    packages = ['wadget'],
    entry_points = {
        'console_scripts': [
            'wadget = wadget.__main__:main'
        ]
    },
    install_requires=['requests'])
