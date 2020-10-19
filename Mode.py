import csv
from collections import Counter

with open("C104.csv", newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
newData = []

for i in range(len(filedata)):
    n_num = filedata[i][1]
    newData.append(float(n_num))

n = len(newData)
data = Counter(newData)
getmode = dict(data)
mode1 = []
mode2 = []

for a,v in getmode.items():
    a = float(a)
    if 60<a<70:
        if v == max(list(data.values())):
            mode1.append(a)
    elif 70<a<80:
        if v == max(list(data.values())):
            mode2.append(a)

if len(mode1) > len(mode2):
    print("Mode is "+str(mode1))
else:
    print("Mode is "+str(mode2))