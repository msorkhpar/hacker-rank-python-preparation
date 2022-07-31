import io
import unittest
from unittest.mock import patch
from src.regex_and_parsing import email_validator


class PhoneNumberValidatorOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["2", "DEXTER <dexter@hotmail.com>", "VIRUS <virus!@variable.:p>"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        email_validator.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "DEXTER <dexter@hotmail.com>")


if __name__ == '__main__':
    unittest.main()
