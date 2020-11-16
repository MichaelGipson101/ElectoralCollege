import sys
import matplotlib.pyplot as plt
import random


def begin():
    print("Welcome to the Electoral College Simulator, what would you like to do?")
    response = input(
        "Choices include: Simulation, Graph, State Choice, or Exit").lower()
    while True:
        if response == "simulation":
            break
        elif response == "graph":
            break
        elif response == "state choice":
            break
        elif response == "exit":
            break
        else:
            print("You haven't entered a correct option, try again")
            response = input(
                "Choices include: Simulation, Graph, State Choice, or Exit").lower()

    if response == "simulation":
        simulation()
    if response == "graph":
        graph()
    if response == "state choice":
        stateChoice()
    if response == "exit":
        sys.exit()


def simulation():
    data = read_data()
    r_wins, b_wins = 0, 0
    for i in range(100):  # This runs 101 times
        states = []
        for state in data:  # This 50 long
            if state[2] == 'P':
                party_choice = random.choices(['R', 'B'], [0.7, 0.3])[0]
                temp = (state[0], state[1], party_choice)
                states.append(temp)
            else:
                states.append(state)
        r_count = 0
        b_count = 0
        for state in states:
            if state[2] == 'R':
                r_count += state[1]
            if state[2] == 'B':
                b_count += state[1]
        print(f'Simulation {i + 1}\nR={r_count}\nB={b_count}\nTotal={b_count + r_count}')
        if b_count > r_count:
            b_wins += 1
        else:
            r_wins += 1
    print("Republican count:", r_wins, " Democrat count:", b_wins)
    if r_wins > b_wins:
        print('Republicans won!')
    else:
        print('Democrats Won!')
    begin()


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
    begin()


def stateChoice():
    data = read_data()
    response = input("Please Choose a State to view its Electoral Votes and Party. ").lower()
    while True:
        if response == "alabama" or response == "al":
            print(data[0])
            break
        elif response == "alaska" or response == "ak":
            print(data[1])
            break
        elif response == "arizona" or response == "az":
            print(data[2])
            break
        elif response == "arkansas" or response == "ar":
            print(data[3])
            break
        elif response == "california" or response == "ca":
            print(data[4])
            break
        elif response == "colorado" or response == "co":
            print(data[5])
            break
        elif response == "connecticut" or response == "ct":
            print(data[6])
            break
        elif response == "delaware" or response == "de":
            print(data[7])
            break
        elif response == "district of columbia" or response == "dc":
            print(data[8])
            break
        elif response == "florida" or response == "fl":
            print(data[9])
            break
        elif response == "georgia" or response == "ga":
            print(data[10])
            break
        elif response == "hawaii" or response == "hi":
            print(data[11])
            break
        elif response == "idaho" or response == "id":
            print(data[12])
            break
        elif response == "illinois" or response == "il":
            print(data[13])
            break
        elif response == "indiana" or response == "in":
            print(data[14])
            break
        elif response == "iowa" or response == "ia":
            print(data[15])
            break
        elif response == "kansas" or response == "ks":
            print(data[16])
            break
        elif response == "kentucky" or response == "ky":
            print(data[17])
            break
        elif response == "louisiana" or response == "la":
            print(data[18])
            break
        elif response == "maine" or response == "me":
            print(data[19])
            break
        elif response == "maryland" or response == "md":
            print(data[20])
            break
        elif response == "massachusetts" or response == "ma":
            print(data[21])
            break
        elif response == "michigan" or response == "mi":
            print(data[22])
            break
        elif response == "minnesota" or response == "mn":
            print(data[23])
            break
        elif response == "mississippi" or response == "ms":
            print(data[24])
            break
        elif response == "missouri" or response == "mo":
            print(data[25])
            break
        elif response == "montana" or response == "mt":
            print(data[26])
            break
        elif response == "nebraska" or response == "ne":
            print(data[27])
            break
        elif response == "nevada" or response == "nv":
            print(data[28])
            break
        elif response == "new hampshire" or response == "nh":
            print(data[29])
            break
        elif response == "new jersey" or response == "nj":
            print(data[30])
            break
        elif response == "new mexico" or response == "nm":
            print(data[31])
            break
        elif response == "new york" or response == "ny":
            print(data[32])
            break
        elif response == "north carolina" or response == "nc":
            print(data[33])
            break
        elif response == "north dakota" or response == "nd":
            print(data[34])
            break
        elif response == "ohio" or response == "oh":
            print(data[35])
            break
        elif response == "oklahoma" or response == "ok":
            print(data[36])
            break
        elif response == "oregon" or response == "or":
            print(data[37])
            break
        elif response == "pennsylvania" or response == "pa":
            print(data[38])
            break
        elif response == "rhode island" or response == "ri":
            print(data[39])
            break
        elif response == "south carolina" or response == "sc":
            print(data[40])
            break
        elif response == "south dakota" or response == "sd":
            print(data[41])
            break
        elif response == "tennessee" or response == "tn":
            print(data[42])
            break
        elif response == "texas" or response == "tx":
            print(data[43])
            break
        elif response == "utah" or response == "ut":
            print(data[44])
            break
        elif response == "vermont" or response == "vt":
            print(data[45])
            break
        elif response == "virginia" or response == "va":
            print(data[46])
            break
        elif response == "washington" or response == "wa":
            print(data[47])
            break
        elif response == "west Virginia" or response == "wv":
            print(data[48])
            break
        elif response == "wisconsin" or response == "wi":
            print(data[49])
            break
        elif response == "wyoming" or response == "wy":
            print(data[50])
            break
        else:
            print("Invalid Input, try again.")
            response = input("Please Choose a State to view its Electoral Votes and Party. ").lower()

    begin()


if __name__ == '__main__':
    begin()