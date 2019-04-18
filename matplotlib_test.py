import matplotlib.pyplot as plt
#from mpmath import mp
import pandas as pd
from random import choice

#set length of pi
# pi_length = 1000000
# mp.dps = pi_length
# pi = mp.pi



list_of_squares=[]

for x in range(1,1001):
    square = {}

    square['result']=x**2
    square['value']=x
    list_of_squares.append(square)


df=pd.DataFrame(list_of_squares)
x = df.value
y = df.result
plt.scatter(x,y,c=y, s=10, edgecolors='none')
print(df)


# for square in list_of_squares:
#     plt.scatter(square['value'],square['result'],s=10,edgecolors="none")
#
plt.title("Squares",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
plt.axis([0,1000,0,1000000])

plt.tick_params(axis="both",which="major")
plt.show()
