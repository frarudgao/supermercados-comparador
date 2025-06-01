import json
import requests
from datetime import datetime
import random

# Cargar productos con IDs exactos de Mercadona
with open("mercadona_ids.json", "r", encoding="utf-8") as f:
    productos = json.load(f)

# Función para obtener el precio real desde Mercadona por ID
def obtener_precio_por_id(id_producto, nombre_producto):
    url = f"https://tienda.mercadona.es/api/products/{id_producto}"
    try:
        res = requests.get(url)
        data = res.json()

        if "price_instructions" in data and "price" in data["price_instructions"]:
            return float(data["price_instructions"]["price"])
        else:
            print(f"⚠️ Producto sin campo 'price_instructions': {nombre_producto}")
            return None

    except Exception as e:
        print(f"❌ Error al obtener precio del producto '{nombre_producto}' (ID: {id_producto}): {e}")
        return None

# Crear listado actualizado
datos_actualizados = []

for item in productos:
    nombre = item["nombre"]
    id_mercadona = item["id"]
    precio_mercadona = obtener_precio_por_id(id_mercadona, nombre)

    if precio_mercadona is None:
        print(f"⚠️ Producto no encontrado o sin precio: {nombre}")

    precio_carrefour = round(random.uniform(0.8, 2.5), 2)  # temporal

    datos_actualizados.append({
        "producto": nombre,
        "mercadona": round(precio_mercadona, 2) if precio_mercadona is not None else 0.00,
        "carrefour": precio_carrefour,
        "fecha": datetime.now().strftime("%Y-%m-%d")
    })

# Guardar resultado
with open("precios_diarios.json", "w", encoding="utf-8") as f:
    json.dump(datos_actualizados, f, indent=2, ensure_ascii=False)




