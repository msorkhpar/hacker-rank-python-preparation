import io
import unittest
from unittest.mock import patch
from src.introduction import leap_year


class LeapYearOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["1990"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_not_multiple_of_4(self, mock_stdout, mock_input):
        leap_year.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "False")

    @patch('builtins.input', side_effect=["2000"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_multiple_of_4_and_400(self, mock_stdout, mock_input):
        leap_year.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "True")

    @patch('builtins.input', side_effect=["2100"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_multiple_of_4_and_100_but_not_400(self, mock_stdout, mock_input):
        leap_year.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "False")

    @patch('builtins.input', side_effect=["2004"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_multiple_of_4_but_not_100(self, mock_stdout, mock_input):
        leap_year.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "True")


if __name__ == '__main__':
    unittest.main()
