file1 = open('input2.txt', 'r')
file2 = open('output2.txt', 'w')

data = []
c_data = []
f_data = []
time = []
k = 1
c = 0
t = 0

for i in file1.readlines():
    data.append(i)

for i in data:
    temp = i.replace('\n', '')
    c_data.append(temp)

n_data = c_data.pop(0)
n, st = n_data.split()
n = int(n)
st = int(st)

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


for i in range(st):
    time.append(0)

for i in range(st):
    t += 1
    temp = f_data.pop(0)
    time[c] = temp[1]
    c += 1

for i in f_data:
    s = int(i[0])
    e = int(i[1])
    for j in range(len(time)):
        if int(time[j]) < s:
            t += 1
            time[j] = e
            break

file2.write(str(t) + "\n")


file1.close()
file2.close()