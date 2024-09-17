#mi lista con clases
class info:
    def milista(self):
        lista_nomperros=["boby","dollar","fany"]
        for x in lista_nomperros:
            print(x)
#mi tupla con clase
    def mitupla(self):
        tupla_colorperros=("blanco","negro","cafe")
        for i in tupla_colorperros:
            print(i)
#mi conjunto con clase
    def miconjunto(self):
        conjunto_razaperros={"dalmata","chihuahua","doberman"}
        for o in conjunto_razaperros:
            print(o)
#mi diccionario con clase
    def midiccionario(self):
        diccionario_datosperros={
            "nombre": "pepito",
            "edad": "2 años",
            "raza": "chihuahua"
        }
        for x,z in diccionario_datosperros.items ():
            print(x,z)
# creando el objeto 
datos=info()
print("--listado de nombres de perros--")
datos.milista()
print("--listado de colores de perros--")
datos.mitupla()
print("--listado de raza de perros--")
datos.miconjunto()
print("--listado de datos del perro--")
datos.midiccionario()

