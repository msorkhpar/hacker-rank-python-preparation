import io
import unittest
from unittest.mock import patch
from src.introduction import arithmetic_operators


class ArithmeticOutputTest(unittest.TestCase):

    param_list = [
        ("3", "5", "8\n-2\n15"),
        ("3", "2", "5\n1\n6"),
        ("-3", "-2", "-5\n-1\n6")
    ]

    def test_evaluate_console_output(self):
        for n1, n2, expected in self.param_list:
            with self.subTest("ArithmeticOutputTest.test_evaluate_console_output", n1=n1, n2=n2):
                with patch('builtins.input', side_effect=[n1, n2]), \
                        patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                    arithmetic_operators.run()
                    self.assertEqual(mock_stdout.getvalue().strip(), expected)


if __name__ == '__main__':
    unittest.main()
