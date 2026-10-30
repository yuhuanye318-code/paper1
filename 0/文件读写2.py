with open("poem.txt", "w", encoding="UTF-8") as f:
    f.write("我欲乘风归去")
    f.write("\n又恐琼楼玉宇")
    f.write("\n高处不胜寒")

with open("poem.txt", "a", encoding="UTF-8") as g:
    g.write("\n起舞弄清影")
    g.write("\n何似在人间")