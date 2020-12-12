'''
Python zde je hrozně ugly, tak si moc nedělej závěry, řekl bych že dokážu psát lepší kód :D (hlavně ne Python teda)
'''

import matplotlib as mt
import chart
from Person import Person

people = []
with open('./people.csv') as data:
    lines = data.readlines()[1:]
    
    for (index, line) in enumerate(lines):
        people.append(Person(line.split(',')))

'''
chart.draw_class_network(people, 0)
chart.draw_class_network(people, 0.25)
chart.draw_class_network(people, 0.5)
chart.draw_class_network(people, 0.75)

chart.draw_most_connected_people(people, 0)
chart.draw_most_connected_people(people, 0.25)
chart.draw_most_connected_people(people, 0.5)
chart.draw_most_connected_people(people, 0.75)

chart.draw_types(people)
chart.draw_types_pie(people)
chart.draw_class_ratio_chart(people)

'''

chart.draw_stat_bar_chart(people, lambda p: p.extrovert, 'Extroverze')
chart.draw_stat_bar_chart(people, lambda p: p.introvert, 'Introverze')
chart.draw_stat_bar_chart(people, lambda p: p.visionary, 'Smysly')
chart.draw_stat_bar_chart(people, lambda p: p.realistic, 'Intuice')
chart.draw_stat_bar_chart(people, lambda p: p.logic, 'Myšlení')
chart.draw_stat_bar_chart(people, lambda p: p.empathic, 'Cítění')
chart.draw_stat_bar_chart(people, lambda p: p.planning, 'Usuzování')
chart.draw_stat_bar_chart(people, lambda p: p.searching, 'Vnímání')
chart.draw_stat_bar_chart(people, lambda p: p.assertitive, 'Průbojní')
chart.draw_stat_bar_chart(people, lambda p: p.careful, 'Opatrní')

# chart.draw_class_ratio_chart(people)




