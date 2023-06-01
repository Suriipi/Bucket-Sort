def quick_sort(v, inicio, fim):
    if inicio < fim:
        pivo = particao(v, inicio, fim)
        quick_sort(v, inicio, pivo - 1)
        quick_sort(v, pivo + 1, fim)

def particao(v, inicio, fim):
    pivo = v[inicio]
    esq = inicio + 1
    dir = fim
    while True:
        while esq <= dir and v[esq] <= pivo:
            esq += 1
        while dir >= esq and v[dir] >= pivo:
            dir -= 1
        if dir < esq:
            break
        else:
            v[esq], v[dir] = v[dir], v[esq]
    v[inicio], v[dir] = v[dir], v[inicio]
    return dir

def insertion_sort(v):
    for i in range(1, len(v)):
        chave = v[i]
        j = i - 1
        while j >= 0 and v[j] > chave:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = chave

def selection_sort(v):
    for i in range(len(v)):
        min_idx = i
        for j in range(i + 1, len(v)):
            if v[j] < v[min_idx]:
                min_idx = j
        v[i], v[min_idx] = v[min_idx], v[i]

def bubble_sort(v):
    n = len(v)
    for i in range(n):
        for j in range(n - i - 1):
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]

def shell_sort(v):
    n = len(v)
    h = 1
    while h < n // 3:
        h = 3 * h + 1
    while h >= 1:
        for i in range(h, n):
            j = i
            while j >= h and v[j] < v[j - h]:
                v[j], v[j - h] = v[j - h], v[j]
                j -= h
        h //= 3

v = [3, 5, 1, 4, 9, 13, 0, 2, 8, 5]

print("Quick Sort:")
quick_sort(v, 0, len(v) - 1)
print(v[:3])

v = [3, 5, 1, 4, 9, 13, 0, 2, 8, 5]

print("Insertion Sort:")
insertion_sort(v)
print(v[:3])

v = [3, 5, 1, 4, 9, 13, 0, 2, 8, 5]

print("Selection Sort:")
selection_sort(v)
print(v[:3])

v = [3, 5, 1, 4, 9, 13, 0, 2, 8, 5]

print("Bubble Sort:")
bubble_sort(v)
print(v[:3])

v = [3, 5, 1, 4, 9, 13, 0, 2, 8, 5]

print("Shell Sort:")
shell_sort(v)
print(v[:3])


