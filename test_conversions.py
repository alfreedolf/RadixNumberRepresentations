import unittest
from radix_repr_var.binary import Binary
from radix_repr_var.octal import Octal


class TestConversions(unittest.TestCase):

    def setUp(self):
        self.bin_val_three = Binary(11)
        self.bin_val_eleven = Binary(1011)
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
