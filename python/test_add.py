import unittest

# Function to be tested
def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):
    def test_add(self):
        # Table of test cases: each tuple contains (input1, input2, expected_output)
        test_cases = [
            (1, 2, 3),
            (10, 20, 30),
            (-1, -1, -2),
            (0, 0, 0),
            (100, -50, 50)
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b, expected=expected):
                self.assertEqual(add(a, b), expected)

if __name__ == '__main__':
    unittest.main()
