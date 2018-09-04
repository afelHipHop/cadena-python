class producto(object):
	def solicitud(self, producto):
		#Solictud del cliente
		pass

class ataque(producto):
	def __init__(self, p=producto()):
		self.__tipoSolicitud = 1
		self.__producto=p
	def solicitud(self, solicitud):
		if (solicitud==self.__tipoSolicitud):
			print("Comprando un arma")
		else:
			self.__producto.solicitud(solicitud)

class defensa(producto):
	def __init__(self, p=producto()):
		self.__tipoSolicitud = 2
		self.__producto=p
	def solicitud(self, solicitud):
		if (solicitud==self.__tipoSolicitud):
			print("Comprando un escudo")
		else:
			self.__producto.solicitud(solicitud)

class pocion(producto):
	def __init__(self):
		self.__tipoSolicitud = 3
	def solicitud(self, solicitud):
		print("Comprando un restaurador de hp y mana")


producto=producto()
pocion=pocion()
defensa=defensa(pocion)
ataque=ataque(defensa)

print("========================================================")
print("== BIENVENIDO A LA TIENDA, ¿QUE LE GUSTARIA COMPRAR?  ==")
print("== 				1. ARMA							 	  ==")
print("==				2. ESCUDO							  ==")
print("==				3. RESTAURADOR DE HP Y MANA 		  ==")
print("========================================================")
ataque.solicitud(1)
ataque.solicitud(2)
ataque.solicitud(3)