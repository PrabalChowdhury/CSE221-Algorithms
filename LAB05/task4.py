file_input =open("input4.txt", "r")
line = file_input.readlines()
for i in range(len(line)):
    # print(line[i])
    a, b = line[i].split()
    a = int(a)
    b = int(b)
    if a != b:
        count = 0
        
        while (a * a <= b):
            if a * a <= b:
                count += 1
                a += 1
        #print(count)
        file_input= open("output4.txt","a") 
        file_input.writelines(str(count)+"\n")