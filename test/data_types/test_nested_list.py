import io
import unittest
from unittest.mock import patch
from src.data_types import nested_list


class NestedListOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        "5", "Harsh", "20", "Beria", "20", "Varun", "19", "Kakunami", "19", "Vikas", "21"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        nested_list.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "Beria\nHarsh")


if __name__ == '__main__':
    unittest.main()
