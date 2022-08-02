import io
import unittest
from unittest.mock import patch
from src.sets import remove_pop_discard


class RemovePopAndDiscardMethodsOfSetOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["9", "1 2 3 4 5 6 7 8 9", "10",
                                          "pop", "remove 9", "discard 9", "discard 8", "remove 7", "pop", "discard 6",
                                          "remove 5", "pop", "discard 5"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        remove_pop_discard.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "4")


if __name__ == '__main__':
    unittest.main()
