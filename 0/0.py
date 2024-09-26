import csv
with open('diabetes_data_upload.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))
print(data)
