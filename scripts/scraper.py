import json
import requests
from datetime import datetime
import random

# Lista de productos comunes (tal como los tienes en productos.json)
productos_comunes = [
    "Leche entera 1L",
    "Huevos talla L docena",
    "Arroz redondo 1kg",
    "Aceite de oliva virgen extra 1L",
    "Pasta espaguetis 500g"
]

# Función para buscar un producto por nombre aproximado en Mercadona
def buscar_precio_mercadona(nombre_producto):
    url_busqueda = f"https://tienda.mercadona.es/api/search/?query={nombre_producto}"
    try:
        res = requests.get(url_busqueda)
        datos = res.json()
        productos = datos.get("results", [])
        if productos:
            return float(productos[0]["price_instructions"]["price"])
        else:
            return None
    except:
        return None

# Crear el listado final
datos_actualizados = []

for producto in productos_comunes:
    precio_mercadona = buscar_precio_mercadona(producto)
    precio_carrefour = round(random.uniform(0.8, 2.5), 2)  # provisional

    datos_actualizados.append({
        "producto": producto,
        "mercadona": precio_mercadona if precio_mercadona else 0.00,
        "carrefour": precio_carrefour,
        "fecha": datetime.now().strftime("%Y-%m-%d")
    })

# Guardar en JSON
with open("precios_diarios.json", "w", encoding="utf-8") as f:
    json.dump(datos_actualizados, f, indent=2, ensure_ascii=False)


