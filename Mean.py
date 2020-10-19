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
total = 0

for x in newData:
    total+=x

mean = total/n

print("The mean of all the heights of 25000 students is "+ str(mean) +" inches")