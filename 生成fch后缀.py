a= input("请输入文件名称（用空格间隔）：")

b = a.split(" ")

print(b)

l=[]

for i in b:
    k = i + ".fch"
    print(k)
    l.append(k)

print(l)

m = " ".join(l)

print(m)

#2-bl 3-bl 2-fn 3-fn 2-sf 3-sf 2-mz 4-mz 5-mz 2-ez 4-ez 5-ez 2-sz 4-sz 5-sz

#2-ben-bl 3-ben-bl 4-ben-bl 5-ben-bl 6-ben-bl 7-ben-bl 2-ben-fn 3-ben-fn 4-ben-fn 5-ben-fn 6-ben-fn 7-ben-fn 2-ben-sf 3-ben-sf 4-ben-sf 5-ben-sf 6-ben-sf 7-ben-sf 2-ben-mz 4-ben-mz 5-ben-mz 6-ben-mz 7-ben-mz 2-ben-ez 4-ben-ez 5-ben-ez 6-ben-ez 7-ben-ez 2-ben-sz 4-ben-sz 5-ben-sz 6-ben-sz 7-ben-sz

#2-sz-N+1 2-sz-N-1 3-ben-bl-N+1 3-ben-bl-N-1 5-ben-bl-N+1 5-ben-bl-N-1 2-ben-mz-N+1  2-ben-mz-N-1 5-ben-mz-N+1 5-ben-mz-N-1