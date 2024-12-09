
# *args, **kwargs

## Crear una lista de palabras y usa la función lambda para quedarte solo con las palabras que empiecen con "A".
lista_palabras=['perro', 'gato', 'ardilla', 'hamster', 'conejo', 'armadillo', 'albatros']
lista_a= []

for animal in lista_palabras:
  animal_con_a=(lambda animal_a: animal_a if animal_a[0] =='a' else '')(animal)
  if len(animal_con_a)>0:
    lista_a.append(animal_con_a)
print(lista_a)

# Funciones de orden superior   map, filter, reduce


