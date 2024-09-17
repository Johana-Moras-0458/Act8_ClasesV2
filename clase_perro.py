print("clases version 2 el constructor")

class perro:
    # funcion constructor
    def __init__(self,color,edad):
        self.color=color
        self.edad=edad
    #funciones creadas por el usuario
    def muerde(self):
        print("chale el perro me mordio")
    def chatperro(self,mensaje):
        print(f"chat perro: {mensaje}")
    def chaperra(self,mensajep):
        print(f"chat perro: {mensajep}")
    def datos(self):
        print(f"color: {self.color} edad: {self.edad} ")
# crear el objeto
chihuas=perro("negro",2)
# llamadasa funciones
chihuas.datos()
chihuas.muerde()
chihuas.chatperro("hola canina")
chihuas.chaperra("hola boby")
chihuas.chatperro("quieres ser mi chava ?")
chihuas.chaperra("grrruu....")