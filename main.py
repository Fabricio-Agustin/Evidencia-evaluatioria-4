from modelo.helicoptero import Helicoptero
from utilidades.menu import mostrar_menu

def main():
    helicoptero = Helicoptero("Bell", "206")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print(helicoptero)
        elif opcion == "2":
            print(helicoptero.encender_motor())
        elif opcion == "3":
            print(helicoptero.despegar())
        elif opcion == "4":
            print(helicoptero.volar())
        elif opcion == "5":
            print(helicoptero.aterrizar())
        elif opcion == "6":
            print(helicoptero.apagar_motor())
        elif opcion == "7":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")

if __name__ == "__main__":
    main()