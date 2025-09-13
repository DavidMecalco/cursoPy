
#Las variables, de forma explicita asigna el valor de una varible

#Tipo int
age = 40

#Tipo str
name = 'David'

#Tipo

#Python es fuertemente tipado, lo que no permite concatenate tipos de datos diferentes, ejemplo:
# print(name + 'tiene' + age + 'años'), esto no se puede, ya que tenemos dos varibales diferentes una int (age) y otra str (name) lo que tenemos que hacer es castear la variable int a str, así:
print(name + ' tiene ' + str(age) + ' años')


#Otra forma de hacer un cast es a de un str a un int
number_str = '30'
number = int(number_str)
print(50 + number)
print(50 - number)
print(50 / number)
print(50 * number)

#Podemos reasignar las variables
x = 10
print(x)
x = 'Hola'
print(x)
