#Comillas dobles o simples, es un tema de estilo y convenience, estándar es un uso de comillas simples ''
  
text = "Hola, Python"
text2 = "Hola, Python"

#Podemos comprar si es lo mismo un str con comillas simples y comillas dobles
result = text2 == text
print(result)

#Así, comprobamos que un str con '' o "" es igual, el uso de uno de otro solo estilo

#No podemos utilizar ' dentro de una cadena de str amenos que sea con un \', ejemplo:
mensaje = 'El código es de los usuarios\'s'
print(mensaje)

#Otra opción es utilizar "" para utilizar ' en un str

mensaje2 = "Hola, Python's"
print(mensaje2)

#palabras compuestas por 2 o más se separan con __
text_multi_line = 'Hola, Python'
print(text_multi_line)


#para str que sea multilínea necesitamos agregar '' o "" 3 veces
text_multi_line2 = """
Hola, Python
Esto es un str multilínea
saludos
"""

print(text_multi_line2)
