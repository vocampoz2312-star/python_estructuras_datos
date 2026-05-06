# Definir ventas_por_region
ventasPorRegion = {
    "Bello": {"Q1": 100, "Q2": 1000, "Q3": 2000, "Q4": 3000},
    "Paris": {"Q1": 800, "Q2": 1200, "Q3": 1600, "Q4": 2000},
    "Medellin": {"Q1": 900, "Q2": 1400, "Q3": 1800, "Q4": 2200},
    "Itagui": {"Q1": 1100, "Q2": 1300, "Q3": 1700, "Q4": 2100}
}

# Calcular ventas totales con items() y sum(values())
totalPorRegion ={}
for region, ventas in ventasPorRegion.items():
    totalPorRegion[region] = sum(ventas.values())
print("Totales por región:", totalPorRegion)

# Encontrar region con max() key=lambda
mejorRegion = max(totalPorRegion, key=lambda r: totalPorRegion[r])
print(f"Región con mayores ventas: {mejorRegion} (Total: {totalPorRegion[mejorRegion]})")

# Inicializar totales_por_trimestre
totales_por_trimestre = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0}
print("Totales iniciales por trimestre:", totales_por_trimestre)

# Acumular con iteracion anidada
for ventas in ventasPorRegion.values():
    for trimestre, monto in ventas.items():
        totales_por_trimestre[trimestre] += monto
print("Totales acumulados por trimestre:", totales_por_trimestre)

# Calcular gran_total
gran_total = sum(totales_por_trimestre.values())
print(f"Gran total de ventas: {gran_total}")
# Generar porcentajes con dict comprehension
porcentajes = {
    region: (total / gran_total) * 100
    for region, total in totalPorRegion.items()
}
print("Porcentaje de participación por región:", porcentajes)
# Imprimir reporte ordenado
print("\nReporte de ventas por región (ordenado alfabéticamente):")
reporte = sorted(totalPorRegion.items())

for region, total in reporte:
    print(region, total)