#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
import os
import random
import sys
from io import StringIO
from abc import ABC
from unittest.mock import patch
from unittest import TextTestRunner
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import import_module, find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)

# Path to file and basename of the file to import
die = import_module(REPO_PATH, 'src/die')
hand = import_module(REPO_PATH, 'src/hand')
rules = import_module(REPO_PATH, 'src/rules')

class Test3Rule(ExamTestCase):
    """
    Testing the class Rule.
    """
    @tags("rules")
    def test_rule_is_abc(self):
        """
        Testar att Rule är en abstrakt klass.
        Förväntar att `issubclass(Rule, ABC)` returnerar:
        {correct}
        Fick följande:
        {student}
        """
        # pass
        self.assertTrue(issubclass(rules.Rule, ABC))

    @tags("rules")
    def test_rule_has_points(self):
        """
        Testar att Rule har en abstrakt metod som heter points.
        Förväntar att True returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.assertTrue(hasattr(rules.Rule, "points"))


class Test4SameValueRule(ExamTestCase):
    """
    Testing the class SameValueRule.
    """
    def setUp(self):
        random.seed("yahtzee")
        self.hand = hand.Hand()

    @tags("rules", "SameValueRule")
    def test_points(self):
        """
        Testar att point returnerar rätt värde.
        Instansierar SameValueRule med argumenten 1 och "1".
        Förväntar att 2 returneras med Hand, [1, 3, 1, 4, 6]:
        Fick följande:
        {student}
        """
        rule = rules.SameValueRule(1, "1")
        self.hand = hand.Hand([1, 3, 1, 4, 6])
        self.assertEqual(rule.points(self.hand), 1*2)

    @tags("rules", "SameValueRule")
    def test_points_missing_value(self):
        """
        Testar att point returnerar rätt värde när inga tärningar har rätt värde.
        Instansierar SameValueRule med argumenten 2 och "2".
        Förväntar att 0 returneras med handen [1, 3, 1, 4, 6]:
        Fick följande:
        {student}
        """
        rule = rules.SameValueRule(2, "2")
        self.hand = hand.Hand([1, 3, 1, 4, 6])
        self.assertEqual(rule.points(self.hand), 2*0)

    @tags("rules", "SameValueRule")
    def test_has_name(self):
        """
        Testar att SameValueRule har attributet name.
        Instansierar SameValueRule med argumenten 2 och "two".
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.SameValueRule(2, "two")
        self.assertEqual(rule.name, "two")



class Test5Ones(ExamTestCase):
    """
    Testing the class Ones.
    """
    @tags("rules", "Ones")
    def test_ones_points(self):
        """
        Testar att points() hos ett Ones objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 3, 1, 4, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.ones = rules.Ones()
        self.hand = hand.Hand([1, 3, 1, 4, 6])
        self.assertEqual(self.ones.points(self.hand), 1*2)


    @tags("rules", "Ones")
    def test_has_name(self):
        """
        Testar att ett Ones objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.Ones()
        self.assertEqual(rule.name, "Ones")


class Test5Twos(ExamTestCase):
    """
    Testing the class Twos.
    """
    @tags("rules", "Twos")
    def test_twos_points(self):
        """
        Testar att points() hos ett Twos objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 2, 1, 2, 2]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.twos = rules.Twos()
        self.hand = hand.Hand([1, 2, 1, 2, 2])
        self.assertEqual(self.twos.points(self.hand), 2*3)

    @tags("rules", "Twos")
    def test_has_name(self):
        """
        Testar att ett Twos objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.Twos()
        self.assertEqual(rule.name, "Twos")

class Test5Threes(ExamTestCase):
    """
    Testing the class Threes.
    """
    @tags("rules", "Threes")
    def test_threes_points(self):
        """
        Testar att points() hos ett Threes objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 3, 1, 4, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.threes = rules.Threes()
        self.hand = hand.Hand([1, 3, 1, 4, 6])
        self.assertEqual(self.threes.points(self.hand), 3*1)

    @tags("rules", "Threes")
    def test_has_name(self):
        """
        Testar att ett Threes objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.Threes()
        self.assertEqual(rule.name, "Threes")


