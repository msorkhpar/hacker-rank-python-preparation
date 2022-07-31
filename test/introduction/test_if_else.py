import io
import unittest
from unittest.mock import patch
from src.introduction import if_else


class IfElseOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["3"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_odd_number_is_weird(self, mock_stdout, mock_input):
        if_else.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "Weird")

    @patch('builtins.input', side_effect=["2"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_between_2_and_5_even_number_is_not_weird(self, mock_stdout, mock_input):
        if_else.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "Not Weird")

    @patch('builtins.input', side_effect=["20"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_between_6_and_20_even_number_is_weird(self, mock_stdout, mock_input):
        if_else.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "Weird")

    @patch('builtins.input', side_effect=["222"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_even_number_greater_than_20_is_not_weird(self, mock_stdout, mock_input):
        if_else.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "Not Weird")


if __name__ == '__main__':
    unittest.main()
