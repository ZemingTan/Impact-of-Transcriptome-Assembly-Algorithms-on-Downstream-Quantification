import csv

def merge_dicts(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        if key in dict2:
            merged_dict[key] = [dict1[key], dict2[key]]
    return merged_dict

TPMFile = "TPM.txt"
TPM={}
with open(TPMFile, 'r', newline='') as file:
    reader = csv.reader(file, delimiter=' ')
    next(reader)
    for row in reader:
        TPM.update({row[0]:float(row[1])})
GroundTruthFile = "GroundTruth.extract.txt"

GroundTruth={}
with open(GroundTruthFile, 'r', newline='') as file:
    reader = csv.reader(file, delimiter='\t')
    next(reader)
    for row in reader:
        GroundTruth.update({row[0]:float(row[1])})
data = merge_dicts(TPM,GroundTruth)
import numpy
import scipy.stats as stats

values = list(data.values())

x = [numpy.log(v[0]+1) for v in values]
y = [numpy.log(v[1]+1) for v in values]

spearman_corr, p_value = stats.spearmanr(x, y)

print(spearman_corr)

with open('Stringtie.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(['Transcript', 'Groundtruth', 'Stringtie'])

    for key, values in data.items():
        writer.writerow([key, values[0], values[1]])
