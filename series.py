from generic_series import Series

def expand_if_needed(series, other, type_needed):
  """
  If other is only one element, e, instead of a Series,
  it is converted into a serie of the same length as
  series, containg only element e.
  """
  if not issubclass(type(other), Series):
    dtype = type(other)
    data = [other] * len(series.data)
    if dtype == type_needed:
      return Series(data, type_needed, series.name)
    else:
      raise TypeError('{} type not supported for operation.'.format(dtype))
  return other


def get_type(series, other):
  """
  Returns the type contained by series.
  It checks both if maybe one of the series only contains None
  """
  t = get_type_from_list(series.data)
  if t != None:
    return t
  t = get_type_from_list(other.data)
  if t != None:
    return t

def get_type_from_list(l):
  """
  Returns the type of elements in a list.
  Here we assume a list can contain only elements of the same type.
  """
  for elem in l:
    if elem != None:
      return type(elem)

class BooleanSeries(Series):
  """
  Class for Boolean Series
  """
  def __init__(self, data, name=None):
    if len(data) > 0:
      for val in data:
        if not (isinstance(val, bool) or val is None):
          raise TypeError('{} is not bool or None'.format(val))

    Series.__init__(self, data, bool, name)

  def __invert__(self):
    """
    Invert a series
    """
    data = []
    for elem in self.data:
      if elem is None:
        data.append(None)
      else:
        data.append(not elem)
    return BooleanSeries(data, self.name)

  """
  Now overwrite the and, or, xor operators
  """
  def __and__(self, other):
    other = expand_if_needed(self, other, bool)
    return BooleanSeries([x and y for x, y in zip(self.data, other.data)])

  def __or__(self, other):
    other = expand_if_needed(self, other, bool)
    return BooleanSeries([x or y for x, y in zip(self.data, other.data)])

  def __xor__(self, other):
    other = expand_if_needed(self, other, bool)
    return BooleanSeries([x ^ y if y!= None and x!= None else None for x, y in zip(self.data, other.data)])


class StringSeries(Series):
  """
  Class for String Series
  """
  def __init__(self, data, name=None):
    for val in data:
      if not (isinstance(val, str) or val is None):
        raise TypeError('{} is not str or None'.format(val))
    Series.__init__(self, data, str, name)


class NumericalSeries(Series):
  """
  Class for Numeric Series
  """
  def __init__(self, data, data_type, name):
      Series.__init__(self, data, data_type, name)

  """
  Now overwrite the +, -, *, /, <, >, <=, >=
  """
  def __add__(self, other):
    other = expand_if_needed(self, other, type(self.data[0]))
    t = get_type(self, other)
    return NumericalSeries([x + y if y!= None and x!= None else None for x, y in zip(self.data, other.data)], t, self.name)
  
  def __sub__(self, other):
    other = expand_if_needed(self, other, type(self.data[0]))
    t = get_type(self, other)
    return NumericalSeries([x - y if y!= None and x!= None else None for x, y in zip(self.data, other.data)], t, self.name)

  def __mul__(self, other):
    other = expand_if_needed(self, other, type(self.data[0]))
    t = get_type(self, other)
    return NumericalSeries([x * y if y!= None and x!= None else None for x, y in zip(self.data, other.data)], t, self.name)

  def __div__(self, other):
    other = expand_if_needed(self, other, type(self.data[0]))
    t = get_type(self, other)
    return NumericalSeries([x / y if y!= None and x!= None else None for x, y in zip(self.data, other.data)], t, self.name)

  def __ne__(self, other):
    other = expand_if_needed(self, other, type(self.data[0]))
    return BooleanSeries([x != y if y!= None and x!= None else None for x, y in zip(self.data, other.data)])

  def __gt__(self, other):
    other = expand_if_needed(self, other, type(self.data[0]))
    return BooleanSeries([x > y if y!= None and x!= None else None for x, y in zip(self.data, other.data)])

  def __lt__(self, other):
    other = expand_if_needed(self, other, type(self.data[0]))
    return BooleanSeries([x < y if y!= None and x!= None else None for x, y in zip(self.data, other.data)])

  def __ge__(self, other):
    other = expand_if_needed(self, other, type(self.data[0]))
    return BooleanSeries([x > y if y!= None and x!= None else None for x, y in zip(self.data, other.data)])

  def __le__(self, other):
    other = expand_if_needed(self, other, type(self.data[0]))
    return BooleanSeries([x < y if y!= None and x!= None else None for x, y in zip(self.data, other.data)])


class IntegerSeries(NumericalSeries):
  """
  Class for Integer Series, Subclass of Numeric Series
  """
  def __init__(self, data, name=None):
      for val in data:
          if not (isinstance(val, int) or val is None):
              raise TypeError('{} is not int or None'.format(val))

      NumericalSeries.__init__(self, data, int, name)


class FloatSeries(NumericalSeries):
  """
  Class for Float Series, Subclass of Numeric Series
  """
  def __init__(self, data, name=None):
    for val in data:
      if not (isinstance(val, float) or val is None):
        raise TypeError('{} is not float or None'.format(val))
    NumericalSeries.__init__(self, data, float, name)