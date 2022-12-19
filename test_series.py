import unittest

from series import BooleanSeries, IntegerSeries, FloatSeries, NumericalSeries

class BooleanSeriesTestCases(unittest.TestCase):
  def test_construct_BooleanSeries(self):
    bs1 = BooleanSeries([True, False, False])
    self.assertEqual(len(bs1.data), 3)

    bs2 = BooleanSeries([True, None, False])
    self.assertEqual(len(bs2.data), 3)

    with self.assertRaises(TypeError):
        BooleanSeries(['apple', True, False])

  def test_BooleanSeries_equality(self):
    bs1 = BooleanSeries([True, False, False])
    bs2 = BooleanSeries([True, False, False])
    bs3 = BooleanSeries([True, False, False, True])
    bs4 = BooleanSeries([True, False, True])

    self.assertTrue(bs1 == bs2)
    with self.assertRaises(RuntimeError):
      bs1 == bs3
    self.assertFalse(bs1 == bs4)

  def test_BooleanSeries_invert(self):
    bs1 = BooleanSeries([True, False, False])
    bs2 = BooleanSeries([False, True, True])
    bs3 = BooleanSeries([True, None, False])
    bs4 = BooleanSeries([False, None, True])

    self.assertTrue(bs1.has_same_data(~bs2))
    self.assertTrue(bs3.has_same_data(~bs4), msg='bs3:{} bs4:{} ~bs4:{}'.format(bs3, bs4, ~bs4))

  def test_BooleanSeries_and(self):
    bs1 = BooleanSeries([True, True, False, None, None])
    bs2 = BooleanSeries([True, False, False, True, None])
    self.assertTrue((bs1 and bs2) == BooleanSeries([True, False, False, True, None]))

  def test_BooleanSeries_and(self):
    bs1 = BooleanSeries([True, True, False, None, None])
    bs2 = BooleanSeries([True, False, False, True, None])
    self.assertTrue((bs1 or bs2) == BooleanSeries([True, True, False, None, None]))

  def test_BooleanSeries_and(self):
    bs1 = BooleanSeries([True, True, False, None, None])
    bs2 = BooleanSeries([True, False, False, True, None])
    self.assertTrue((bs1 ^ bs2) == BooleanSeries([False, True, False, None, None]))


class NumericalSeriesTestCases(unittest.TestCase):
  def test_greater_than(self):
    is1 = IntegerSeries([3, 5, 10])
    is2 = IntegerSeries([1, None, 11])
    self.assertTrue((is1 > is2) ==  BooleanSeries([True, None, False]))

    fs1 = FloatSeries([3.0, 5.0, 10.0])
    self.assertTrue((fs1 > 4.0) == BooleanSeries([False, True, True]))

  def test_addition(self):
    is1 = IntegerSeries([3, 5, 10])
    is2 = IntegerSeries([1, None, 11])
    self.assertTrue((is1 + is2) ==  NumericalSeries([4, None, 21], int, None))

    fs1 = FloatSeries([3.0, None, 10.0])
    self.assertTrue((fs1 + 4.0) ==  NumericalSeries([7.0, None, 14.0], float, None))


if __name__ == '__main__':
    unittest.main()