import io
import unittest
from unittest.mock import patch
from src.collections import word_order


class WordOrderOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["4", "bcdef", "abcdefg", "bcde", "bcdef"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        word_order.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "3\n2 1 1")


if __name__ == '__main__':
    unittest.main()
