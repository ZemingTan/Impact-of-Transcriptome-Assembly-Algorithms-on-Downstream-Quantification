import csv
IDFile = 'ID.txt'

ID = {}

with open(IDFile, 'r', newline='') as file:
    reader = csv.reader(file, delimiter=' ')
    next(reader)
    for row in reader:
        ID.update({row[0]:0})
print(len(ID))
QuantFile = '../GroundTruth.txt'
quant = {}
with open(QuantFile, 'r', newline='') as file:
    reader = csv.reader(file,delimiter=' ')
    next(reader)
    for row in reader:
        quant.update({row[0]:float(row[1])})
TPM={key: quant[key] for key in quant if key in ID}
with open('GroundTruth.extract.txt','w',newline='') as file:
    writer = csv.writer(file,delimiter='\t')
    for key, value in TPM.items():
        writer.writerow([key, value])

print(len(TPM))

