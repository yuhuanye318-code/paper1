# f = open(".\wenjian.txt","r",encoding="utf-8")
# a = f.read()
# print(a)
# f.close()

# with open(".\wenjian.txt","r",encoding="utf-8") as f:
# with open(".\wenjian.txt","r",encoding="utf-8") as f:
#     print(f.readline())
#     print(f.readline())

with open("wenjian.txt", "r", encoding="utf-8") as f:
    a = f.readlines()
    for i in a:
        print(i)