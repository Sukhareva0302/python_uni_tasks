import csv
with open('diabetes_data_upload.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
sum_num=0
for i in range(1,len(data)):
    sum_num=sum_num+int(data[i][0])
avg=sum_num/len(data)
print(avg)
