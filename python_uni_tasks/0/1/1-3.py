import csv
with open('diabetes_data_upload.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

from array import *
ob1di1=array('i',[])
ob0di0=array('i',[])
ob1di0=array('i',[])
ob0di1=array('i',[])
for i in range(1,len(data)):
    obesity=data[i][-2]
    diabetes=data[i][-1]
    if obesity == "Yes":
        if diabetes == "Positive":
            ob1di1.append(i)
        else:
            ob1di0.append(i)
    else:
        if diabetes == "Positive":
            ob0di1.append(i)
        else:
            ob0di0.append(i)

print(ob1di1, ob1di0)
print()
print(ob0di1, ob0di0)
