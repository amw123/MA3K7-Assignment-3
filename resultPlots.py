import numpy as np
import random

n=21
loopSize =20
answers = np.array([])

for loop in range(loopSize):
  hat = np.arange(1,n+1)
  #print("\nLoop", loop)
  #print(hat)

  for i in range(n-1):
    a_index = random.randrange(len(hat))
    a = hat[a_index]
    hat = np.delete(hat,a_index)

    b_index = random.randrange(len(hat))
    b = hat[b_index]
    hat = np.delete(hat,b_index)
    #print("a= ", a, "b= ", b)
    #print(hat)

    c= abs(b-a)
    #print("c =", c)
    hat = np.append(hat,c)
    #print(hat)
    #print(" ")
  answers = np.append(answers,hat[0])
print(answers)

my_bins = np.linspace(-0.5, n+0.5, n+2)
plt.hist(answers,bins=my_bins, rwidth=0.8) #cumulative=True, density=False, 
plt.title(f"Distribution of Hat_{n-1} (with n={n}, sample size={loopSize})")
plt.xlabel("Value")
plt.ylabel("Frequency")
#plt.xticks(np.linspace(0,n,n+1))
