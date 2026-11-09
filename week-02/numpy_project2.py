import numpy as np

one = np.ones((5,5)) #Создаём единичную матрицу 5 на 5
result = one + np.eye(5) #Добавляем сложение по диагонали
print(result)
#Срез первых двух строчек
print(one[0:2])