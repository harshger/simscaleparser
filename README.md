# Simscale Log Parser

Trace reconstruction from logs

## Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites
Linux and python3

### Installing
python setup.py install

This allows you to easily install Python packages required to run the project.
When we install the package, setuptools will copy the script "run.sh" to our PATH and make it available for general use.:

$ run.sh

### Test
For running the tests you can use the following command.
python setup.py test

### Evaluator
To be used with evaluator, run the following command from the bin directory.
./traces-evaluator run.sh
