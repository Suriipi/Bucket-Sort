def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up: 
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up     
    return b     
              
def bucketSort(x):
    arr = []
    slot_num = 10 # 10 significa 10 espaços, cada
                  # espaço tem o tamanho de 0.1
    for i in range(slot_num):
        arr.append([])
          
    # Bota os elementos do vetor em baldes diferentes 
    for j in x:
        index_b = int(slot_num * j) 
        arr[index_b].append(j)
        
      # Ordena os valores dentro dos baldes indvidualmente
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
        
    # Concatena o resultado
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k += 1
            
    return x
  
x = [0.897, 0.565, 0.656,
     0.123, 0.665, 0.3434, 0.9, 0.178] 
print("Vetor ordenado é: ")
print(bucketSort(x))