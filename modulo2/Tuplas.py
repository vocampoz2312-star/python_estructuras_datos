# Definir catalogo como tupla de subtuplas
catalogo = (("Blidspot", "Rx", 2001, 10),
               ("La casa de papel", "NN", 2020, 10),
               ("Amor", "Gaia", 2015, 7),
               ("Ranita", "Hernandez", 1988, 8))
# Recorrer catalogo con for desempaquetando los cuatro campos
for nombre, director, año, puntuacion in catalogo:
    print(f"Nombre: {nombre} \n Director: {director} \n Año: {año} \n Puntuación: {puntuacion}\n")



# Usar operador * para separar primera pelicula del resto

primeraPelicula, *restoCatalogo = catalogo
print("Primera película:", primeraPelicula)
print("Resto del catálogo:", restoCatalogo)

# Definir buscar_por_director(director)
def buscar_por_director(director):
    peliculas = []
    for pelicula in catalogo:
        if pelicula[1]==director:
            peliculas.append(pelicula)
       
    if peliculas:
        print(f"peliculas hechas por {director}: {peliculas}")
    else:
        print("No se encontraron peliculas por ese director")

# Definir obtener_estadisticas(peliculas)
#Implementa obtener_estadisticas() retornando (min, max, promedio)
def obtener_estadisticas(peliculas):
    puntuaciones = []
    for puntuacion in peliculas:
        puntuaciones.append(puntuacion[3])
    minPuntuacion = min(puntuaciones)
    maxPuntuacion = max(puntuaciones)
    promedioPuntuacion = sum(puntuaciones) / len(puntuaciones)

    return minPuntuacion, maxPuntuacion, promedioPuntuacion



# Llamar a buscar_por_director e imprimir coincidencias
buscar_por_director("Rx")

# Desempaquetar retorno de obtener_estadisticas
minimo, maximo, promedio = obtener_estadisticas(catalogo)

# Imprimir minima, maxima y promedio
print(f"Minima: {minimo}\nMaxima: {maximo}\nPromedio: {promedio}")