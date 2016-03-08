from setuptools import setup

setup(
    name='shortenurl21',
    version='0.1',
    py_modules=['shortenurl21'],
        install_requires=[
            'Click',
    ],
    entry_points='''
        [console_scripts]
        shortenurl21=shortenurl21:cli
    ''',
)