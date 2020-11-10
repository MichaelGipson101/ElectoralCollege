import pandas as pd
import matplotlib.pyplot as plt


def read_data():
    data = open('electoral_data.csv')
    results = []
    data.readline()
    for row in data.readlines():
        row = row.split(',')
        results.append(tuple([row[0], int(row[1]), row[2].strip()]))
    data.close()
    return results


def graph():
    results = read_data()
    for choice in ['R', 'B', 'P']:
        votes = sum(x[1] for x in results if x[2] == choice)
        plt.title("Electoral Vote Count")
        plt.xlabel("Party or Swing")
        plt.ylabel("Votes")
        plt.bar([choice], [votes], color=['purple'] if choice == 'P' else ['red'] if choice == 'R' else ['blue'] if
        choice == 'B' else ['black'])
    plt.show()


def stateChoice():
    input('What state are you from?')


if __name__ == '__main__':
    read_data()
    graph()
