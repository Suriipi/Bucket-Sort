def cycleSort(array):
  writes = 0
   
  # Varre o vetor para achar ciclos
  for cycleStart in range(0, len(array) - 1):
    item = array[cycleStart]
     
    # Acha onde o valor deve ser colocado
    pos = cycleStart
    for i in range(cycleStart + 1, len(array)):
      if array[i] < item:
        pos += 1
        
     
    # Se o valor ja está lá, isso não é um ciclo
    if pos == cycleStart:
      continue
     
    # Posiciona o valor logo após o valor duplicado
    while item == array[pos]:
      pos += 1
    array[pos], item = item, array[pos]
    writes += 1
     
    # Rotaciona o resto do ciclo
    while pos != cycleStart:
       
      # Acha onde o valor deve ser colocado
      pos = cycleStart
      for i in range(cycleStart + 1, len(array)):
        if array[i] < item:
          pos += 1
       
      # Posiciona o valor logo após o valor duplicado
      while item == array[pos]:
        pos += 1
      array[pos], item = item, array[pos]
      writes += 1
      print(array)
   
  return writes
   
arr = [1, 8, 3, 9, 10, 10, 2, 4 ]
n = len(arr)
cycleSort(arr)
 
print("Vetor ordenado: ")
for i in range(0, n) :
    print(arr[i], end = ' ')
 
