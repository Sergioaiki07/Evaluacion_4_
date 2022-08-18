import func
import time
from colorama import Fore
#Interfaz usuario

print("Host conectados: ", func.obtener_ips()) #obtiene los host conectados como primera accion
inicial_ips=func.obtener_ips() #obtiene las ip de los host 
while True: #ciclo infinito
    cantidad_host = func.host_registrados() #obtiene datos de host
    lista_actual_ip = func.obtener_ips() #obtienelos host en el tiempo actual
    lista_actual = func.listar_host()
    diferencias = set(lista_actual_ip) - set(inicial_ips) #Compara los vectores, si existe una diferencia mostrara que host se adiciono
    if diferencias:
        print(Fore.RED+"Se detectarón los siguientes host conectados!!", diferencias) #imprime los host adicionados

    time.sleep(5) #Analisis cada 5 segundos 