class Test5Fours(ExamTestCase):
    """
    Testing the class Fours.
    """
    @tags("rules", "Fours")
    def test_fours_points(self):
        """
        Testar att points() hos ett Fours objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 3, 1, 4, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.fours = rules.Fours()
        self.hand = hand.Hand([1, 3, 1, 4, 6])
        self.assertEqual(self.fours.points(self.hand), 4*1)


    @tags("rules", "Fours")
    def test_fours_no_points(self):
        """
        Testar att points() hos ett Fours objekt returnerar rätt antal poäng när det inte finns några fyror i handen.
        Använder en Hand med följande tärningar som argument.
        [1, 3, 1, 2, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.fours = rules.Fours()
        self.hand = hand.Hand([1, 3, 1, 2, 6])
        self.assertEqual(self.fours.points(self.hand), 0)


    @tags("rules", "Fours")
    def test_has_name(self):
        """
        Testar att ett Fours objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.Fours()
        self.assertEqual(rule.name, "Fours")

class Test5Fives(ExamTestCase):
    """
    Testing the class Fives.
    """
    @tags("rules", "Fives")
    def test_fives_points(self):
        """
        Testar att points() hos ett Fives objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [5, 5, 1, 4, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.fives = rules.Fives()
        self.hand = hand.Hand([5, 5, 1, 4, 6])
        self.assertEqual(self.fives.points(self.hand), 5*2)

    @tags("rules", "Fives")
    def test_has_name(self):
        """
        Testar att ett Fives objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.Fives()
        self.assertEqual(rule.name, "Fives")


class Test5Sixes(ExamTestCase):
    """
    Testing the class Sixes.
    """
    @tags("rules", "Sixes")
    def test_sixes_points(self):
        """
        Testar att points() hos ett Sixes objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 3, 6, 6, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.sixes = rules.Sixes()
        self.hand = hand.Hand([1, 3, 6, 6, 6])
        self.assertEqual(self.sixes.points(self.hand), 6*3)

    @tags("rules", "Sixes")
    def test_sixes_no_points(self):
        """
        Testar att points() hos ett Sixes objekt returnerar rätt antal poäng när det inte finns några sexor.
        Använder en Hand med följande tärningar som argument.
        [1, 3, 2, 2, 3]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.sixes = rules.Sixes()
        self.hand = hand.Hand([1, 3, 2, 2, 3])
        self.assertEqual(self.sixes.points(self.hand), 0)

    @tags("rules", "Sixes")
    def test_has_name(self):
        """
        Testar att ett Sixes objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.Sixes()
        self.assertEqual(rule.name, "Sixes")


class Test6ThreeOfAKind(ExamTestCase):
    """
    Testing the class TestThreeOfAKind.
    """
    @tags("rules", "ThreeOfAKind")
    def test_three_of_a_kind_points(self):
        """
        Testar att points() hos ett ThreeOfAKind objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [6, 3, 6, 1, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.ThreeOfAKind()
        self.hand = hand.Hand([6, 3, 6, 1, 6])
        self.assertEqual(self.a_rule.points(self.hand), 22)

    @tags("rules", "ThreeOfAKind")
    def test_three_of_a_kind_points_all_the_same(self):
        """
        Testar att points() hos ett ThreeOfAKind objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [6, 6, 6, 6, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.ThreeOfAKind()
        self.hand = hand.Hand([6, 6, 6, 6, 6])
        self.assertEqual(self.a_rule.points(self.hand), 30)

    @tags("rules", "ThreeOfAKind")
    def test_has_name(self):
        """
        Testar att ett ThreeOfAKind objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.ThreeOfAKind()
        self.assertEqual(rule.name, "Three Of A Kind")

class Test6FourOfAKind(ExamTestCase):
    """
    Testing the class TestFourOfAKind.
    """
    @tags("rules", "FourOfAKind")
    def test_four_of_a_kind_points(self):
        """
        Testar att points() hos ett FourOfAKind objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [6, 6, 6, 1, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.FourOfAKind()
        self.hand = hand.Hand([6, 6, 6, 1, 6])
        self.assertEqual(self.a_rule.points(self.hand), 6*4+1)

    @tags("rules", "FourOfAKind")
    def test_four_of_a_kind_points_all_the_same(self):
        """
        Testar att points() hos ett FourOfAKind objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [6, 6, 6, 6, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.FourOfAKind()
        self.hand = hand.Hand([6, 6, 6, 6, 6])
        self.assertEqual(self.a_rule.points(self.hand), 6*5)

    @tags("rules", "FourOfAKind")
    def test_four_of_a_kind_points_none_same(self):
        """
        Testar att points() hos ett FourOfAKind objekt returnerar rätt antal poäng när inga tärningar är lika.
        Använder en Hand med följande tärningar som argument.
        [1, 2, 3, 4, 5]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.FourOfAKind()
        self.hand = hand.Hand([1, 2, 3, 4, 5])
        self.assertEqual(self.a_rule.points(self.hand), 0)

    @tags("rules", "FourOfAKind")
    def test_has_name(self):
        """
        Testar att ett FourOfAKind objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.FourOfAKind()
        self.assertEqual(rule.name, "Four Of A Kind")

class Test7FullHouse(ExamTestCase):
    """
    Testing the class FullHouse.
    """
    @tags("rules", "FullHouse")
    def test_full_house_points(self):
        """
        Testar att points() hos ett FullHouse objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [6, 1, 6, 1, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.FullHouse()
        self.hand = hand.Hand([6, 1, 6, 1, 6])
        self.assertEqual(self.a_rule.points(self.hand), 25)

    @tags("rules", "FullHouse")
    def test_full_house_points_none(self):
        """
        Testar att points() hos ett FullHouse objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 1, 5, 6, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.FullHouse()
        self.hand = hand.Hand([1, 1, 5, 6, 6])
        self.assertEqual(self.a_rule.points(self.hand), 0)

    @tags("rules", "FullHouse")
    def test_has_name(self):
        """
        Testar att ett FullHouse objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.FullHouse()
        self.assertEqual(rule.name, "Full House")

class Test8Yahtzee(ExamTestCase):
    """
    Testing the class Yahtzee.
    """
    @tags("rules", "Yahtzee")
    def test_yahtzee_points(self):
        """
        Testar att points() hos ett Yahtzee objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 1, 1, 1, 1]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.Yahtzee()
        self.hand = hand.Hand([1, 1, 1, 1, 1])
        self.assertEqual(self.a_rule.points(self.hand), 50)

    @tags("rules", "Yahtzee")
    def test_yahtzee_points_none(self):
        """
        Testar att points() hos ett Yahtzee objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 1, 1, 1, 6]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.Yahtzee()
        self.hand = hand.Hand([1, 1, 1, 1, 6])
        self.assertEqual(self.a_rule.points(self.hand), 0)


    @tags("rules", "Yahtzee")
    def test_has_name(self):
        """
        Testar att ett Yahtzee objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.Yahtzee()
        self.assertEqual(rule.name, "Yahtzee")

class Test8Chance(ExamTestCase):
    """
    Testing the class Chance.
    """
    @tags("rules", "Chance")
    def test_chance_points(self):
        """
        Testar att points() hos ett Chance objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 4, 1, 6, 5]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.Chance()
        self.hand = hand.Hand([1, 4, 1, 6, 5])
        self.assertEqual(self.a_rule.points(self.hand), 17)


    @tags("rules", "Chance")
    def test_has_name(self):
        """
        Testar att ett Chance objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.Chance()
        self.assertEqual(rule.name, "Chance")


class Test9SmallStraight(ExamTestCase):
    """
    Testing the class SmallStraight.
    """
    @tags("rules", "SmallStraight")
    def test_small_straight_points_end(self):
        """
        Testar att points() hos ett SmallStraight objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 3, 6, 4, 5]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.SmallStraight()
        self.hand = hand.Hand([1, 3, 6, 4, 5])
        self.assertEqual(self.a_rule.points(self.hand), 30)


    @tags("rules", "SmallStraight")
    def test_small_straight_points_beginning(self):
        """
        Testar att points() hos ett SmallStraight objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 3, 2, 2, 4]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.SmallStraight()
        self.hand = hand.Hand([1, 3, 2, 2, 4])
        self.assertEqual(self.a_rule.points(self.hand), 30)

    @tags("rules", "SmallStraight")
    def test_small_straight_points_missing_values(self):
        """
        Testar att points() hos ett SmallStraight objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 3, 6, 6, 5]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.SmallStraight()
        self.hand = hand.Hand([1, 3, 6, 6, 5])
        self.assertEqual(self.a_rule.points(self.hand), 0)

    @tags("rules", "SmallStraight")
    def test_has_name(self):
        """
        Testar att ett SmallStraight objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.SmallStraight()
        self.assertEqual(rule.name, "Small Straight")

class Test9LargeStraight(ExamTestCase):
    """
    Testing the class LargeStraight.
    """
    @tags("rules", "LargeStraight")
    def test_large_straight_points_end(self):
        """
        Testar att points() hos ett LargeStraight objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [2, 3, 6, 4, 5]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.LargeStraight()
        self.hand = hand.Hand([2, 3, 6, 4, 5])
        self.assertEqual(self.a_rule.points(self.hand), 40)


    @tags("rules", "LargeStraight")
    def test_large_straight_points_beginning(self):
        """
        Testar att points() hos ett LargeStraight objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 3, 2, 5, 4]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.LargeStraight()
        self.hand = hand.Hand([1, 3, 2, 5, 4])
        self.assertEqual(self.a_rule.points(self.hand), 40)

    @tags("rules", "LargeStraight")
    def test_large_straight_points_missing_values(self):
        """
        Testar att points() hos ett LargeStraight objekt returnerar rätt antal poäng.
        Använder en Hand med följande tärningar som argument.
        [1, 3, 6, 6, 5]
        Förväntar att följande returneras:
        {correct}
        Fick följande:
        {student}
        """
        self.a_rule = rules.LargeStraight()
        self.hand = hand.Hand([1, 3, 6, 6, 5])
        self.assertEqual(self.a_rule.points(self.hand), 0)

    @tags("rules", "LargeStraight")
    def test_has_name(self):
        """
        Testar att ett LargeStraight objekt har rätt värde i name.
        Förväntar att .name innehåller följande.
        {correct}
        Innehöll följande:
        {student}
        """
        rule = rules.LargeStraight()
        self.assertEqual(rule.name, "Large Straight")

if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)
