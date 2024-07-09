import googlemaps
import numpy as np
from itertools import permutations
from decouple import config

# Configuração da API do Google Maps
api_key = config('GOOGLE_KEY')
maps = googlemaps.Client(key=api_key)


#Função para criação da matriz com os endereços fornecidos
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

#Função para analisar menor rota da matriz de endereços fornecido
def menor_rota(matriz):
    num_locations = len(matriz)
    all_routes = permutations(range(num_locations))
    shortest_distance = np.inf
    shortest_path = []

    for route in all_routes:
        current_distance = 0
        for i in range(num_locations - 1):
            current_distance += matriz[route[i]][route[i + 1]]

        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_path = route

    return shortest_path, shortest_distance
