import re
#name = input("Enter file:")
#if len(name) < 1 : name = "sample.txt"
handle = open('assignment.txt')
lst = list()
for line in handle:
    line=line.strip()
    y = re.findall('([0-9]+)',line)
    if len(y)>0:
        for num in y:
            numb = int(num)
            lst.append(numb)
            #print(numb)
    else:
        continue
print(sum(lst))
