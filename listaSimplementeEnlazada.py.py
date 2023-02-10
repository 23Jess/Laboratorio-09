class Nodo():
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular():
    def __init__(self):
        self.primero = None
        self.ultimo = None 
    
    #Nos retornará si la lista está vacía
    def Vacia(self):
        return self.primero == None 

    #Método de agregar al inicio
    def AgregarInicio(self,dato):
        if  self.Vacia(): #Si la lista está vacía, inserta el primer dato
            self.primero = self.ultimo = Nodo(dato)
            self.ultimo.siguiente = self.primero
        else: #Si no está vacía, guarda el dato ingresado en la variable aux
            aux = Nodo(dato)
            aux.siguiente = self.primero 
            self.primero = aux 
            self.ultimo.siguiente = self.primero 

    #Método para agregar al final de la lista
    def AgregarFinal(self,dato):
        if self.Vacia(): #Se agrega un elemento a la lista
            self.primero = self.ultimo = Nodo(dato) 
            self.ultimo.siguiente = self.primero 
        else: 
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato) 
            self.ultimo.siguiente = self.primero 

    #Eliminar al primero de la lista
    def EliminarInicio(self):
        if self.Vacia():
            print("Lista Vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None 
        else:
            self.primero = self.primero.siguiente 
            self.ultimo.siguiente = self.primero 

    #Eliminar al final de la lista
    def EliminarFinal(self):
        if self.Vacia():
            print("Lista vacía")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None 
        else:
            aux = self.primero 
            while aux.siguiente != self.ultimo:
                aux = aux.siguiente 
            aux.siguiente = self.primero 
            self.ultimo = aux 


    #Método para recorrer y mostrar la lista con los elementos
    def Recorrer(self):
        aux = self.primero 
        while aux.siguiente != self.primero:
            print(aux.dato)
            aux = aux.siguiente
        print(aux.dato) 



try:
    if __name__ == "__main__":
        opcion = 0
        lista = ListaCircular()
        while opcion != 7:
            print("Lista Circular:\n 1. ¿Está vacía la lista?\n 2. Agregar Inicio\n 3. Agregar Final\n 4. Eliminar Inicio\n 5. Eliminar Final\n 6. Mostrar\n 7. Salir")
            opcion = int(input("Ingrese su opción "))

            if opcion == 1:
                print("SI" if lista.Vacia() else "NO")

            elif opcion == 2:
                dato = input("Ingresa un número ")
                lista.AgregarInicio(dato)

            elif opcion == 3:
                dato = input("Ingresa un número ")
                lista.AgregarFinal(dato)

            elif opcion == 4:
                lista.EliminarInicio()

            elif opcion == 5:
                lista.EliminarFinal()
            
            elif opcion == 6:
                lista.Recorrer()

            elif opcion == 7:
                print("Fin")
            else:
                print("Ingresaste una opción errónea, vuelve a intentarlo.")
except Exception as e:
    print(e)