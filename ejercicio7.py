persona = {
    "nombre": "Miguel",
    "edad": 22,
    "carrera": "Ing Sistemas",
    "ciudad": "Barranquilla"
}

print("--- Claves ---")
for clave in persona.keys():
    print(clave)

print("\n--- Valores ---")
for valor in persona.values():
    print(valor)

print("\n--- Pares Clave-Valor ---")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")