import func
import time
from colorama import Fore
#Interfaz usuario

print("Host conectados: ", func.obtener_ips())
inicial_ips=func.obtener_ips()
while True: #ciclo infinito
    cantidad_host = func.host_registrados()
    lista_actual_ip = func.obtener_ips()
    lista_actual = func.listar_host()
    prueba = set(lista_actual_ip)

    diferencias = set(lista_actual_ip) - set(inicial_ips)
    if diferencias:
        print(Fore.RED+"Se detectarón los siguientes host conectados!!", diferencias)
        lista_diff = list(diferencias)
        print(lista_diff)
        print(lista_diff[0])
        print(lista_diff[1])
        print(lista_diff[3])
    time.sleep(5)


