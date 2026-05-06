# Definir ventas con 6 productos (producto, unidades, precio, categoria)
ventas = [
    {"producto": "Laptop", "unidades": 5, "precio": 800, "categoria": "Electrónica"},
    {"producto": "Mouse", "unidades": 20, "precio": 30, "categoria": "Accesorios"},
    {"producto": "Teclado", "unidades": 15, "precio": 60, "categoria": "Accesorios"},
    {"producto": "Monitor", "unidades": 8, "precio": 300, "categoria": "Electrónica"},
    {"producto": "Silla", "unidades": 10, "precio": 150, "categoria": "Muebles"},
    {"producto": "Escritorio", "unidades": 5, "precio": 200, "categoria": "Muebles"},
]

# List comp: valor_total = unidades * precio
valores_totales = [{"producto": v["producto"], "valor_total": v["unidades"] * v["precio"]} for v in ventas]

# List comp con filtro: productos_destacados (valor > 1000)
productos_destacados = [v["producto"] for v in ventas if (v["unidades"] * v["precio"]) > 1000]

# Dict comp: producto_info  nombre: {valor, unidades}
producto_info = {
    v["producto"]: {"valor": v["unidades"] * v["precio"], "unidades": v["unidades"]}
    for v in ventas
}

# Dict comp con filtro: ranking_premium (precio > 50) desc
ranking_premium = {v["producto"]: v["unidades"] * v["precio"] for v in ventas if v["precio"] > 50}
ranking_premium_ordenado = dict(sorted(ranking_premium.items(), key=lambda x: x[1], reverse=True))

# Set comp: categorias_unicas
categorias_unicas = {v["categoria"] for v in ventas}

# Set comp con filtro: productos_baratos (precio <= 50)
productos_baratos = {v["producto"] for v in ventas if v["precio"] <= 50}

# Combinar: resumen_formateado dict comp filtrado
resumen_formateado = {
    v["producto"]: f"Valor: {v['unidades'] * v['precio']}, Unidades: {v['unidades']}, Categoría: {v['categoria']}"
    for v in ventas
}

# Calcular e imprimir gran_total
gran_total = sum(v["unidades"] * v["precio"] for v in ventas)

# Resumen
print("=== RESUMEN DE COMPREHENSIONS ===")
print("\n1. Valores totales por producto:")
for item in valores_totales:
    print(f"   {item['producto']}: {item['valor_total']}")
print("\n2. Productos destacados (valor > 1000):", productos_destacados)
print("\n3. Info por producto:")
for prod, info in producto_info.items():
    print(f"   {prod}: Valor: {info['valor']}, Unidades: {info['unidades']}")
print("\n4. Ranking premium (precio > 50, ordenado desc):")
for prod, val in ranking_premium_ordenado.items():
    print(f"   {prod}: {val}")
print("\n5. Categorías únicas:", categorias_unicas)
print("\n6. Productos baratos (precio <= 50):", productos_baratos)
print("\n7. Resumen formateado:")
for prod, res in resumen_formateado.items():
    print(f"   {prod}: {res}")
print(f"\n8. Gran total de ventas: {gran_total}")
