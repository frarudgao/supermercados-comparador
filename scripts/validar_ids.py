import json
import requests

# Cargar productos desde el JSON
with open("mercadona_ids.json", "r", encoding="utf-8") as f:
    productos = json.load(f)

# Validar cada producto
print("🔍 Comprobando IDs de Mercadona...\n")

for producto in productos:
    nombre = producto["nombre"]
    id_ = producto["id"]
    url = f"https://tienda.mercadona.es/api/products/{id_}"

    try:
        res = requests.get(url)
        if res.status_code != 200:
            print(f"❌ {nombre} (ID: {id_}) → No responde (HTTP {res.status_code})")
            continue

        data = res.json()
        price = data.get("price_instructions", {}).get("price")

        if price is None:
            print(f"⚠️ {nombre} (ID: {id_}) → Producto encontrado, pero sin precio")
        else:
            print(f"✅ {nombre} (ID: {id_}) → Precio actual: {price:.2f} €")

    except Exception as e:
        print(f"❌ Error al procesar {nombre} (ID: {id_}): {e}")

print("\n✅ Validación completada.")
