from setuptools import setup

setup(
    name = 'wadget',
    version = '0.0.9',
    license = 'MIT License',
    description = 'A multi-platform CLI /idgames client for downloading Doom addons quickly.',
    long_description = open('README.md').read(),
    long_description_content_type='text/markdown',
    author = 'Avery Ross',
    packages = ['wadget'],
    entry_points = {
        'console_scripts': [
            'wadget = wadget.__main__:main'
        ]
    },
    install_requires=['requests', 'clint'])
