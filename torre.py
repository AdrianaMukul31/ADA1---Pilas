def mover_disco(origen, destino, nombre_origen, nombre_destino):
    disco = origen.pop()
    destino.append(disco)
    print(f"Moviendo disco {disco} de {nombre_origen} a {nombre_destino}")

def hanoi(n, origen, auxiliar, destino, nombre_origen, nombre_auxiliar, nombre_destino):
    if n == 1:
        mover_disco(origen, destino, nombre_origen, nombre_destino)
    else:
        hanoi(n-1, origen, destino, auxiliar, nombre_origen, nombre_destino, nombre_auxiliar)
        mover_disco(origen, destino, nombre_origen, nombre_destino)
        hanoi(n-1, auxiliar, origen, destino, nombre_auxiliar, nombre_origen, nombre_destino)


origen = [3, 2, 1]   
auxiliar = []        
destino = []         


print(f"Estado inicial:\nOrigen: {origen}\nAuxiliar: {auxiliar}\nDestino: {destino}\n")


hanoi(3, origen, auxiliar, destino, "Origen", "Auxiliar", "Destino")

print(f"\nEstado final:\nOrigen: {origen}\nAuxiliar: {auxiliar}\nDestino: {destino}")
