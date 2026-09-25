"""Сортировка списка методом пузырька."""


def bubble_sort(items):
    arr = items.copy()
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr



if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("До сортировки:", data)
    print("После сортировки:", bubble_sort(data))
