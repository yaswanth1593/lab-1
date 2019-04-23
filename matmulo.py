X = [[0,0,0],[0,0,0],[0 ,0,0]]

Y = [[6,8,1],[9,27,5],[2,43,31]]

result = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(X)):
 for j in range(len(Y[0])):
                 for k in range(len(Y)):
                            result[i][j] += X[i][k] * Y[k][j]

for r in result:
 print(r)

