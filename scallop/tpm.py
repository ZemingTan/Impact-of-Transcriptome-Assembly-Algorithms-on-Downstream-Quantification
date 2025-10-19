import csv
IDFile = 'ID.txt'

ID = {}

with open(IDFile, 'r', newline='') as file:
    reader = csv.reader(file, delimiter=' ')
    next(reader)
    for row in reader:
        ID.update({row[1]:row[0]})
print(len(ID))
QuantFile = 'salmon.quant/quant.sf'
quant = {}
with open(QuantFile, 'r', newline='') as file:
    reader = csv.reader(file,delimiter='\t')
    next(reader)
    for row in reader:
        quant.update({row[0]:float(row[3])})
TPM={ID[key]: quant[key] for key in ID if key in quant}
with open('TPM.extract.txt','w',newline='') as file:
    writer = csv.writer(file,delimiter=' ')
    for key, value in TPM.items():
        writer.writerow([key, value])

print(len(TPM))

