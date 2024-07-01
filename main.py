import googlemaps
import numpy as np
from itertools import permutations
from decouple import config

api_key = config('GOOGLE_KEY')
maps = googlemaps.Client(key=api_key)

origem = [
    'Av. Brigadeiro Luis Antonio 2503 11B, São Paulo - SP, 01401-000',
    'Rodovia Anhanguera, Km 125 s/n - Vila Bertini, Americana - SP',
    'Av. Dr. Heitor Penteado, s/n - Parque Taquaral, Campinas - SP, 13075-460',
    'Av. Pedro Álvares Cabral - Vila Mariana, São Paulo - SP, 04094-05',
    'Av. Brig. Faria Lima, 3600 - 10º - Itaim Bibi, São Paulo - SP, 04538-132',
    'R. Eduardo Tozi, s/n - Vila Doze de Setembro I, Jaguariúna - SP, 13912-572',
    'Alameda Campinas, 1160 - Jardim Paulista, São Paulo - SP, 01404-200'
]

destino = [
    'Rodovia Anhanguera, Km 125 s/n - Vila Bertini, Americana - SP',
    'Av. Dr. Heitor Penteado, s/n - Parque Taquaral, Campinas - SP, 13075-460',
    'Av. Pedro Álvares Cabral - Vila Mariana, São Paulo - SP, 04094-05',
    'Av. Brig. Faria Lima, 3600 - 10º - Itaim Bibi, São Paulo - SP, 04538-132',
    'R. Eduardo Tozi, s/n - Vila Doze de Setembro I, Jaguariúna - SP, 13912-572',
    'Alameda Campinas, 1160 - Jardim Paulista, São Paulo - SP, 01404-200'
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


