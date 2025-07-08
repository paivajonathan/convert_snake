from setuptools import setup, find_packages

setup(
    name='convert_snake',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'convert_snake=convert_snake.cli:main',
        ],
    },
)
