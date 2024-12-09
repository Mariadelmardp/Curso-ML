

lista_precios=[21,23,55,59,89]
lista_precios_caros=[]
lista_precios_baratos= []
umbral_precio= 0
suma_precio= 0

print(f'La longitud de lista_precios es {len(lista_precios)}')
for precio in lista_precios:
  suma_precio += precio
umbral_precio = suma_precio/len(lista_precios)

for precio in lista_precios:
  if precio < umbral_precio:
    lista_precios_caros.append(precio)
  else:
    lista_precios_baratos.append(precio)
print(f'La lista de precios caros es: {lista_precios_caros} \nLa lista de precios baratos es: {lista_precios_baratos}')

for i, precio in enumerate(lista_precios, start=1):
  print(f'El precio {i} es:{precio}')

print(f'La suma de los precios es {suma_precio}' )
print(f'La media de los precios es {umbral_precio}')


print('________________________________Bucles While___________________________\n') 

#Crear una contraseña segura
while True:
    contraseña = input('Por favor, introduzca una contraseña segura:')
    longitud= len(contraseña)>=6
    mayuscula= False
    minusculas= False
    numero = False
    for caracter in contraseña:
      if caracter.isupper():
        mayuscula=True
      elif caracter.islower():
        minusculas=True
      elif caracter.isdigit():
        numero=True
    if longitud and mayuscula and minusculas and numero:
      print(f'Contraseña segura')
      break
    else:
      print('Contraseña no es segura')   

# Sacar las edad superiores a un rango

lista_edades= [23, 25, 15, 98, 56, 78, 44, 42, 63, 4, 29]

for edad in lista_edades:
  if edad > 65:
    continue
    pass
    break

