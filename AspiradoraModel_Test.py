import time
from AspiradoraModel import AspiradoraModel
from CeldaSuciaAgent import CeldaSuciaAgent

agents = int(input("Ingrese el número de agentes: "))
sucias = int(input("Ingrese el porcentaje de celdas sucias: "))
M = int(input("Ingrese el número de filas: "))
N = int(input("Ingrese el número de columnas: "))
num_celdas = M * N
t = int(input("Ingrese el tiempo máximo: "))

celdas_sucias = int((sucias * num_celdas)/100)

now = time.time()
future = now + t
model = AspiradoraModel(agents, sucias, M, N)
pasos = 0
tiempo = 0

while time.time() < future:
    model.step()
    pasos += 1
    sucias_count = 0

    for i in model.schedule.agents:
        if isinstance(i, CeldaSuciaAgent):
            if i.is_dirty:
                sucias_count += 1

    if sucias_count == 0:
        tiempo = time.time()
        break

limpias = 100 - ((sucias_count * 100)/num_celdas)

if tiempo == 0:
    print(f"Tiempo máximo excedido")
    print(f"Porcentaje de celdas limpias: {int(limpias)}%")
    print(f"Pasos realizados por cada agente: {pasos}")
    print(f"Movimientos totales: {pasos * agents}")

else:
    print(f"Tiempo total: {tiempo - now} segundos")
    print(f"Porcentaje de celdas limpias: 100%")
    print(f"Pasos realizados por cada agente: {pasos}")
    print(f"Movimientos totales: {pasos * agents}")
