import csv
with open('diabetes_data_upload.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
sum_num_F=0
sum_num_M=0
len_M=0
len_F=0
#gender = "Male"
for i in range(1,len(data)):
    gender=data[i][1]
    if gender == "Male":
        sum_num_M=sum_num_M+int(data[i][0])
        len_M=len_M+1
    else:
        sum_num_F=sum_num_F+int(data[i][0])
        len_F=len_F+1
avg_F=sum_num_F/len_F
avg_M=sum_num_M/len_M
print("Средний врзраст мужчин =", avg_M)
print("Средний врзраст женщин =", avg_F)
