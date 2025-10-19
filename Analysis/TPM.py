import csv
IDFile = 'StringtieID.txt'

StringID = []

with open(IDFile, 'r', newline='') as file:
    reader = csv.reader(file, delimiter=' ')
    next(reader)
    for row in reader:
        StringID.append(row[1])
QuantFile = 'quant.sf'
quant = {}
with open(QuantFile, 'r', newline='') as file:
    reader = csv.reader(file,delimiter='\t')
    next(reader)
    for row in reader:
        quant.update({row[0]:float(row[3])})
TPM = {}
for key in quant.keys():
    if key in StringID:
        print(key)
        TPM[key]=quant[key]
with open('TPM.txt','w',newline='') as file:
    writer = csv.writer(file,delimiter='\t')
    for key, value in TPM.items():
        writer.writerow([key, value])
