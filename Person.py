def split_stat(stat):
    stats = stat.split('/')
    return (int(stats[0]), int(stats[1]))


class Person:
    def __init__(self, line):
        mark = line[6].split('(')[0]
    
        self.name = line[0]
        self.extrovert, self.introvert = split_stat(line[1])
        self.visionary, self.realistic = split_stat(line[2])
        self.logic, self.empathic = split_stat(line[3])
        self.planning, self.searching = split_stat(line[4])
        self.assertitive, self.careful = split_stat(line[5])
        self.mark = mark
        self.mark_name = line[6].split('(')[1].split(')')[0]
        self.mark_simple = mark.split('-')[0]
        self.gender = line[7][0]