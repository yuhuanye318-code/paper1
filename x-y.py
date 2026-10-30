a = range(4,6)
b = ["bl","fn","sf","mz","ez","sz"]
l=[]

for i in b:
    for j in a:
        c = str(j) + "-" + str(i)
        print(c)
        l.append(c)

print(l)
k = " ".join(l)
print(k)