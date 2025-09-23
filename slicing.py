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

#Otros ejemplos para el Slicing de Strings
text = 'Hola Mundo'
print(text[0:4])
print(text[:4])
print(text[2:])
print(text[::3])

text = 'Hola Mundo'
new_text = text[:5] + text[5:].replace('Hola','Python')
print(new_text)

text = 'Python es genial'
parts = text.split()
parts2 = parts[:2]
print(parts)
print(parts2)
parts_reverse = parts[::-1]
print(parts_reverse)

text_reverse = ' '.join(parts_reverse)
print(text_reverse)
