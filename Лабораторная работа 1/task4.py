users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений

enters = len(users)
unique_users = set(users)
unique_enters = len(unique_users)

dictionary = {"Общее количество": enters, "Уникальные посещения": unique_enters}
print(dictionary)