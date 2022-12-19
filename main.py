from dataframe import Dataframe

def main():
  dict = {"SKU": ["X4E", "T3B", " F8D", "C7X"],
        "price": [7.0, 3.5, 8.0, 6.0],
        "sales": [5, 3, 1, 10],
        "taxed": [False, False, True, False]}
  df = Dataframe(dict)

  print("The Dataframe is:")
  print(df,"\n")

  dfc = df.copy()
  print("The Dataframe can be copied:")
  print(dfc,"\n")

  result = (df["price"] + 5.0 > 10.0) & (df["sales"] > 3) & ~df["taxed"]
  print(result)

  result = df[result]
  print(result)

  result = result["SKU"]
  print(result)



if __name__ == "__main__":
  main()