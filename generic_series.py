class Series:
  def __init__(self, data, series_type, name=None):
    self.name = name
    self.type = series_type
    self.data = data

  def __str__(self):
    return '''
    Series type: {}
    Series name: {}
    Series data: {}'''.format(type(self), self.name, str(self.data))

  """Series types or lengths are different => fail hard
     Otherwise, element-wise comparison"""
  def __eq__(self, other):
    if self.type != other.type:
      raise TypeError('Series have different types: {} and {}'.format(self.type, other.type))
    elif len(self.data) != len(other.data):
      raise RuntimeError('Series have different lengths')
    else:
      return self.data == other.data

  # for testing purposes
  def has_same_data(self, other):
      return self.data == other.data
