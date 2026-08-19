try:
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    
    resultado = a / b
    print(f"El resultado de la división es: {resultado}")

except ZeroDivisionError:
    print("Error: No es posible dividir entre cero.")

except ValueError:
    print("Error: Debe ingresar únicamente números válidos.")