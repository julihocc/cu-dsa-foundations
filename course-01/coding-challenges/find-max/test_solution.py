import unittest
try:
    from solution import find_max
except ImportError:
    # Allow tests to be discovered even if solution.py is empty or missing function
    find_max = None

class TestFindMax(unittest.TestCase):
    def setUp(self):
        if find_max is None:
            self.skipTest("find_max function not found in solution.py")

    def test_positive_list(self):
        """Test with a list of positive integers."""
        self.assertEqual(find_max([1, 5, 3, 9, 2]), 9)
        
    def test_negative_list(self):
        """Test with a list of negative integers."""
        self.assertEqual(find_max([-10, -5, -2, -8]), -2)
        
    def test_mixed_list(self):
        """Test with a list of mixed positive and negative integers."""
        self.assertEqual(find_max([-10, 5, 0, -20]), 5)
        
    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(find_max([42]), 42)
        
    def test_duplicate_max(self):
        """Test with a list containing duplicate maximum values."""
        self.assertEqual(find_max([1, 5, 5, 3]), 5)
        
    def test_empty_list(self):
        """Test with an empty list. Should return None."""
        self.assertIsNone(find_max([]))

if __name__ == '__main__':
    unittest.main()
