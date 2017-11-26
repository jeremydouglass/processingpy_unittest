import unittest
import sys

"""Simple unit testing for Processing.py sketches.

A single-tab simple unit testing solution for Processing.py.
Add groups of tests here organized in the unittest style:
Group test sets to be run simultaneously in classes that
extend unittest.TestCase. Group related tests as functions
named test_foo within TestCase classes.

Use `tests.run()` to auto-discover and run all tests.
Use `tests.run(TestFoo)` to run one specific test class.

"""
def run(case=None, out=sys.stdout):
    """Simple test runner.
    
    Call with case = a specific test set:
    the class name of a TestCase-derived class.
    When no case is provided, discovers and runs
    all tests in its own module (its own PDE tab).
    
    Default to normal console text (white text),
    set out=sys.stderr to print as error (red text).

    Args:
        case (TestCase): Tests to run.
        out  (stream file object): Where to write results.
        
    """    
    if case is not None:
        suite = unittest.TestLoader().loadTestsFromTestCase(case)
    else:
        # load all tests from this module
        suite = unittest.TestLoader().loadTestsFromModule(sys.modules[__name__])
    # run test suite
    unittest.TextTestRunner(stream=out, descriptions=True,
                            verbosity=2, failfast=False, buffer=False,
                            resultclass=None).run(suite)

# Example tests: these can be deleted and replaced.

class TestEqual(unittest.TestCase):
    """Simple example."""
    
    def test_47(self):
        self.assertEqual(47, 40 + 7)
        self.assertFalse(47 % 2 == 0)
        self.assertTrue(47 / 47 == 1)

class TestStringMethods(unittest.TestCase):
    """Example string tests from unittest documentation."""
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

class TestSkipping(unittest.TestCase):
    """Example skipping tests from unittest documentation.
    Modified to eliminate dependencies.
    """    
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(1 < (2, 4),
                     "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

if __name__ == '__main__':
    """Discover and run all tests on main entrypoint."""
    unittest.main(exit=False)
