"""Server for final task of DIGITALIZE"""
from loguru import logger
from fastapi import FastAPI, Body, Response
from phone_standartizator import get_standart_phone

app = FastAPI()

@app.get("/")
def index_page():
    """Will handle first page"""
    return "Well hello!"

@app.post("/unify_phone_from_json")
def noramlize_phone(data : dict = Body(...)):
    """Will hendle phone request page"""
    raw_phone = data['phone']
    logger.info(raw_phone)
    standart_phone = get_standart_phone(raw_phone)
    logger.info(standart_phone)
    return Response(standart_phone, media_type="text/html")
