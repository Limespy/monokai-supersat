"""Example python script"""
import unittest
from dataclasses import dataclass
def thing(*args, kwarg = 1, another_kwarg = ('hmm', None)
          ) -> tuple[list[str], int]:

    return [another_kwarg[0]], None
# A comment
(((((())))))
@dataclass
class Test(unittest.case):

    def test_1(self):
        self.assertTrue(True)
