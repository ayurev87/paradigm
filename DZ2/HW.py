# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

print ('Ввод число')
n = int(input())
for i in range(1,n+1 ):
    for j in range(1, n+1):
        print("{0} * {1} = {2}".format(i,j, i*j))
    print("")
#структурная парадигма: goto нету. все конструкции используются, а процедурная парадигма  нету функции. 