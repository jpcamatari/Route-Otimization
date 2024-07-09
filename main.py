import logging
from fastapi import FastAPI, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
from controller import matriz_distancias, menor_rota
import pandas as pd


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/rota")
async def calculate_route(request: Request, origem: str = Query(...), destino: List[str] = Query(...)):
    origem_list = [origem]
    destino_list = destino
    locations = origem_list + destino_list
    distance_matrix = matriz_distancias(locations, locations)

    # Encontrando a rota mais curta e a menor distância total
    shortest_path, shortest_distance = menor_rota(distance_matrix)
    fields = ["Origem", "Destino", "Distancia (Km)"]
    rota = pd.DataFrame(columns=fields)
    total_distance = 0

    for i in range(len(shortest_path) - 1):
        current_index = shortest_path[i]
        next_index = shortest_path[i + 1]
        distance = round(distance_matrix[current_index][next_index] / 1000.0,1)
        total_distance += distance

        temp = pd.DataFrame([[locations[current_index], locations[next_index], distance]], columns=fields)
        rota = pd.concat([rota, temp], ignore_index=True)

    # Criar a URL do Google Maps
    enderecos = list(rota["Origem"]) + [rota["Destino"].iloc[-1]]
    base_url = "https://www.google.com/maps/dir/"
    enderecos_url = "/".join([endereco.replace(" ", "+") for endereco in enderecos])
    google_maps_url = base_url + enderecos_url

    tables = rota.to_dict(orient="records")

    # Renderizando o template result.html com os dados calculados
    return templates.TemplateResponse("result.html", {
        "request": request,
        "tables": tables,
        "total_distance": round(total_distance,1),
        "link": google_maps_url
    })