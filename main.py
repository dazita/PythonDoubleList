from DoubleList import DoubleLinkedList

def main():
    dll = DoubleLinkedList()

    print("🚀 Insertando elementos...")
    dll.insert(10)
    dll.insert(20)
    dll.insert(30)
    dll.insert(40)

    print("\n📋 Mostrando lista:")
    print(dll.show())

    print("\n🔄 Mostrando lista en reversa:")
    print(dll.show_reversed())

    print(f"\n📏 Tamaño de la lista: {dll.size()}")

    print("\n🔎 ¿Existe el 20 en la lista?")
    print(dll.exist(20))

    print("\n🗑️ Eliminando el elemento 20...")
    dll.remove(20)

    print("\n📋 Lista después de eliminar 20:")
    print(dll.show())

    print("\n📌 Obteniendo el valor en la posición 1:")
    print(dll.get(1))

if __name__ == "__main__":
    main()