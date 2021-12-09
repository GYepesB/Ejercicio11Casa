import bubble_sort as BS

while True:
    lista = list()
    fin = False
    while True:
        while True:
            e = input("Dime números: ")
            if e == "fin":
                fin = True
                break

            try:
                e = int(e)
                break
            except:
                print("El dato no es numérico: ")
        if fin:
            break
        if e == -9999:
            break

        lista.append(e)

    if fin:
        break


    lo = BS.BubbleSort(lista)
    print("Lista ordenada", lo.sorted_list)

