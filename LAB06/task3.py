def LCS(X, Y, Z):
    m = len(X)
    n = len(Y)
    o = len(Z)
    c = [[[0 for i in range(o + 1)] for j in range(n + 1)] for k in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            for k in range(1, o + 1):
                if i == 0 or j == 0 or k == 0:
                    c[i][j][k] = 0
                else:
                    if X[i - 1] == Y[j - 1] and X[i - 1] == Z[k - 1]:
                        c[i][j][k] = c[i - 1][j - 1][k - 1] + 1
                    else:
                        if c[i - 1][j][k] >= c[i][j - 1][k]:
                            max = c[i - 1][j][k]
                            if max >= c[i][j][k - 1]:
                                c[i][j][k] = max
                            else:
                                max = c[i][j][k - 1]
                                c[i][j][k] = max
                        else:
                            max = c[i][j - 1][k]
                            if max >= c[i][j][k - 1]:
                                c[i][j][k] = max
                            else:
                                max = c[i][j][k - 1]
                                c[i][j][k] = max

    return c[m][n][o]
                           
f1=open("input3.txt","r")
f2=open("output3.txt","w")
l=f1.read().split("\n")
x=l[0]
y=l[1]
z=l[2]
f2.write(str(LCS(x,y,z)))