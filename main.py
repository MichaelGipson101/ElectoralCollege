import pandas as pd
import matplotlib.pyplot as plt


def read_data(file_name):
    data = open(file_name)
    results = []
    data.readline()
    for row in data.readlines():
        row = row.split(',')
        results.append(tuple([row[0], int(row[1]), row[2].strip()]))
    data.close()
    return results


if __name__ == '__main__':
    results = read_data('electoral_data.csv')
    print(results)
