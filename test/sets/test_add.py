import io
import unittest
from unittest.mock import patch
from src.sets import add


class AddMethodOfSetOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["7", "UK", "China", "USA", "France", "New Zealand", "UK", "France"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        add.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "5")


if __name__ == '__main__':
    unittest.main()
