name = 'David Mecalco'
course = 'Python'


#Metos para los str, como upperCase y loweCase
print(name.upper())
print(name.lower())

#Los metodos para str son inmutables
name_upper = name.upper()
print(name_upper)
print(name)

#Podemos comparar si son igual
print(name == name_upper)

#Capitalice se utiliza para poner la primera letra del texto en Mayúscula
words = 'curso de python'
print(words.capitalize())

#Title se utiliza para poner la primera letra de una palabra en Mayúscula
print(words.title())

#Eliminar espacios en un str utilizamos lstrip
words = '    hola David   '
print(words.lstrip())

#Para eliminar los espacios de la derecha sería rstrip
print(words.rstrip())

#Para eliminar todos los espacios s strip
print(words.strip())

#Para remplazar fragmentos de texto
text = 'Hola Java'
new_text = text.replace('Java', 'Python')
print(text)
print(new_text)

#Para separar texto utilizamos split
text = 'David,Mecalco,Python,Java'
data_list = text.split(',')
print(data_list[0])
print(data_list[1])
print(data_list[2])
print(data_list)

#Para convertir un a arreglo a un texto
data = ['David', 'Java', 'Python', 'Mecalco']
text = '/'.join(data)
print(text)

#Encontrar texto en una posición específica
text = 'Hola, David que tal'
print(text.find('David'))

#Para saber si un texto empieza y termina con:
text = 'Hola, mucho gusto David'
print(text.startswith('David'))
print(text.endswith('David'))

#Otros metodos para los str
number = '123456789'
decimal = '1.102312312'
text = 'Python'
mix = 'Python 3'

print(number.isnumeric())
print(decimal.isdigit())
print(decimal.isdecimal())
print(text.isalpha())
print(text.isalnum())