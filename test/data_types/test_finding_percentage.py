import io
import unittest
from unittest.mock import patch
from src.data_types import finding_percentage


class FindingPercentageOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=["3", "Krishna 67 68 69", "Arjun 70 98 63", "Malika 52 56 60", "Malika"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        finding_percentage.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "56.00")


if __name__ == '__main__':
    unittest.main()
