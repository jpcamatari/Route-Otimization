import googlemaps
import numpy as np
from itertools import permutations
import pandas as pd
from decouple import config


api_key = config('GOOGLE_KEY')
maps = googlemaps.Client(key=api_key)

origem = [
    'Rua José de Paula, 252, Jardim Bela Vista, mogi guaçu',
    'rua jose de lima, 184, jardim do lago, engenheiro coelho',
    'rua osvualte darri, 28, villa garden, campinas'
]

destino = [
    'rua jose de lima, 184, jardim do lago, engenheiro coelho',
    'rua osvualte darri, 28, villa garden, campinas'
]

def matriz_distancias(origem, destino):
    distance_matrix = maps.distance_matrix(origem, destino, mode="driving")
    num_origem = len(origem)
    num_destino = len(destino)
    matriz = np.zeros((num_origem, num_destino))
    
    for i in range(num_origem):
        row = distance_matrix['rows'][i]
                
        for j in range(num_destino):
            element = row['elements'][j]
            if element['status'] == 'OK':
                matriz[i][j] = element['distance']['value']
            else:
                matriz[i][j] = np.inf 
    return matriz


def menor_rota(matriz):
    num_locations = len(matriz)
    all_routes = permutations(range(num_locations))
    shortest_distance = np.inf
    shortest_path = []

    for route in all_routes:
        current_distance = 0
        for i in range(num_locations - 1):
            current_distance += matriz[route[i]][route[i + 1]]
        current_distance += matriz[route[-1]][route[0]]
        
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_path = route
    
    return shortest_path, shortest_distance


distance_matrix = matriz_distancias(origem, origem)
shortest_path, shortest_distance = menor_rota(distance_matrix)
fields = ["Origem", "Destino", "Distancia(Km)"]
rota = pd.DataFrame(columns=fields)


total_distance = 0
for i in range(len(shortest_path)):
    current_index = shortest_path[i]
    next_index = shortest_path[(i + 1) % len(shortest_path)]
    distance = distance_matrix[current_index][next_index] / 1000
    total_distance += distance

    temp = pd.DataFrame([[origem[current_index], origem[next_index], distance]], columns=fields)
    rota = pd.concat([rota, temp], ignore_index=True)


print(rota)


# Criar a URL do Google Maps
enderecos = list(rota["Origem"]) + [rota["Destino"].iloc[-1]]
base_url = "https://www.google.com/maps/dir/"
enderecos_url = "/".join([endereco.replace(" ", "+") for endereco in enderecos])
google_maps_url = base_url + enderecos_url

print(f"Link do Google Maps: {google_maps_url}")







