#!/usr/bin/python3

import unittest
import json
import csv
import pep8

from models.base import Base

class TestBase(unittest.TestCase):
    """Unittest for base class"""
    def test_ida(self):
        bas1 = Base()
        bas2 = Base()
        bas3 = Base(100)

        self.assertEqual(bas1.id, 1)
        self.assertEqual(bas2.id, 2)
        self.assertEqual(bas3.id, 100)

    def test_2_json_empty(self):
        """
        Test for json to string when list is empty
        
        """
        outcome = Base.to_json_string([])
        self.assertEqual(outcome, "[]")

    def test_2_json_none(self):
        """
        Test for json to string when list is none
        
        """
        outcome = Base.to_json_string(None)
        self.assertEqual(outcome, "[]")

    def test_2_json_string_list(self):
        """
        Test for json to string when list is not empty
        
        """
        list_dictionaries = [{"id": 1, "name": "Baby_Sekuru"}, {"id": 2, "name": "Alek_Mamu"}]
        exQ = '[{"id": 1, "name": "Baby_Sekuru"}, {"id": 2, "name": "Alek_Mamu"}]'
        outcome = Base.to_json_string(list_dictionaries)
        self.assertEqual(outcome, exQ)

    def test_save_2_fl(self):
        """
        Test to save to file.
        
        """
        list_objs = []
        ex_fln = "Rectangle.json"
        ex_jstr = "[]"

        Base.save_to_file(list_objs)

        with open(ex_fln, "r") as fl:
            act_jstr = fl.read()

        self.assertEqual(act_jstr, ex_jstr)

        list_objs = [Base(1), Base(2)]
        ex_fln = "Base.json"
        ex_jstr = '[{"id": 1}, {"id": 2}]'

        Base.save_to_file(list_objs)

        with open(ex_fln, "r") as fl:
            act_jstr = fl.read()

        self.assertEqual(act_jstr, ex_jstr)

    def test_from_js_str(self):
        """
        Test for from js to str.
        
        """
        jstr = None
        exQ = []
        self.assertEqual(Base.from_json_string(jstr), exQ)

        jstr = ""
        exQ = []
        self.assertEqual(Base.from_json_string(jstr), exQ)

        jstr = '[{"id": 1}, {"id": 2}]'
        exQ = [{"id": 1}, {"id": 2}]
        self.assertEqual(Base.from_json_string(jstr), exQ)

        

    def test_pep8_con(self):
        """
        Test for pep8 guidelines
        
        """
        pep8sty = pep8.StyleGuide(quiet=True)
        outcome = pep8sty.check_files(['models/base.py'])
        self.assertEqual(outcome.total_errors, 0)

if __name__ == '__main__':
        unittest.main()
