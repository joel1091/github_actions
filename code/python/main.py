def sumar(a, b):
    """Función para sumar dos números"""
    return a + b


def mostrar_menu():
    """Muestra el menú de opciones al usuario"""
    print("\n===== CALCULADORA SIMPLE =====")
    print("1. Sumar")
    print("2. Restar (próximamente)")
    print("3. Multiplicar (próximamente)")
    print("4. Dividir (próximamente)")
    print("5. Salir")
    return input("\nSelecciona una opción (1-5): ")


def obtener_numeros():
    """Solicita dos números al usuario"""
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        return num1, num2
    except ValueError:
        print("Error: Por favor, introduce solo números.")
        return None, None


def main():
    """Función principal que ejecuta la calculadora"""
    while True:
        opcion = mostrar_menu()

        if opcion == '5':
            print("Gracias por usar la Calculadora Simple. ¡Hasta pronto!")
            break
        elif opcion == '1':
            num1, num2 = obtener_numeros()
            if num1 is not None and num2 is not None:
                resultado = sumar(num1, num2)
                print(f"El resultado de {num1} + {num2} = {resultado}")

        elif opcion in ['2', '3', '4']:
            print("Esta operación aún no está disponible. ¡Próximamente!")

        else:
            print("Opción no válida. Selecciona una opción entre 1 y 5.")


# Ejecutar la calculadora
if __name__ == "__main__":
    main()
