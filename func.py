import json
import conf
import requests

def adquerir_ticket ():
    data = {"password": conf.PSW, "username": conf.USR} #credenciales de la api
    cab = {"content-type": "application/json"} #cabecera
    ticket = requests.post(conf.URL+ "ticket", json.dumps(data), headers=cab).json()['response']['serviceTicket'] # adquerir solo el ticket
    return ticket

#Funcion para eliminar ticket
def eliminar_ticket(ticket):
    data = {"Ticket": ticket}
    cab = {"content-type": "application/json", "X-Auth-Token": ticket}
    requests.delete(conf.URL + "ticket/"+ticket, data=json.dumps(data), headers=cab) #eliminar ticket

#host conectados en la red
def host_registrados(): #obtiene solo la cantidad de host para determinar el numero maximo 
    ticket = adquerir_ticket()
    cabecera_inventario = {"content-type": "application/json", "X-Auth-Token": ticket}
    host = requests.get(conf.URL + "host/count?hostName=&hostMac=&hostType=&connectedInterfaceName=&hostIp=&connectedNetworkDeviceIpAddress=&subType=&filterOperation=", headers=cabecera_inventario).json()['response']#adquirir solo el numero de host
    eliminar_ticket(ticket)
    return host
def listar_host():
    total_host=host_registrados()
    lista=[]
    ticket = adquerir_ticket()
    cabecera_inventario = {"content-type": "application/json", "X-Auth-Token": ticket}
    host = requests.get(conf.URL + "host", headers=cabecera_inventario)#Adquirir los host para comparar
    eliminar_ticket(ticket)
    return host
def obtener_ips():#Adquirir las ip para comprar
    lista = []
    i = 0
    while i < host_registrados():
        lista.append(listar_host().json()['response'][i]['hostIp'])
        i = i + 1
    return lista

lista_inicio = listar_host() #lista para cargar los host en primera instancia
cant = host_registrados()
