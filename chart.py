import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from Person import Person
import connections
import math

def draw_stat_bar_chart(people, key, title):
    people_sorted = sorted(people, key=key)
    height = [key(person) for person in people_sorted]
    bars = [person.name for person in people_sorted]
    colors = ['blue' if person.gender == 'M' else 'red' for person in people_sorted]
    y_pos = np.arange(len(bars))

    plt.title(title)
    plt.barh(y_pos, height)
    plt.yticks(y_pos, bars)

    plt.savefig(f'./assets/{title}.svg', format='svg')
    plt.clf()

def draw_class_ratio_chart(people):
    properties = {
        'Extroverze': 0,
        'Introverze': 0,
        'Smysly': 0,
        'Intuice': 0,
        'Mysleni': 0,
        'Citeni': 0,
        'Usuzovani': 0,
        'Vnimani': 0,
    }

    for person in people:
        properties['Extroverze'] += person.extrovert
        properties['Introverze'] += person.introvert
        properties['Smysly'] += person.visionary
        properties['Intuice'] += person.realistic
        properties['Mysleni'] += person.logic
        properties['Citeni'] += person.empathic
        properties['Usuzovani'] += person.planning
        properties['Vnimani'] += person.searching

    sorted_properties_items = sorted(properties.items(), key=lambda t: t[1])

    height = [value / len(people) for _, value in sorted_properties_items]
    bars = [name.capitalize() for name, _ in sorted_properties_items]
    y_pos = np.arange(len(bars))

    plt.title('Průměrné hodnoty')
    plt.barh(y_pos, height)
    plt.yticks(y_pos, bars)

    plt.savefig(f'./assets/PrumerneHodnoty.svg', format='svg')
    plt.clf()

def draw_class_network(people, density = 0):
    G = nx.Graph()
    for person1 in people:
        for person2 in people:
            rating = connections.get_connection_rating(person1.mark, person2.mark)
            if rating > density:
                length = math.pow(rating, 2)
                G.add_edge(person1.name, person2.name, length=length)

    pos = nx.spring_layout(G, k=0.55, iterations=50)
    nx.draw(G, pos, with_labels=True, node_color='red', edge_color='green')
    plt.savefig(f'./assets/Network_{density}.png')
    plt.clf()

def draw_most_connected_people(people, treshhold = 0):
    people_map = {}
    for person in people:
        rating = connections.get_person_connectivness(person, people, treshhold)
        people_map[person.name] = rating

    sorted_people_map = sorted(people_map.items(), key=lambda t: t[1]) 

    height = [value for _, value in sorted_people_map]
    bars = [name.capitalize() for name, _ in sorted_people_map]
    y_pos = np.arange(len(bars))

    plt.title('Nejvíce propojení lidé')
    plt.barh(y_pos, height)
    plt.yticks(y_pos, bars)

    plt.savefig(f'./assets/Connections_{treshhold}.png')
    plt.clf()

def draw_types(people):
    people_types = {}

    for mark in connections.MARKS:
        people_types[mark] = 0

    for person in people:
        people_types[person.mark_simple] += 1

    sorted_types_map = sorted(people_types.items(), key=lambda t: t[1])

    height = [value for _, value in sorted_types_map]
    bars = [mark.capitalize() for mark, _ in sorted_types_map]
    y_pos = np.arange(len(bars))

    plt.title('Typy')
    plt.barh(y_pos, height)
    plt.yticks(y_pos, bars)

    plt.savefig(f'./assets/Types.png')
    plt.clf()

def draw_bars(people):
    class_types = {
        'INFP': [16.40, 0],
        'ENFP': [11.83, 0],
        'INFJ': [8.06, 0],
        'INTP': [10.04, 0],
        'ENTP': [6.99, 0],
        'INTJ': [6.10, 0],
        'ISFJ': [4.90, 0],
        'ESFJ': [5.38, 0],
        'ESTJ': [4.20, 0],
        'ENFJ': [5.11, 0],
        'ISFP': [3.93, 0],
        'ISTJ': [4.04, 0],
        'ENTJ': [3.44, 0],
        'ESFP': [3.79, 0],
        'ESTP': [2.85, 0],
        'ISTP': [2.94, 0],
    }

    for person in people:
        class_types[person.mark_simple][1] += 1

    sorted_types = sorted(class_types.items(), key=lambda t: t[1][0])

    labels = [label for label, _ in sorted_types]
    men_means = [((values[1] / len(people)) * 100) for label, values in sorted_types]
    women_means = [values[0] for label, values in sorted_types]

    print(men_means)
    print(women_means)

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    fig.set_size_inches(8.5, 5.5)
    rects1 = ax.bar(x - width/2, men_means, width, label='Třída')
    rects2 = ax.bar(x + width/2, women_means, width, label='ČR')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Procentuální výskyt')
    ax.set_title('Výskyty jednotlivých typů osobností')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.savefig(f'./assets/Bars.svg', format='svg')
    plt.clf()

def draw_types_pie(people):
    people_types = {}

    for person in people:
        if (people_types.get(person.mark_simple)):
            people_types[person.mark_simple] += 1
        else:
            people_types[person.mark_simple] = 1

    labels = [label for label, _ in people_types.items()]
    sizes = [count for _, count in people_types.items()]

    _, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')

    plt.savefig(f'./assets/TypesPie.svg', format="svg")
    plt.clf()