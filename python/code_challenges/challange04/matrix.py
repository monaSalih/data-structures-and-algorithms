def  sumFunc(matrix):
  newMatrix=[]

  for i in matrix:#n
    sum=0
    for j in i:#n
      sum=sum+j
    newMatrix=newMatrix+[sum]
  return newMatrix

matrix =[ [1, 2, 3], [3, 5, 7], [1, 7, 10] ]
print(sumFunc(matrix))
