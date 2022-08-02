import io
import unittest
from unittest.mock import patch
from src.sets import union


class UnionMethodOfSetOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["9", "1 2 3 4 5 6 7 8 9", "9", "10 1 2 3 11 21 55 6 8", ])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        union.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "13")


if __name__ == '__main__':
    unittest.main()
