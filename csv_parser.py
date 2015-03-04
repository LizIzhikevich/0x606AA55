__author__ = 'joanneyeh'

import pandas as pd

"""
This program converts the text files for the California
Discipline Dataset to a csv file for easy processing

Usage examples at the end of file

"""


def parse_text_file(filename, output_file_name):
    with open(filename) as file:
        without_commas = file.read().replace(',', '')
        without_commas = without_commas.replace('*', '0')
    file = without_commas.split('\n')
    data = []
    for entry in file:
        data.append(entry.split('\t'))
    df = pd.DataFrame(data)
    df = df.drop([df.columns[13]], axis=1)
    df = df.drop([df.columns[13]], axis=1)
    df.to_csv(output_file_name, index=False, header=False)
    return

parse_text_file('CA_discip13.txt', 'CA_discip13.csv')
parse_text_file('CA_discip12.txt', 'CA_discip13.csv')
