list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

team_index = len(list_players) // 2

team_a = list_players[:team_index]
print( team_a)
team_b = list_players[team_index:]
print( team_b)
