import unittest

class TestClass(unittest.TestCase):

    def _test(self):
        # GIVEN
        # WHEN
        # THEN

    def test_one(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_two(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_three(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

