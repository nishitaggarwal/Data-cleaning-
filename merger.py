#%%
import csv
dataset_1 =[]
dataset_2 = []

with open("Bright_stars.csv","r",encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_1.append(row)
        
 
with open("unit_converted_stars.csv","r",encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset_2.append(row)
        
      
header_1 = dataset_1[0]
header_2 = dataset_2[0]
planet_data_1 = dataset_1[1:]
planet_data_2 = dataset_2[1:]

headers = header_1 + header_2
planet_data = []

for i in planet_data_1:
    planet_data.append(i)
for j in planet_data_2:
    planet_data.append(j)

with open("final.csv","w",encoding='utf8') as f:
    csv_writer = csv.writer(f)

    csv_writer.writerow(headers)
    csv_writer.writerows(planet_data)
# %%
