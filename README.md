# A unittest example for Processing.py

This is a single-file module and an example sketch to get [Processing.py](https://github.com/jdf/processing.py) users started with simple [unit testing](https://en.wikipedia.org/wiki/Unit_testing) and [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) (TDD) by adding a single `tests.py` file/tab.

Processing.py is Python Mode for Processing. It can be used to quickly wrap Python code together with the Processing Java API and distribute them as cross-platform sketches that run either as standalone apps or within the Processing IDE (PDE). Processing.py supports Python 2.7 running on the [Jython](http://www.jython.org/) 2.7 Python-on-Java interpreter. This includes the built-in [unittest Unit Testing Framework](https://docs.python.org/2/library/unittest.html). 

This sketch demonstrates how to create and organize groups of `unittest` tests and run them from a sketch, for example through `tests.run()`

## Getting Started

You can get started using unittest in Processing.py sketches by either:

-  downloading the example sketch and modifying it, or
-  adding the tests.py file to an existing Processing.py sketch
   and calling it with run() from the main sketch.

## Prerequisites

If not already installed, you must:

1. Download Processing 3.x  
2. In Processing, install Python Mode:  
   -  `Processing > Tools > Add Tool > Modes > Python Mode`

## Using the example sketch

1. Download or clone this repository.
2. Launch the example in Processing by double-clicking `using_unittest.pyde`
3. Modify `tests.py` to add tests.

## Adding to an existing sketch

1. Copy `tests.py` into the sketch folder,
   or create a new tab `tests.py` in PDE, and copy-paste the contents in.
2. Modify `tests.py` to add tests.
3. In the main sketch file/tab:
   -  add `import tests` to the header
   -  add `tests.run()` to `setup()` (or where appropriate)

## Versioning

This project uses [semantic versioning](http://semver.org/). For the versions available, see the tags on this repository.

## Authors

* [**Jeremy Douglass**](https://github.com/jeremydouglass) - *Initial work*

## Acknowledgments

* [Jonathan Feinberg](https://github.com/jdf)
* [Marco Piccolino](https://github.com/marco-piccolino)
