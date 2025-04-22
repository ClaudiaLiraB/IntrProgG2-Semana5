distancia_recorrida_km = float(input("Ingrese la distancia recorrida en kilómetros: "))
litros_consumidos = float(input("Ingrese la cantidad de litros consumidos: "))
precio_por_litro = 48.30
rendimiento_km_por_litro = distancia_recorrida_km / litros_consumidos
gasto_total_combustible = litros_consumidos * precio_por_litro

print("\nDistancia recorrida:", distancia_recorrida_km, "km")
print("Litros consumidos:", litros_consumidos, "litros")
print("Precio por litro:", precio_por_litro)

print("Rendimiento del vehículo:", rendimiento_km_por_litro, "km/l")

print("Gasto total en combustible:", gasto_total_combustible)