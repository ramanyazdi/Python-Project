

count = 0
for i in range(112,999):
    if str(i)[1] != str(0) and str(i)[2] != str(0):
        if str(i)[0] != str(i)[1] or str(i)[0] != str(i)[2] :
            if str(i)[0] == str(i)[1] or str(i)[0] == str(i)[2] or str(i)[1] == str(i)[2]:
                print(i)
                count += 1

print(count)