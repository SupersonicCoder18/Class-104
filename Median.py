import csv

with open("C104.csv", newline = "") as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
newData = []

for i in range(len(filedata)):
    n_num = filedata[i][1]
    newData.append(float(n_num))

n = len(newData)
newData.sort()

if n%2 == 0:
    median1 = float(newData[n//2])
    median2 = float(newData[n//2 - 1])
    median = (median1+median2)/2
else:
    median = newData[n//2]
    print(n)

print("The median of this data is " +str(median))