#this is a program to run run knn algorithum
import math as m
n=int(input("Enter the number of the element in your Table:----   "))
#supervised points
a=int(input("Ebter the first supervised point :--"))
b=int(input("Ebter the second supervised point:--"))

x1=[]
for i in range(1,n+1):
    x=int(input(f"Enter x{i} value  :--"))
    x1.append(x)
print(x1)

y1=[]
for j in range(1,n+1):
    y=int(input(f"Enter y{j} values:---"))
    y1.append(y)
print(y1)



cl=[]
for c in range(1,n+1):
    hu=input(f" name the class {c}:-- ")
    cl.append(hu)
print(cl)


w1=[]

for w in range(0,n):
    points=m.sqrt(((a-x1[w])**2 + (b-y1[w])**2))

    w1.append(points)

print(f" The distance from th super vision points are   {w1}")
# w1.sort()
# print(w1)

dict1={}
for new in range(0,n):
    f={
        w1[new]:cl[new] ,


    }
    dict1.update(f)
print(dict1)


import pandas as pd
ser=pd.Series(dict1)
ser=ser.reset_index()
ser.set_index("index",inplace=True)
ser.sort_index()
    
