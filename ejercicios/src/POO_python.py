

class Empleados:
  
  def __init__(self, nombre, edad, salario):
    self.nombre= nombre
    self.edad= edad
    self.salario= salario
    
  def mostrar_info(self):
    return f'El empleado llamado {self.nombre} tiene {self.edad} años y cobra {self.salario} €'

  def calcular_bonificacion(self):
    print('La bonificación para el salario de {self.nombre} es:')
    return self.salario * 0.05
  def evaluar_desempeno ():
    return 'Evaluar desempeño por '
    
class Gerente(Empleados):
  def __init__(self, nombre, edad, salario, departamento):
    
    super().__init__(nombre, edad, salario)
    self.departamento= departamento
    
  def mostrar_info(self):
    return f'{super().mostrar_info()} y pertenece al departamento de {self.departamento}'
  
  def calcular_bonificacion(self):
    print('La bonificación para el salario de {self.nombre} es:')
    return self.salario * 0.10

class Ingeniero(Empleados):
  
  def __init__(self, nombre, edad, salario, especialidad):
    super().__init__(nombre, edad, salario)
    self.especialidad= especialidad

  def mostrar_info(self):
    return f'{super().mostrar_info()} con la especialidad en  {self.especialidad}'
  
  def calcular_bonificacion(self):
    print('La bonificación para el salario de {self.nombre} es:')
    return self.salario * 0.08
 