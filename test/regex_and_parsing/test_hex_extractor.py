import io
import unittest
from unittest.mock import patch
from src.regex_and_parsing import hex_color_extractor


class HexColorExtractorOutputTest(unittest.TestCase):

    @patch('builtins.input', side_effect=[
        "11",
        "#BED",
        "{",
        "    color: #FfFdF8; background-color:#aef;",
        "    font-size: 123px;",
        "    background: -webkit-linear-gradient(top, #f9f9f9, #fff);",
        "}",
        "#Cab",
        "{",
        "    background-color: #ABC;",
        "    border: 2px dashed #fff;",
        "}"
    ])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evaluate_console_output(self, mock_stdout, mock_input):
        hex_color_extractor.run()
        self.assertEqual(mock_stdout.getvalue().strip(), "#FfFdF8\n#aef\n#f9f9f9\n#fff\n#ABC\n#fff")

    def test_selector_should_not_be_marked_as_hex_color(self):
        result = hex_color_extractor.extract_hex_codes(["#aaa"])
        self.assertListEqual(result, [])

    def test_hex_color_connected_without_spaces_to_css_attribute(self):
        result = hex_color_extractor.extract_hex_codes(["background-color:#aaaaaa"])
        self.assertListEqual(result, ["#aaaaaa"])

    def test_multiple_hex_colors_in_a_line(self):
        result = hex_color_extractor.extract_hex_codes(["background: -webkit-linear-gradient(top, #f9f9f9, #fff);"])
        self.assertListEqual(result, ["#f9f9f9", "#fff"])

    def test_wrong_size_hex_colors_in_a_line_should_not_be_extracted(self):
        result = hex_color_extractor.extract_hex_codes(["background-color:#abcd"])
        self.assertListEqual(result, [])


if __name__ == '__main__':
    unittest.main()
