from setuptools import setup

setup(
   name='simscaleparser',
   version='1.0',
   description='Trace reconstruction from logs',
   author='Harshil Gupta',
   author_email='harsh.ger@gmail.com',
   packages=['logparser'],  #same as name
   scripts=['run.sh']
)
