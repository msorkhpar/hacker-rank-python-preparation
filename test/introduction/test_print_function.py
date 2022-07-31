import io
import unittest
from unittest.mock import patch
from src.introduction import print_function


class PrintFunctionOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["5"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        print_function.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "12345")


if __name__ == '__main__':
    unittest.main()
