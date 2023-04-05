from pypinyin import lazy_pinyin, Style
f = open('全中文.txt')
text = f.read()
text = set(text)
style = Style.BOPOMOFO
for i in text:
    if i == '\n' or i == ' ':
        continue
    k = lazy_pinyin(i, style=style)
    #print("pinyin.put(\"", end = i)
    #print("\"", end = ", \"")
    #print(k[0], end = "\");\n")
    print("<string name=\"", end = i)
    print("\">", end = k[0])
    print("</string>")
f.close
