class Series:
  """
  Class for generic Serie
  """
  def __init__(self, data, series_type, name=None):
    self.name = name
    self.type = series_type
    self.data = data

  def __str__(self):
    """
    String representation of a Serie
    """
    return '''
    Series type: {}
    Series name: {}
    Series data: {}'''.format(type(self), self.name, str(self.data))

  def __eq__(self, other):
    """
    Overwrites the equal operator 
    Series types or lengths are different => fail hard
    Otherwise, element-wise comparison
    """
    if self.type != other.type:
      raise TypeError('Series have different types: {} and {}'.format(self.type, other.type))
    elif len(self.data) != len(other.data):
      raise RuntimeError('Series have different lengths')
    else:
      return self.data == other.data
