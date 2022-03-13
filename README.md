
# Number Theory 

This project has problems from [project euler](https://projecteuler.net/archives), as well as random snippits from my computational number theory class. 

## Structure 
The Project structure was forked from [The Hitchhikers Guide to Packaging](https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/quickstart.html).

## How to Run (For me)
Most of this is from [here](https://packaging.python.org/en/latest/tutorials/installing-packages/#installing-requirements) and also [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
1. Create a virutalenv, which I called number_theory, and then run it with the

```
virtualenv number_theory 
source number_theory/bin/activate

# creates a list of packages in requirements.txt
pip freeze --local > requirements.txt
```

2. Run a terminal in the number_theory directory, and test code using the following

```
python -m unittest tests.test_basic
```

Note: test_basic is an example of a test module, you can replace it with any test file in /tests/

