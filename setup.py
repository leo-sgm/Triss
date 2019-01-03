# from distutils.core import setup
from setuptools import find_packages, setup

setup(name='Triss',
      version='0.2.1a',
      description='A sample Python project | for quick access to scripts | ',
      author='Leo',
      license='MIT',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'Triss = Triss.Triss:run',
          ]
      })
