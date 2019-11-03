#! /usr/bin/python3
#Program for 4,8,m adjacency

#4-adjacency
def N4(a, i , j):
   s = set()
   if (i -1) >= 0:
     s.add(a[i-1][j])
   if (i+1) < len(a):
     s.add(a[i+1][j])
   if (j-1) >= 0:
     s.add(a[i][j-1])
   if (j+1) < len(a[0]):
     s.add(a[i][j+1])
   return s

#8-adjacency
def N8(a, i, j):
   s = set()
   row = len(a)
   col = len(a[0])
   for x in N4(a, i, j):
    s.add(x)
   if (i+1 < row) and (j+1 < col):
     s.add(a[i+1][j+1])
   if (i-1 >= 0) and (j-1 >= 0):
     s.add(a[i-1][j-1])
   if (i-1 >= 0) and (j+1 < col):
     s.add(a[i-1][j+1])
   if (i+1 < row) and (j-1 >= 0):
     s.add(a[i+1][j-1])
   return s

#m-adjacency 
def Nm(a, i, j, v):
    s = set()
    s1 = N4(a, i, j)
    for x in s1:
      s.add(x)
    if (i+1) < len(a) and (j+1) < len(a[0]):
      s2 = N4(a, i+1, j+1)
      s3 = s1 & s2
      s4 = s3 - v
      for x in s4:
        s.add(x) 
    if (i-1) >= 0 and (j-1) >= 0:
      s2 = N4(a, i-1, j-1)
      s3 = s1 & s2
      s4 = s3 - v
      for x in s4:
        s.add(x)
    if (i+1) < len(a) and (j-1) >= 0:
      s2 = N4(a, i+1, j-1)
      s3 = s1 & s2
      s4 = s3 - v
      for x in s4:
        s.add(x)  
    if (i-1) >= 0 and (j+1) < len(a[0]):
      s2 = N4(a, i-1, j+1)
      s3 = s1 & s2
      s4 = s3 - v
      for x in s4:
        s.add(x)
    return s
    
#given binary img
img = [[10, 4, 4, 4, 5, 5, 5, 15, 15],
[15, 15, 15 , 4, 4, 5, 5, 15, 2],
[5, 2, 15, 3, 3, 3, 5, 5, 1],
[10, 3, 5, 5, 4, 10, 10, 4, 1],
[10, 2, 4, 5, 15, 5, 10, 5, 10],
[5, 5, 5, 5, 7, 7, 7, 15, 5],
[15, 4, 10, 10, 10, 10, 7, 7, 5],
[15, 4, 15, 15, 5, 10, 7, 10, 10],
[15, 15, 5, 5, 5, 10, 10, 10, 10]]

v = {5, 10, 15}

for i in range(len(img)):
  for j in range(len(img[0])):
     print(N4(img, i, j), end = " ")
     
print("\n")
     
for i in range(len(img)):
  for j in range(len(img[0])):
     print(N8(img, i, j), end = " ")
print("\n")
     
for i in range(len(img)):
  for j in range(len(img[0])):
     print(Nm(img, i, j, v), end = " ")
print("\n")
     
    
