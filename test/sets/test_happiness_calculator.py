import io
import unittest
from unittest.mock import patch
from src.sets import happiness_calculator


class HappinessCalculatorOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["3 2", "1 5 3", "3 1", "5 7"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        happiness_calculator.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "1")


if __name__ == '__main__':
    unittest.main()
