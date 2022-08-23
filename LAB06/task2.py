file1 = open('input2.txt', 'r')
file2 = open('output2.txt', 'w')
data = []
for i in file1:
    data.append(i.replace('\n', ''))
x = data[0]
y = data[1]
z = data[2]


def lcs(X, Y, Z):
    m = len(X)
    n = len(Y)
    o = len(Z)
    l = [[[0 for k in range(o + 1)] for j in range(n + 1)] for i in range(m + 1)]
    for i, x in enumerate(X):
        for j, y in enumerate(Y):
            for k, z in enumerate(Z):
                if x == y and y == z:
                    l[i + 1][j + 1][k + 1] = l[i][j][k] + 1
                else:
                    l[i + 1][j + 1][k + 1] = max(l[i + 1][j + 1][k], l[i][j + 1][k + 1], l[i + 1][j][k + 1])
    lcs_str = ""
    while m > 0 and n > 0 and o > 0:
        step = l[m][n][o]
        if step == l[m - 1][n][o]:
            m -= 1
        elif step == l[m][n - 1][o]:
            n -= 1
        elif step == l[m][n][o - 1]:
            o -= 1
        else:
            lcs_str += str(X[m - 1])
            m -= 1
            n -= 1
            o -= 1
    return len(lcs_str[::-1])


length = lcs(x, y, z)
file2.write(str(length))

file1.close()
file2.close()
