import io
import unittest
from unittest.mock import patch
from src.data_types import runner_up


class RunnerUpOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["5", "2 3 6 6 5"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        runner_up.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "5")

    @patch('builtins.input', side_effect=["5", "-7 -7 -7 -7 -6"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_negative_input_evaluate_console_output(self, mock_stdout, mock_input):
        runner_up.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "-7")


if __name__ == '__main__':
    unittest.main()
