import io
import unittest
from unittest.mock import patch
from src.introduction import division_operator


class DivisionOutputTest(unittest.TestCase):

    param_list = [
        ("3", "5", "0\n0.6"),
        ("4", "3", "1\n1.3333333333")
    ]

    def test_evaluate_console_output(self):
        for n1, n2, expected in self.param_list:
            with self.subTest("DivisionOutputTest.test_evaluate_console_output", n1=n1, n2=n2):
                with patch('builtins.input', side_effect=[n1, n2]), \
                        patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                    division_operator.run()
                    self.assertEqual(mock_stdout.getvalue().strip(), expected)


if __name__ == '__main__':
    unittest.main()
