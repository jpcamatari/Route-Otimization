from typing import List
from fastapi import FastAPI, Query, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import logging

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
    logger.info(f"Origem recebida: {origem}")
    logger.info(f"Destinos recebidos: {destino}")
    return {"origem": origem, "destino": destino}
