from setuptools import setup, find_packages

setup(
    name='quamtun',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'wheel',
    ],
    entry_points={
        'console_scripts': [
            'mycommand=mypackage.command_line:main',
        ],
    },
)
