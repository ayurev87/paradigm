from typing import List


def binary_search(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 3, 4,  6, 7, 8, 10, 13, 14]
target = 4
result = binary_search(arr, target)
print(f"Исходный список: {arr}")
print(f"Цель: {target}")
if result == -1:
    print("Искомый элемент не найден")
else:
    print(f"Искомый элемент найден по индексу {result}")
