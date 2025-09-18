#Extraer Partes específicas de un str con Slicing, no es un método

text = 'David Mecalco'
print(text[0:7:1])
print(text[0:4:2])

#Desde el comienzo hasta
print(text[:2])

#Desde el princio hasya el final
print(text[::])

#Reversa o inversa
print(text[::-1])

#Ejemplo
text = 'Anita lava la tina'
print(text)
print(text[::-1])