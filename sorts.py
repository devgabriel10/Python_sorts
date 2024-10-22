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