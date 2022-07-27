from unittest import TestCase


class TestDominos(TestCase):
    def test_dominos_algorithm(self):
        from dominos import Dominos
        dominos = Dominos()
        self.assertEqual(dominos.dominos_algorithm(r'||//||\||/\|', 1), r'||///\\||/\|')
        self.assertEqual(dominos.dominos_algorithm(r'||//||||\|//|||', 2), r'||////\\\|////|')
        self.assertEqual(dominos.dominos_algorithm(r'|/||\||/\|', 1), r'|//\\||/\|')
        self.assertEqual(dominos.dominos_algorithm(r'||//||\|', 8), r'||///\\|')
        self.assertEqual(dominos.dominos_algorithm(r'||||\\\\/|', 8), r'|\\\\\\\/|')

    def test_reverse_dominos(self):
        from dominos import Dominos
        dominos = Dominos()
        self.assertEqual(dominos.reverse_dominos(r'||////\\\|////|', 2), r'||//||||\|//|||')
        self.assertEqual(dominos.reverse_dominos(r'||//\\\|/|/|', 3), r'||/|||\|/|/|')
