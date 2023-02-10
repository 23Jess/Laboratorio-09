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


    #Método para recorrer para mostrar la lista
    def Recorrer(self):
        aux = self.primero 
        while aux.siguiente != self.primero:
            print(aux.dato)
            aux = aux.siguiente
        print(aux.dato) 

lista = ListaCircular()

lista.AgregarFinal(1)
lista.AgregarFinal(5)
lista.AgregarFinal(8)
lista.AgregarFinal(12)
lista.AgregarFinal(23)

lista.AgregarInicio(2)
lista.AgregarInicio(50)

lista.AgregarFinal(42)

lista.EliminarInicio()
lista.EliminarFinal()

lista.Recorrer()


