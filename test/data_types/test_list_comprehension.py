import io
import unittest
from unittest.mock import patch
from src.data_types import list_comprehension


class ListComprehensionOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["1", "1", "1", "2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        list_comprehension.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]")


if __name__ == '__main__':
    unittest.main()
