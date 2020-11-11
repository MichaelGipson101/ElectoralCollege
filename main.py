import pandas as pd
import matplotlib.pyplot as plt
import random


def begin():
    print("Welcome to the Electoral College Simulator, what would you like to do?")
    response = input(
        "Choices include: Simulation, Graph")
    while True:
        if response == "simulation" or response == "graph":
            break
        else:
            print("You haven't entered a correct option, try again")
            response = input(
                "Choices include: Simulation, Graph")
            break

    if response == "simulation":
        simulation()
    if response == "graph":
        graph()


def simulation():
    options = ["Dem", "Rep", "3rd"]

    simulation = random.choices(options, weights=(49, 49, 1), k=100)

    print("Dems won ", simulation.count('Dem'), " times")
    print("Reps won ", simulation.count('Rep'), " times")
    print("3rd Party won ", simulation.count('3rd'), " times")


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
        plt.title("Electoral Vote Count by Party")
        plt.xlabel("Party or Swing")
        plt.ylabel("Electoral Votes")
        plt.bar([choice], [votes], color=['purple'] if choice == 'P' else ['red'] if choice == 'R' else ['blue'] if
        choice == 'B' else ['black'])
    plt.show()


def stateChoice():
    input('What state are you from?')


if __name__ == '__main__':
    begin()
