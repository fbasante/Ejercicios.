#Tipos de datos.

#Boolean.

#boolean1=True
#boolean2=False

#if(boolean1):
    print("Usuario "Pachón" válido")
#else:
        #print("Usuario inválido")

# Enteros, flotante.

a=1
b=3.0
print(a,b)

# Listas.

listado_numeros=[1, 2, 3, 4, 5, 6, 7]
print(a)
elemento= listado_numeros[2]
print(elemento)

#slice= listado_numeros[3:5]
#print ("rebanada =", slice)

listado_strings=["a", "2", "d", "e", "k", "l", "u"]
print("listado_strings=", listado_strings)
print("impresion del 3ro al último elemento del listado", listado_strings[2:7])
print("impresion del 2do al último elemento del listado", listado_strings[1:])
print("impresion del 2do al cuarto elemento del listado", listado_strings[0:4:2])

listado_numeros.append(1000)
listado_numeros.pop()
print(listado_numeros)
print(listado_numeros.count(1))
listado_numeros.reverse()
print(listado_numeros)

lista=[i for i in range (2, 100, 3)]
lista2=lista.copy()
lista.reverse()
#print("lista original =", lista[0:10])
#print("lista copia", lista2[0:10])

#strings
string1="Hola curso informatica II:"
string2=string1.replace("a","X")
print("string1=" , string1)
print("string2=" , string2)

string3=string2.capitalize()
print("string capitalize=", string3)

print("metodo upper () =>","anita lava la tina", upper())
print("metodo lower () =>","anita lava la tina", lower())
print("metodo split () =>","anita lava la tina".split("a"))
print ("corazón valiente"[3:9])

strin="corazon valiente"
#strin[0]="d"

#diccionarios

diccionario1={"house": "casa", "car": "carro", "sky": "cielo"}
print(diccionario1)
print(diccionario1["house"])
print(diccionario1["sky"])
print("claves => ", diccionario1.keys())
print("valores => ", diccionario1.values())