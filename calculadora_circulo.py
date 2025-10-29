import math

def area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    
    Parámetros:
        radio (float): El radio del círculo. Debe ser un número positivo.
        
    Retorna:
        float: El área del círculo.
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    
    return math.pi * (radio ** 2)

if __name__ == "__main__":
    print("=== Calculadora de área de círculos ===")
    print("Escribe 'salir', 'exit' o 'fin' para terminar.\n")

    while True:
        opcion = input("Introduce el radio del círculo: ").strip().lower()
        
        if opcion in ("salir", "exit", "fin"):
            print("👋 ¡Hasta luego!")
            break
        
        try:
            radio = float(opcion)
            area = area_circulo(radio)
            print(f"➡️  El área del círculo con radio {radio} es: {area:.2f}\n")
        except ValueError:
            print("⚠️  Por favor, introduce un número válido o 'salir', 'exit' o 'fin' para terminar.\n")
