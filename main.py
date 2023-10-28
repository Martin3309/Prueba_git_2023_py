#Creacion de clase
class Persona:
    def __init__(self,nombre, apellido, edad) -> None:
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
#Creacion de metodos

#Creacion metodo get
    @property
    def nombre(self):
        print("Usando metodo Get")
        return self._nombre
#Creacion de metodo set
    @nombre.setter
    def nombre(self,nombre2):
        self._nombre = nombre2
        print("Usando metodo Set")

    @property
    def apellido(self):
        print("Usando metodo Get")
        return self._apellido
        
    @apellido.setter
    def apellido(self,apellido2):
        self._apellido = apellido2
        print("Usando metodo Set")

    @property
    def edad(self):
        print("Usando metodo Get")
        return self._edad
        
    @edad.setter
    def edad(self,edad2):
        self._edad = edad2
        print("Usando metodo Set")
#Metodo para mostrar clase
    def mostrar(self):
        print(f"Nombre: {self._nombre} // Apellido: {self._apellido} // Edad: {self._edad}")
#Metodo para eliminar clase, casi no se usa
    def __del__(self):
        print(f"Eliminando objeto: {self.nombre} {self.apellido}")

#Esta condicion se usa cuando quiero saber cual es el archivo principal.
#Si name == main entonces ejecutar eso, para no ejecutar en los dos archivos.

if __name__ == "__main__":
    persona1 = Persona("Martin", "Bravo",25)
    persona1.mostrar()
    print(__name__) #Muestra si estamos posicionados.

