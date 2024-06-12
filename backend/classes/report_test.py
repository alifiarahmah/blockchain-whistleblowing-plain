import unittest

from Report import Report

class TestApp(unittest.TestCase):
    report = Report()
    def test_create_report(self):
        block = self.report.create_block(2, self.report.print_previous_block(), 'suspect_name2', 'dept2', 'action_category2', 'description2', 'location2', 'time_of_occurence2', 'evidence2')
        self.assertEqual(block['index'], 2)

    def test_display_reports(self):
        block = self.report.create_block(2, self.report.print_previous_block(), 'suspect_name2', 'dept2', 'action_category2', 'description2', 'location2', 'time_of_occurence2', 'evidence2')
        self.assertEqual(len(self.report.chain), 3)

    def test_valid(self):
        valid = self.report.chain_valid(self.report.chain)
        self.assertFalse(valid)

    def test_unvalid(self):
        self.report.chain[0]['proof'] = 34
        valid = self.report.chain_valid(self.report.chain)
        self.assertFalse(valid)

if __name__ == '__main__':
    unittest.main()