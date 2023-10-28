#Del archivo main se importa la clase creada en este
from main import Persona

#metodo center para ponerle 50 "-" a los dos lados.
print(f"Creando objeto".center(50,"-"))

persona1 = Persona("Hola","Mundo",25)
persona1.mostrar()

print(__name__)

persona1.__del__