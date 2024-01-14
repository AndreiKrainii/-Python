# TODO Напишите функцию find_common_participants

def find_common_participants(team1, team2, a=','):
    group_1 = set(team1.split(a))
    group_2 = set(team2.split(a))
    intersec = (list(group_1.intersection(group_2)))
    intersec.sort()
    return intersec

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, '|'))