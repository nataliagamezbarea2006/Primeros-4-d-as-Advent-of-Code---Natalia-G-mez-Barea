# variables iniciales
total=0 
número = ""  
#2.Definir función para procesar cada línea y obtener el número
def procesar_linea(linea):
    numero = ""
    for linea in line:
        if linea.isnumeric():
            numero += linea
    if len(numero) == 1:
        numero = numero + numero
    else:    
        #suma el primer número que haya y el último
        numero = numero[0] + numero[-1]

    return int(numero)
    
#3. Abrir el archivo 'input.txt'en lectura (r) y guardar en una variable el contenido
with open('archivo.txt', 'r') as input_file:
    for line in input_file:
        numero = procesar_linea(line)
        total += numero

# Imprimir el número total
print("El número total es:", total)
