import numpy as np
import random

n=10
hat = np.arange(1,n+1)
print(hat)

for i in range(n-1):
  a_index = random.randrange(len(hat))
  a = hat[a_index]
  print("a index =", a_index, "  so a= ", a)
  hat = np.delete(hat,a_index)
  print(hat)

  b_index = random.randrange(len(hat))
  b = hat[b_index]
  print("b index =", b_index, "  so b= ", b)
  hat = np.delete(hat,b_index)
  print(hat)

  c= abs(b-a)
  print("We append", c)
  hat = np.append(hat,c)
  print(hat)
  print(" ")
