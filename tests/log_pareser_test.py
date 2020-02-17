import unittest
from logparser import log_parser as lp

class log_parser_test_case(unittest.TestCase):
    def setUp(self):
        self.log_parser = lp.log_parser()

    def test_malformed_input(self):
        output, error = self.log_parser.process_log_entry("dgsaf", True)
        self.assertIn("Malformed Input: dgsaf", error)
        self.assertListEqual([], output)

    def test_json_output(self):
        output, error = self.log_parser.process_log_entry("2016-10-20T12:43:32.000Z 2016-10-20T12:43:42.000Z trace1 front-end null->aa", True)
        self.assertListEqual([], error)
        self.assertEqual(1, len(output))
        self.assertIn("\"id\": \"trace1\"", output[0])
        self.assertIn("\"service\": \"front-end\"", output[0])
        self.assertIn("\"start\": \"2016-10-20T12:43:32.000Z\"", output[0])
        self.assertIn("\"end\": \"2016-10-20T12:43:42.000Z\"", output[0])
        self.assertIn("\"calls\": []", output[0])
        self.assertIn("\"span\": \"aa\"", output[0])

    def test_incomplete_trace(self):
        output, error = self.log_parser.process_log_entry("2016-10-20T12:43:33.000Z 2016-10-20T12:43:36.000Z trace1 back-end-1 aa->ac", True)
        self.assertIn("Discarding Trace: trace1", error)
        self.assertListEqual([], output)

    def test_json_output_multiple_calls(self):
        self.log_parser.process_log_entry("2016-10-20T12:43:33.000Z 2016-10-20T12:43:36.000Z trace1 back-end-1 aa->ac", False)
        self.log_parser.process_log_entry("2016-10-20T12:43:34.000Z 2016-10-20T12:43:35.000Z trace1 back-end-3 ac->ad", False)
        self.log_parser.process_log_entry("2016-10-20T12:43:38.000Z 2016-10-20T12:43:40.000Z trace1 back-end-2 aa->ab", False)
        output, error = self.log_parser.process_log_entry("2016-10-20T12:43:32.000Z 2016-10-20T12:43:42.000Z trace1 front-end null->aa", True)

        self.assertListEqual([], error)
        self.assertEqual(1, len(output))
        self.assertIn("\"id\": \"trace1\"", output[0])
        self.assertIn("\"calls\": [\n            {\n                \"start\": \"2016-10-20T12:43:33.000Z\",\n", output[0])

if __name__ == '__main__':
    unittest.main()
