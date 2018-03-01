# from distutils.core import setup
from setuptools import setup, find_packages

setup(name='Triss',
	version='0.2.0a',
	description='A sample Python project \|for quick commands',
	author='Leo',
	license='MIT',
	packages=find_packages(),
	entry_points={
        'console_scripts': [
            'Triss4 = Triss.Triss:run',
        ]
    },
)
