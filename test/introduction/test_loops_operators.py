import io
import unittest
from unittest.mock import patch
from src.introduction import loops_operators


class LoopsOutputTest(unittest.TestCase):
    functions = [
        loops_operators.run_with_for,
        loops_operators.run_with_while,
        loops_operators.run_with_lambda
    ]

    param_list = [
        ("3", "0\n1\n4"),
        ("4", "0\n1\n4\n9"),
        ("5", "0\n1\n4\n9\n16")
    ]

    def test_evaluate_console_output(self):
        for n, expected in self.param_list:
            for func in self.functions:
                with self.subTest("LoopsOutputTest.test_evaluate_console_output", func=func, n=n):
                    with patch('builtins.input', side_effect=[n]), \
                            patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
                        loops_operators.run(func)
                        self.assertEqual(mock_stdout.getvalue().strip(), expected)


if __name__ == '__main__':
    unittest.main()
