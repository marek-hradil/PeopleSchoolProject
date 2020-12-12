MARKS = [
    'INFP',
    'ENFP',
    'INFJ',
    'ENFJ',
    'INTJ',
    'ENTJ',
    'INTP',
    'ENTP',
    'ISFP',
    'ESFP',
    'ISTP',
    'ESTP',
    'ISFJ',
    'ESFJ',
    'ISTJ',
    'ESTJ'
]


def mark_to_index(mark):
    return MARKS.index(mark.split('-')[0])

connection_table = [
    [0.75, 0.75, 0.75, 1, 0.75, 1, 0.75, 0.75, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.75, 0.75, 1, 0.75, 1, 0.75, 0.75, 0.75, 0, 0, 0, 0, 0, 0, 0, 0],
    [0.75, 1, 0.75, 0.75, 0.75, 0.75, 0.75, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 0.75, 1, 0, 0, 0, 0, 0, 0, 0],
    [0.75, 1, 0.75, 0.75, 0.75, 0.75, 0.75, 1, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25],
    [1, 0.75, 0.75, 0.75, 0.75, 0.75, 1, 0.75, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
    [0.75, 0.75, 0.75, 0.75, 0.75, 1, 0.75, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 1],
    [0.75, 0.75, 1, 0.75, 1, 0.75, 0.75, 0.75, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25],
    [0, 0, 0, 1, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.5, 1, 0.5, 1],
    [0, 0, 0, 0, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 1, 0.5, 1, 0.5],
    [0, 0, 0, 0, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 0.5, 1, 0.5, 1],
    [0, 0, 0, 0, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.25, 1, 0.5, 1, 0.5],
    [0, 0, 0, 0, 0.25, 0.5, 0.25, 0.25, 0.5, 1, 0.5, 1, 0.75, 0.75, 0.75, 0.75],
    [0, 0, 0, 0, 0.25, 0.5, 0.25, 0.25, 1, 0.5, 1, 0.5, 0.75, 0.75, 0.75, 0.75],
    [0, 0, 0, 0, 0.25, 0.5, 0.25, 0.25, 0.5, 1, 0.5, 1, 0.75, 0.75, 0.75, 0.75],
    [0, 0, 0, 0, 0.25, 0.5, 1, 0.25, 1, 0.5, 1, 0.5, 0.75, 0.75, 0.75, 0.75],
]

def get_connection_rating(mark1, mark2):
    return connection_table[mark_to_index(mark1)][mark_to_index(mark2)]

def get_person_connectivness(person, people, treshhold = 0):
    rating = 0
    for friend in people:
        connection_rating = get_connection_rating(person.mark, friend.mark)
        if (connection_rating > treshhold):
            rating += connection_rating

    return rating