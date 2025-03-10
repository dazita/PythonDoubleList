from DoubleList import DoubleLinkedList

def main():
    dll = DoubleLinkedList()
    
    # Insertar elementos
    dll.insert(10)
    dll.insert(20)
    dll.insert(30)
    dll.insert(40)
    print("Lista después de insertar elementos:")
    print(dll.show())
    
    # Verificar existencia
    print("\n¿Existe el 20 en la lista?:", dll.exist(20))
    print("¿Existe el 50 en la lista?:", dll.exist(50))
    
    # Obtener tamaño de la lista
    print("\nTamaño de la lista:", dll.size())
    
    # Acceder a un elemento por índice
    try:
        print("Elemento en la posición 2:", dll.get(2))
    except IndexError as e:
        print(e)
    
    # Mostrar lista en orden inverso
    print("\nLista en orden inverso:")
    print(dll.show_reversed())
    
    # Eliminar un elemento
    dll.remove(20)
    print("\nLista después de eliminar 20:")
    print(dll.show())
    
    # Recorrer con iterador
    print("\nRecorrido con iterador:")
    for item in dll:
        print(item, end=' -> ')
    print("None")
    
if __name__ == "__main__":
    main()
