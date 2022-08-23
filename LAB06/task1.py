file1 = open('input1.txt', 'r')
file2 = open('output1.txt', 'w')

data = []
for i in file1:
    data.append(i.replace('\n', ''))
total = int(data[0])
real = data[1]
pred = data[2]

zone = {
    "Y": "Yasnaya",
    "P": "Pochinki",
    "S": "School",
    "R": "Rozhok",
    "F": "Farm",
    "M": "Mylta",
    "H": "Shelter",
    "I": "Prison"
}


def lcs(x, y):
    m = len(x)
    n = len(y)
    l = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif x[i - 1] == y[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i - 1][j], l[i][j - 1])
    idx = l[m][n]
    zone_seq = [""] * (idx + 1)
    zone_seq[idx] = ""
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            zone_seq[idx - 1] = x[i - 1]
            i = i - 1
            j = j - 1
            idx -= 1
        elif l[i][j - 1] < l[i - 1][j]:
            i = i - 1
        else:
            j = j - 1
    zone_str = ''.join(zone_seq[:-1])
    return zone_str


test = lcs(real, pred)

for i in test:
    if i in zone.keys():
        file2.write(zone[i] + " ")
file2.write("\nCorrectness of Prediction: " + str(len(test) * 100 // total) + "%")

file1.close()
file2.close()