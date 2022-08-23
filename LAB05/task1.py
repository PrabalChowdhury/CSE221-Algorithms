file1 = open('input1.txt', 'r')
file2 = open('output1.txt', 'w')

data = []
c_data = []
f_data = []
k = 1
t = 1

for i in file1.readlines():
    data.append(i)

for i in data:
    temp = i.replace('\n', '')
    c_data.append(temp)

n = int(c_data.pop(0))

for i in c_data:
    f_data.append(i.split())

for i in range(n):
    swap = False
    for j in range(0, n - i - 1):
        if int(f_data[j][k]) > int(f_data[j + 1][k]):
            f_data[j], f_data[j + 1] = f_data[j + 1], f_data[j]
            swap = True
    if not swap:
        break

op = [f_data.pop(0)]
end = op[0][1]

for i in f_data:
    s = int(i[0])
    e = int(i[1])
    if int(end) <= s:
        op.append(i)
        t += 1
        end = e

file2.write(str(t) + "\n")

for i in op:
    file2.write(i[0])
    file2.write(" ")
    file2.write(i[1])
    file2.write('\n')

file1.close()
file2.close()











