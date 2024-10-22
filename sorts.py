# Métodos de Ordenação!

def selection_sort(list):
    n = len(list)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if list[i] < list[min_index]:
                min_index = i
        if list[j] > list[min_index]:
            aux = list[j]
            list[j] = list[min_index]
            list[min_index] = aux


def bubble_sort(list):
    n = len(list)
    for j in range(n-1):
        for i in range(n-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]


def insertion_sort(list):
    n = len(list)
    for i in range(1, n):
        key = list[i]
        j = i - 1
        while j >= 0 and list[j] > key:
            list[j+1] = list[j]
            j = j - 1
        # j + 1, pois o j foi decrementado como condição de parada do while.
        list[j+1] = key