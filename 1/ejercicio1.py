# variables iniciales
total=0 
# 2. Abrir el archivo 'input.txt'en lectura (r) y guardar en una variable el contenido
with open('archivo.txt', 'r') as file:
    for linea in file:  
        for caracter in linea: 
            número = ""  
            caracteres = ""
            print("El contenido del caracter es " + caracter)
            
            # Saber si es un valor numérico o con letras
            if caracter.isdigit():
                print("Es un número")
            else:
                print("No es un número")
            
            if caracter.isalpha():
                print("Es una letra")
            else:
                print("No es una letra")



#     a. Inicializar una variable 'number' como una cadena vacía.
#     b. Iterar a través de cada carácter 'c' en la línea:
#         i. Si 'c' es un dígito numérico, añadirlo a 'number'.
#     c. Verificar la longitud de 'number':
#         i. Si es 1, duplicar el dígito ('number = number + number').
#         ii. Si es mayor a 1, asignar a 'number' el primer y último dígito ('number = number[0] + number[-1]').
#     d. Convertir 'number' a entero.
#     e. Agregar 'number' al 'total'.
# 4. Cerrar el archivo.
# 5. Imprimir el valor final de 'total'.

# https://www.youtube.com/watch?v=UT4_ZgdeRTM
# https://www.youtube.com/watch?v=YEWxlbffgxE