from series import BooleanSeries, FloatSeries, IntegerSeries, StringSeries, get_type_from_list

class Dataframe:
  def __init__(self, dict_series):
    if dict_series is None:
      self.full_data = []
      self.data = []
      self.columns = []
    else:
      self.full_data = dict_series
      self.columns = list(dict_series.keys())
      self.data = []
      for elem in dict_series:
        t = get_type_from_list(dict_series[elem])
        if t == bool:
          self.data.append(BooleanSeries(dict_series[elem], elem))
        elif t == float:
          self.data.append(FloatSeries(dict_series[elem], elem))
        elif t == int:
          self.data.append(IntegerSeries(dict_series[elem], elem))
        elif t == str:
          self.data.append(StringSeries(dict_series[elem], elem))
        else:
          raise TypeError('{} type not supported.'.format(t))

  def __getitem__(self, key):
    if isinstance(key, BooleanSeries):
      rows = []
      for i in range(len(key.data)):
          if key.data[i]:
              rows.append(i)
      print(rows)
      dict = {}
      for col in self.full_data:
        l = [self.full_data[col][i] for i in rows]
        dict[col] = l
      return Dataframe(dict)
          
    else:
      if key not in self.columns:
        return KeyError("{} is not a valid column name in the selected dataframe".format(key))
      else:
        idx = self.columns.index(key)
        return self.data[idx]
  
  def __eq__(self, other):
    return(self.full_data == other.full_data)

  def __repr__(self):
    result = ['\t'.join(self.columns)]
    for i in range(len(self.data[0].data)):
      line = '\t'.join(str(self.data[j].data[i]) for j in range(len(self.columns)))
      result.append(line)
    return '\n'.join(result)

  def copy(self):
    return self.__class__(self.full_data)

  def __contains__(self, item):
      return item in self.columns

  def __iter__(self):
    for column in self.columns:
        yield column

  def __len__(self):
      return len(self.data)