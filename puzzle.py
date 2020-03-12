numero_original= 58184241583791680
multiplicador_17cifras=100000000000000000
divisor= 2017
resto_no_repetido=True
contador_iteraciones=0
resto = 0
lista_restos=[resto]
lista_restos_str=str(lista_restos)

def setResto():
    resto = 0
    lista_restos=[resto]
    return 


while resto_no_repetido:
    contador_iteraciones+=1
    resto_mas_numero_original = (resto * multiplicador_17cifras) + numero_original
    resto = resto_mas_numero_original % divisor
    resto_como_elem_lista=[resto]
    if str(resto_como_elem_lista) in lista_restos_str or contador_iteraciones>100000:
        resto_no_repetido=False
        print("Cantidad de iteraciones para que se repita un resto ", contador_iteraciones)
        print("Resto repetido ", resto)
    else:
        lista_restos_str= lista_restos_str + str(resto_como_elem_lista)
        
        
iteraciones_remanentes = numero_original % contador_iteraciones
setResto()
lista_restos_str = str(lista_restos)
 

for i in range(0,iteraciones_remanentes):
    resto_mas_numero_original = (resto * multiplicador_17cifras) + numero_original
    resto= resto_mas_numero_original % divisor
    resto_como_elem_lista=[resto]
    lista_restos_str= lista_restos_str + str(resto_como_elem_lista)
    #resto_mas_numero_original = (resto * multiplicador_17cifras) + numero_original


print("Después de los ciclos repetidos quedan " + str(iteraciones_remanentes) + " iteraciones")
print("El Resto final de la división es: ", resto)


if "[1625]" in lista_restos_str:
    print("Encontrado en: ", lista_restos_str.index("[1625]"))
else:
    print("El resultado propuesto por otro programador (1625) no fue encontrado entre los restos de las iteraciones iteraciones_remanentess")

        
        
        

