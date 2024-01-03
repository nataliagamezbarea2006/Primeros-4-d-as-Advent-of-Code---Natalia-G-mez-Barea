suma_numeros_combinados = 0  

with open('1-a.txt', 'r') as archivo:
    lineas = archivo.readlines()  

for linea in lineas:
    primer_numero = ""
    ultimo_numero = ""

    for caracter in linea:
        if caracter.isdigit():
            if primer_numero == "":
                primer_numero = caracter
            ultimo_numero = caracter

    if primer_numero != "" and ultimo_numero != "":
        numeros_combinados = int(primer_numero + ultimo_numero)  
        suma_numeros_combinados += numeros_combinados  
        
print(f"La suma de todos los números combinados es: {suma_numeros_combinados}")
