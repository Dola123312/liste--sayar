def listesayar():
  for i in liste:
      if type(i) == list:
          for e in i:
              print(e)
      else:
          print(i)
