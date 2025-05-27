import json
from datetime import datetime
import random

productos_comunes = [
    "Leche entera 1L",
    "Huevos talla L docena",
    "Arroz redondo 1kg",
    "Aceite de oliva virgen extra 1L",
    "Pasta espaguetis 500g"
]

datos_actualizados = []

for producto in productos_comunes:
    datos_actualizados.append({
        "producto": producto,
        "mercadona": round(random.uniform(0.8, 2.5), 2),
        "carrefour": round(random.uniform(0.8, 2.5), 2),
        "fecha": datetime.now().strftime("%Y-%m-%d")
    })

with open("precios_diarios.json", "w", encoding="utf-8") as f:
    json.dump(datos_actualizados, f, indent=2, ensure_ascii=False)
