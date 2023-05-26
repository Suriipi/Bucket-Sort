def bucketSort(array):
    bucket = []

    # Cria baldes vazios
    for i in range(len(array)):
        bucket.append([])

    # Insere elementos em seus respectivos baldes
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Ordena os elementos de cada balde
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Pega os elementos ordenados
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


array = [.25, .32, .33, .52, .37, .47]
print("Array organizado do menor ao maior: ")
print(bucketSort(array))


    