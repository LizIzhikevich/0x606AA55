__author__ = 'joanneyeh'

import csv
import pandas as pd

def parse_text_file(filename):
    with open(filename) as file:
        without_commas = file.read().replace(',', '')
        without_commas = without_commas.replace('*', '0')
    test = without_commas.split('\n')
    return test

tester = parse_text_file('CAdiscipline14.txt')

data = []
for entry in tester:
    data.append(entry.split('\t'))

df = pd.DataFrame(data)
df = df.drop([df.columns[13]], axis=1)
df = df.drop([df.columns[13]], axis=1)

df.to_csv('CA_discip14.csv', index=False, header=False)

DataFrame.plot()