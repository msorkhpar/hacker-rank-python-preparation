import io
import unittest
from unittest.mock import patch
from src.regex_and_parsing import phone_validator


class PhoneNumberValidatorOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["5", "9587456281", "1252478965", "9587456281s", "95874562", "s95874562"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        phone_validator.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "YES\nNO\nNO\nNO\nNO")

    def test_is_valid_returns_true_when_given_input_is_valid(self):
        self.assertIsNotNone(phone_validator.is_valid("9587456281"))

    def test_is_valid_returns_false_when_input_is_too_short(self):
        self.assertIsNone(phone_validator.is_valid("9576281"))

    def test_is_valid_returns_false_when_input_is_too_long(self):
        self.assertIsNone(phone_validator.is_valid("9587456281s"))

    def test_is_valid_returns_false_when_input_not_start_with_7_8_9(self):
        self.assertIsNone(phone_validator.is_valid("1252478965"))


if __name__ == '__main__':
    unittest.main()
