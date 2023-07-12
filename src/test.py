import unittest
from app import rnd, max_num_in_list

class TestApp(unittest.TestCase):
    def test_rnd_correct_value(self):
        """Test if rnd returns a value within the expected range."""
        start = 2
        end = 20
        result = rnd(start, end)
        self.assertIn(result, range(start, end+1))
        # Note: Testing a randomized function like rnd with a fixed expected range may pass or fail by chance.
        # The test should be run multiple times to observe the behavior and ensure consistency.

    def test_rnd_no_out_of_range_value(self):
        """Test if rnd does not return an out-of-range value."""
        start = 2
        end = 20
        result = rnd(start, end)
        self.assertGreaterEqual(result, start)
        self.assertLessEqual(result, end)
        # Note: Testing a randomized function like rnd can only increase the likelihood of correct behavior, but doesn't guarantee it.
        # The test should be run multiple times to observe the behavior and ensure the generated values are within the expected range.

    def test_max_num_in_list(self):
        """Test if max_num_in_list returns the greatest number in the list."""
        numbers = [2, 6, 8, 7, -1]
        result = max_num_in_list(numbers)
        self.assertEqual(result, 8)

if __name__ == '__main__':
    unittest.main()
