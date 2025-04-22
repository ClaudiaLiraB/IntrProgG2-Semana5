capital_inicial = float(input("Ingrese el capital inicial: "))
tasa_interes_anual_porcentaje = float(input("Ingrese la tasa de interés anual (en porcentaje): "))
cantidad_anios = int(input("Ingrese la cantidad de años: "))
tasa_interes_anual_decimal = tasa_interes_anual_porcentaje / 100
factor_crecimiento = (1 + tasa_interes_anual_decimal) ** cantidad_anios
monto_final = capital_inicial * factor_crecimiento
interes_ganado = monto_final - capital_inicial

print("\nCapital inicial:", capital_inicial)
print("Tasa de interés anual:", tasa_interes_anual_porcentaje, "%")
print("Cantidad de años:", cantidad_anios)

print("Monto final:", monto_final)
print("Interés ganado:", interes_ganado)