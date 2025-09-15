#lista inteligente
tareas = ["lavar ropa", "hacer ejercicio", "leer un libro"]
print("Lista inicial:")
print(tareas)

# Agregar tareas
tareas.append("preparar la cena")
tareas.append("ordenar el escritorio")
print("\nDespués de agregar dos tareas:")
print(tareas)

# Insertar en posición específica
tareas.insert(2, "pagar facturas")
print("\nDespués de insertar 'pagar facturas' en posición 2:")
print(tareas)

# Eliminar tarea por nombre
tareas.remove("leer un libro")
print("\nDespués de eliminar 'leer un libro':")
print(tareas)

# Eliminar por posición
tarea_eliminada = tareas.pop(0)
print("\nEliminamos la primera tarea:", tarea_eliminada)
print("Lista final:", tareas)
