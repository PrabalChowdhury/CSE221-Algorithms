file1 = open('input3.txt', 'r')
file2 = open('output3.txt', 'w')

data = []
c_data = []
op = []
jack = []
jill = []
jack_time = 0
jill_time = 0
p = 0

for i in file1.readlines():
    data.append(i)

for i in data:
    temp = i.replace('\n', '')
    c_data.append(temp)

work = c_data[1].split()
calls = c_data[2]
work.sort()

for i in calls:
    if i == 'J':
        jack_work = work[p]
        jack.append(jack_work)
        jack_time += int(jack_work)
        op.append(jack_work)
        p += 1
    else:
        c = 0
        temp = jack
        h_time = temp.pop()
        while True:
            if h_time not in jill:
                jill.append(h_time)
                jill_time += int(h_time)
                op.append(h_time)
                break
            else:
                c += 1
                h_time = temp[c]

for i in op:
    file2.write(i)

file2.write('\n')
file2.write('Jack will work for ' + str(jack_time) + " hours\n")
file2.write('Jill will work for ' + str(jill_time) + " hours\n")


file1.close()
file2.close()