numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

num_sum = sum(numbers[0:4])+sum(numbers[5:])
num_count = len(numbers)
num_average = num_sum/num_count
numbers[4] = num_average

print("Измененный список:", numbers)
