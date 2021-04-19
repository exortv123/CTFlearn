# Can you help me? 
# I need to know how many lines there are where the number of 0's is a multiple of 3 or the numbers of 1s is a multiple of 2.

fo = open("data.dat")
result = 0

for line in fo.readlines():
    line = line.strip()
    countZero = line.count("0")
    countOne = line.count("1")
    if(countZero % 3 == 0) or (countOne % 2 == 0):
        result +=1
print(result)
