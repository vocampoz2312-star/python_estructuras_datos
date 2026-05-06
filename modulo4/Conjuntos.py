# Definir tienda_centro, tienda_norte y tienda_sur
tienda_centro = {"blusa", "jean", "shorts", "camisa"}
tienda_norte = {"vestido", "croptop", "falda", "pantalon"}
tienda_sur = {"shorts", "bermuda", "faldashort", "blusita"}

# Calcular catalogo_completo con union()
catalogo_completo = tienda_centro.union(tienda_norte).union(tienda_sur)

# Calcular productos_comunes con intersection()
productos_comunes = tienda_centro.intersection(tienda_norte, tienda_sur)

# Exclusivos de cada tienda con difference(union())
exclusivos_centro = tienda_centro.difference(tienda_norte, tienda_sur)
exclusivos_norte = tienda_norte.difference(tienda_centro, tienda_sur)
exclusivos_sur = tienda_sur.difference(tienda_centro, tienda_norte)

# Verificar pares con isdisjoint()
disjoint_centro_norte = tienda_centro.isdisjoint(tienda_norte)
disjoint_centro_sur = tienda_centro.isdisjoint(tienda_sur)
disjoint_norte_sur = tienda_norte.isdisjoint(tienda_sur)

# Definir usuario1, usuario2, usuario3
usuario1 = {"accion", "comedia", "drama"}
usuario2 = {"drama", "terror", "accion"}
usuario3 = {"comedia", "romance"}

# Calcular con & | - ^ <= y mostrar resumen
comunes = usuario1 & usuario2
universo = usuario1 | usuario2 | usuario3
exclusivos = usuario1 - usuario2
diferencia_simetrica = usuario1 ^ usuario2
subconjunto = usuario1 <= universo

# Resumen
print("=== RESUMEN DE CONJUNTOS =====")
print("\n1. Tiendas:")
print("   Catálogo completo:", catalogo_completo)
print("   Productos comunes entre todas las tiendas:", productos_comunes)
print("   Exclusivos centro:", exclusivos_centro)
print("   Exclusivos norte:", exclusivos_norte)
print("   Exclusivos sur:", exclusivos_sur)
print("   ¿Tienda centro y norte son disjuntos?:", disjoint_centro_norte)
print("   ¿Tienda centro y sur son disjuntos?:", disjoint_centro_sur)
print("   ¿Tienda norte y sur son disjuntos?:", disjoint_norte_sur)

print("\n2. Usuarios:")
print("   Géneros comunes usuario1 y usuario2:", comunes)
print("   Todos los géneros (universo):", universo)
print("   Géneros exclusivos usuario1:", exclusivos)
print("   Diferencia simétrica usuario1 y usuario2:", diferencia_simetrica)
print("   ¿usuario1 es subconjunto del universo?:", subconjunto)