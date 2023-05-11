import copy
import selection_sort as SelectionSort
import bubble_sort as BubbleSort

arranjo1 = [42, 3, 7, 12, 20, -1, 0]
print(f'Entrada: {arranjo1}')
SelectionSort.ordene(arranjo1)
print(f'Arranjo ordenado (Selection sort): {arranjo1}')
arranjo2 = copy.deepcopy(arranjo1)
print(f'Arranjo ordenado (Bubble sort): {arranjo2}')
