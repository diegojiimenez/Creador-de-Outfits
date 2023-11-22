import random

# Base de datos de prendas (más completa)
prendas_hombre = {
    'invierno': ['chaqueta de cuero', 'abrigo', 'suéter', 'camisa', 'pantalón de lana', 'botas', 'zapatos formales'],
    'verano': ['camiseta', 'camisa de lino', 'shorts', 'pantalón corto', 'zapatillas', 'sandalias']
}

prendas_mujer = {
    'invierno': ['abrigo de lana', 'suéter de cuello alto', 'blusa', 'falda lápiz', 'botas altas', 'tacón alto'],
    'verano': ['blusa sin mangas', 'vestido floral', 'shorts de mezclilla', 'sandalias', 'zapatillas de ballet']
}

def generar_outfit(sexo, colores, temporada):
    prendas_disponibles = prendas_hombre if sexo.lower() == 'h' else prendas_mujer
    prendas_seleccionadas = prendas_disponibles[temporada.lower()]

    # Filtrar prendas por colores seleccionados
    prendas_filtradas = [prenda for prenda in prendas_seleccionadas if any(color in prenda.lower() for color in colores.split(','))]

    # Seleccionar un conjunto aleatorio de prendas para el outfit
    outfit_generado = random.sample(prendas_filtradas, min(3, len(prendas_filtradas)))

    return outfit_generado

# 1. Entrada de datos
sexo_usuario = input("¿Es para hombre o mujer? (H/M): ")
colores_usuario = input("Ingrese los colores deseados, separados por comas: ")
temporada_usuario = input("¿Invierno o verano?: ")

# 2. Generación de outfits
outfit_generado = generar_outfit(sexo_usuario, colores_usuario, temporada_usuario)

# 3. Visualización
print("¡Aquí está tu outfit generado!")
for idx, prenda in enumerate(outfit_generado, start=1):
    print(f"{idx}. {prenda}")

# 4. Feedback del usuario
gusto_usuario = input("¿Te gusta esta combinación? (Sí/No): ")

# 5. Iteración o finalización
if gusto_usuario.lower() == "no":
    print("Vamos a intentarlo de nuevo...")
    # Puedes agregar lógica adicional para ajustar la generación de outfits según las preferencias del usuario.
else:
    print("¡Genial! ¡Disfruta de tu outfit!")
