import unittest
import dataframe
from series import BooleanSeries, IntegerSeries, FloatSeries, NumericalSeries

class DataFrameTest(unittest.TestCase):
  def setUp(self):
    dict = {"SKU": ["X4E", "T3B", " F8D", "C7X"],
     "price": [7.0, 3.5, 8.0, 6.0],
     "sales": [5, 3, 1, 10],
     "taxed": [False, False, True, False]}
    self.df = dataframe.Dataframe(dict)

  def test_can_construct(self):
    dict = {}
    self.df = dataframe.Dataframe(dict)

  def test_contains(self):
    self.assertTrue("price" in self.df)
    
  def test_iter(self):
    result = [elem for elem in self.df]
    wanted = ['SKU', 'price', 'sales', 'taxed']
    self.assertTrue(result == wanted)

  def test_len(self):
    result = len(self.df)
    wanted = 4
    self.assertTrue(result == wanted)


if __name__ == '__main__':
    unittest.main()