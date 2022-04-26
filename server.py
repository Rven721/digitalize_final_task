"""Server for final task of DIGITALIZE"""
from loguru import logger
from fastapi import FastAPI, Body, Response, Form, Request
from phone_standartizator import get_standart_phone

logger.remove()
logger.add("hystory.log")

app = FastAPI()

@app.get("/")
def index_page():
    """Will handle first page"""
    return Response("Well helllo!", media_type="text/html")

@app.post("/unify_phone_from_json")
def noramlize_phone_from_json(data : dict = Body(...)):
    """Will hendle phone request page"""
    raw_phone = data['phone']
    logger.info(raw_phone)
    standart_phone = get_standart_phone(raw_phone)
    logger.info(standart_phone)
    return Response(standart_phone, media_type="text/html")

@app.post("/unify_phone_from_form")
def noramlize_phone_from_form(phone : str = Form(...)):
    """Will hendle phone request page"""
    logger.info(phone)
    standart_phone = get_standart_phone(phone)
    logger.info(standart_phone)
    return Response(standart_phone, media_type="text/html")

@app.get("/unify_phone_from_query")
def normalize_phone_from_query(phone: str):
    """Will return normalized fone goten from query"""
    standart_phone = get_standart_phone(phone)
    logger.info(standart_phone)
    return Response(standart_phone, media_type="text/html")
