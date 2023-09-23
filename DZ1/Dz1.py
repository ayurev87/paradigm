# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
def sort_List_imperativnyi(numbers):
   for i in range(len(numbers)):
      maxNum = i
      for j in range(i+1, len(numbers)):
         if numbers[i] > numbers[maxNum]:
            maxNum =j
            numbers[i], numbers[maxNum] = numbers[maxNum], numbers[i]

numbers = [ 4 ,3, -2, 6, -1 , -4, 1]
sort_List_imperativnyi(numbers)
print(numbers)

# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле
# Пример процедуры для сортировки списка чисел в порядке убывания, используя алгоритм сортировки выбором:

def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)
numbers = [ 4 ,3, -2, 6, -1 , -4, 1]
sorting = sort_list_declarative(numbers)
print(sorting)   