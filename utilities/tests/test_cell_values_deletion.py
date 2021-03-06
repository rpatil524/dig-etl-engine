# -*- coding: utf-8 -*-
import unittest
import sys, os
import json

sys.path.insert(0, '../')

from data_import.dig_tabular_import import TabularImport


class TestDeleteCellValues(unittest.TestCase):
    def setUp(self):
        self.csv_file = os.path.join(os.path.dirname(__file__), "./test_data/delete_cell_input.csv")

    def test_decode_cell(self):
        mapping_spec = {
            "prefix": "testdecode",
            "website": "http://testdecode.isi",
            "file_url": "https://testdecode.isi/1",
            "id_path": "",
            "remove_leading_trailing_whitespace": True,
            "remove_blank_fields": True,
            "config": {
                "title": "{A}: decode test  in {C}",
                "type": [
                    "Event",
                    "Decode Test"
                ],
                "rules": [
                    {
                        "path": "B 1",
                        "field": "decoded",
                        "delete": "delete"
                    }
                ]
            }
        }
        ti = TabularImport(self.csv_file, mapping_spec)
        objs = ti.object_list
        self.assertTrue('B 1' not in objs[3])
        self.assertTrue('B 1' not in objs[4])


if __name__ == '__main__':
    unittest.main()
