'''
En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:

* Color

* Ruedas

* Puertas

Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:

* Velocidad

* Cilindrada

Por último, tendrás que crear un objeto de la clase Coche y mostrarlo

'''

class Vehiculo:
	def __init__(self,color,ruedas,puertas):
		self.color = color
		self.ruedas = ruedas
		self.puertas = puertas


class Coche(Vehiculo):
	def __init__(self,velocidad,cilindrada,color,ruedas,puertas):
		super().__init__(color,ruedas,puertas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def infoCoche(self):
		print(f'velocidad:{self.velocidad}, cilindros:{self.cilindrada}, color:{self.color}, ruedas:{self.ruedas}, puertas:{self.puertas}')

mustang = Coche(120,8,"negro",4,4)

ferrari = Coche(160,12,"rojo",4,2)

mustang.infoCoche()

ferrari.infoCoche()
