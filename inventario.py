import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la simulación
initial_inventory = 100  # Inventario inicial
reorder_point = 20  # Punto de reorden
order_quantity = 80  # Cantidad a ordenar cuando se reordena
lead_time = 3  # Tiempo de entrega (días) de una orden
daily_demand_mean = 5  # Demanda diaria promedio
daily_demand_std = 2  # Desviación estándar de la demanda diaria
simulation_days = 100  # Días a simular

# Variables para la simulación
inventory = initial_inventory
days_out_of_stock = 0
orders_pending = 0
orders_arrival_day = -1  # No hay orden activa al inicio
inventory_levels = []  # Registro del nivel de inventario por día

# Simulación día a día
for day in range(simulation_days):
    # Registrar nivel actual de inventario
    inventory_levels.append(inventory)

    # Generar la demanda del día (puede ser negativa, lo que implica que no hubo demanda)
    demand = max(0, np.random.normal(daily_demand_mean, daily_demand_std))
    
    # Satisfacer la demanda con el inventario disponible
    if inventory >= demand:
        inventory -= demand
    else:
        # Inventario insuficiente, el cliente no es atendido en su totalidad
        inventory = 0
        days_out_of_stock += 1

    # Verificar si llega una orden de reabastecimiento
    if day == orders_arrival_day:
        inventory += order_quantity
        orders_pending = 0

    # Colocar una orden si el inventario está por debajo del punto de reorden y no hay una orden pendiente
    if inventory < reorder_point and orders_pending == 0:
        orders_pending = 1
        orders_arrival_day = day + lead_time

# Resultados
print(f"Días sin inventario: {days_out_of_stock}")
print(f"Nivel final de inventario: {inventory}")

# Graficar el nivel de inventario a lo largo de los días
plt.figure(figsize=(10, 6))
plt.plot(range(simulation_days), inventory_levels, label='Nivel de inventario', color='green')
plt.axhline(reorder_point, color='red', linestyle='--', label='Punto de reorden')
plt.title('Simulación del Nivel de Inventario a lo Largo del Tiempo')
plt.xlabel('Día')
plt.ylabel('Inventario')
plt.legend()
plt.grid(True)
plt.show()
