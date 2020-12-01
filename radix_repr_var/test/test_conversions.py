import unittest
from radix_repr_var.binary import Binary
from radix_repr_var.octal import Octal


class TestConversions(unittest.TestCase):
    """
    This is a test case for conversions
    """
    def setUp(self):
        """
        defining some test values:
        3 in binary
        11 in binary
        12 in octal
        :return:
        """
        self.bin_val_three = Binary(11)
        self.bin_val_eleven = Binary(1011)
        self.octal_val_twelve = Octal(14)

    def test_convert_to(self):
        decimal_eleven = self.bin_val_eleven.convert_to(10)
        self.assertEqual(11, decimal_eleven)

        decimal_three = self.bin_val_three.convert_to(10)
        self.assertEqual(3, decimal_three)

        decimal_twelve = self.octal_val_twelve.convert_to(10)
        self.assertEqual(12, decimal_twelve)


if __name__ == '__main__':
    unittest.main()
