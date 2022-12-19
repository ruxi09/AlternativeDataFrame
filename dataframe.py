from series import BooleanSeries, FloatSeries, IntegerSeries, StringSeries, get_type_from_list

class Dataframe:
  def __init__(self, full_data):
    if full_data is None:
      self.full_data = []
      self.data = []
      self.columns = []
    else:
      self.full_data = full_data
      self.columns = list(full_data.keys())
      self.data = []
      for elem in full_data:
        t = get_type_from_list(full_data[elem])
        if t == bool:
          self.data.append(BooleanSeries(full_data[elem], elem))
        elif t == float:
          self.data.append(FloatSeries(full_data[elem], elem))
        elif t == int:
          self.data.append(IntegerSeries(full_data[elem], elem))
        elif t == str:
          self.data.append(StringSeries(full_data[elem], elem))
        else:
          raise TypeError('{} type not supported.'.format(t))

  def __getitem__(self, key):
    """
    Overwrite the get operator.
    If given a BooleanSeries returns the Dataframe with returns another
     DataFrame containing only the rows with True values
    """
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
    """
    Overwrites the equal operator
    Check the base dict
    """
    return(self.full_data == other.full_data)

  def __repr__(self):
    """
    Overwrites String Representation of the Dataframe
    """
    result = ['\t'.join(self.columns)]
    for i in range(len(self.data[0].data)):
      line = '\t'.join(str(self.data[j].data[i]) for j in range(len(self.columns)))
      result.append(line)
    return '\n'.join(result)

  def copy(self):
    """
    Creates a copy of the given Dataframe
    """
    return self.__class__(self.full_data)

  def __contains__(self, item):
    """
    Checks is Dataframe contains given item
    """
    return item in self.columns

  def __iter__(self):
    """
    Return an iterator object that goes through each 
    element of the Dataframe
    """
    for column in self.columns:
        yield column

  def __len__(self):
      return len(self.data)