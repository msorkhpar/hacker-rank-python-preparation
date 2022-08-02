import io
import unittest
from unittest.mock import patch
from src.regex_and_parsing import neo_and_matrix


class NeoAndMatrixOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        "7 3",
        "Tsi",
        "h%x",
        "i #",
        "sM ",
        "$a ",
        "#t%",
        "ir!"
    ])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        neo_and_matrix.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "This is Matrix#  %!")


if __name__ == '__main__':
    unittest.main()
