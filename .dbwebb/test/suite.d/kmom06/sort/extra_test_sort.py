#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
import os
import random
import sys
from io import StringIO
from unittest.mock import patch
from unittest import TextTestRunner
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import import_module, find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

# Path to file and basename of the file to import
list = import_module(REPO_PATH, 'src/unorderedlist')
sort = import_module(REPO_PATH, 'src/sort')
Handler = import_module(REPO_PATH, 'main').Handler

class Test4SortExtra(ExamTestCase):
    """
    Testing the class List.
    """

    def setUp(self):
        self.int_ulist = list.UnorderedList()
        self.int_ulist.append(3)
        self.int_ulist.append(5)
        self.int_ulist.append(111)
        self.int_ulist.append(1)
        self.int_ulist.append(34)
        self.int_ulist.append(0)
        self.int_ulist.append(11)
        self.int_list = [3, 5, 111, 1, 34, 0, 11]

    @tags("sort", "bubble")
    def test_a_bubble_int(self):
        """
        recursive_bubble
        Testar att sorterar en lista med heltal.
        Förväntar att följande lista är korrekt sorterad:
        {arguments}
        Förväntar värdet på en position:
        {correct}
        Fick istället följande värde på den positionen:
        {student}
        """
        self._argument = self.int_list
        sort.recursive_bubble(self.int_ulist)
        sorted_list = sorted(self.int_list)
        for i in range(len(self.int_list)):
            self.assertEqual(self.int_ulist.get(i), sorted_list[i])


    def check_print_contain(self, inp, correct=None):
        """
        One function for testing print input functions.
        """
        with patch("builtins.input", side_effect=inp):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                h = Handler()
                try:
                    h.main()
                except SystemExit:
                    pass
                str_data = fake_out.getvalue()
                if correct is not None:
                    for val in correct:
                        self.assertIn(val, str_data)
                return h

    @tags("menu", "12")
    def test_b_bubble_menu(self):
        """
        Testar lägga till flera värden med menyval 1 och sorterar med menyval 12.
        Använder följande som input:
        {arguments}
        Förväntar att följande värde finns i listan på korrekt index:
        {correct}
        Innehöll:
        {student}
        """
        self.norepr = True
        self._multi_arguments  = ["1", "12", "continue", "1", "10", "continue", "1", "19", "continue", "1", "22", "continue", "12", "continue", "q"]
        h = self.check_print_contain(self._multi_arguments)
        self.assertEqual(str(h.list.get(0)), "10")
        self.assertEqual(str(h.list.get(1)), "12")
        self.assertEqual(str(h.list.get(2)), "19")
        self.assertEqual(str(h.list.get(3)), "22")

    @tags("sort", "insertion")
    def test_c_insertion_mix_types(self):
        """
        insertion_sort
        Testar att sorterar en lista med heltal och strängar. Kollar att heltal och strängar sorteras för sig.
        Förväntar att följande lista är korrekt sorterad:
        {arguments}
        Förväntar värdet på en position:
        {correct}
        Fick istället följande värde på den positionen:
        {student}
        """
        ulist = list.UnorderedList()
        [3, "b", 1, "a", 2]
        ulist.append(3)
        ulist.append("b")
        ulist.append(1)
        ulist.append("a")
        ulist.append(2)
        ulist.append("d")
        as_list = [3, "b", 1, "a", 2]

        self._argument = as_list
        sort.insertion_sort(ulist)
        sorted_list = [1, 2, 3, "a", "b", "d"]
        for i in range(len(as_list)):
            self.assertEqual(ulist.get(i), sorted_list[i])


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
