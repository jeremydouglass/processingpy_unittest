import unittest

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
