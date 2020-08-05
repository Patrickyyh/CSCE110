words= list()
with open('words.txt','r')as f:
   lines = f.readline()
   while (lines!=""):
     lines = lines.strip()
     words.append(lines)
     lines = f.readline()

print("Result:",end=" ")
for word in words:
    if word == word[::-1]:
        print(True,end = " ")
    else:
        print(False , end = " ")
