
# pylint: disable=E1601

"""
Script to test python scripts for applicant project
"""

import unittest

from calculator import CalculatorClass
from primes import PrimeClass


class TestApplicantPython(unittest.TestCase):
    """
    Main class to test python scripts for applicant project
    """

    def setUp(self):
        """
        Method init of global unittest class
        """
        self.obj_calculator = CalculatorClass()
        self.obj_prime = PrimeClass()

    def test_10_sum(self):
        """
        UnitTest method to check sum method
        """
        print "start test:" + \
            self.test_10_sum.__doc__
        mysum = self.obj_calculator.sum([1, 2, 3, 4, 5, 6])
        if mysum != 'not implement yet':
            self.assertEqual(mysum, 21, 'incorrect sum method')
        print "end test:" + \
            self.test_10_sum.__doc__

    def test_20_primes(self):
        """
        UnitTest method to check primes method
        """
        print "start test:" + \
            self.test_20_primes.__doc__
        if self.obj_prime.is_prime(0) != 'not implement yet':
            primes_result = all(
                [
                    self.obj_prime.is_prime(num) is True
                    for num in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                                31, 37, 41, 43, 47, 53, 59, 61, 67,
                                71, 73, 79, 83, 89, 97, 101, 103, 107]
                ]
            )
            self.assertEqual(
                primes_result,
                True,
                'incorrect prime method with primes numbers')

            no_primes_result = all(
                [
                    self.obj_prime.is_prime(num) is False
                    for num in [1, 4, 6, 8, 9, 10, 12, 14,
                                15, 16, 18, 20, 21, 22, 24,
                                25]
                ]
            )
            self.assertEqual(
                no_primes_result,
                True,
                'incorrect prime method with not primes numbers')
        print "end test:" + \
            self.test_20_primes.__doc__


if __name__ == '__main__':
    unittest.main()
