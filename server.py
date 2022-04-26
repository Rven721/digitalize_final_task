"""Server for final task of DIGITALIZE"""
from loguru import logger
from fastapi import FastAPI, Body, Response, Form, Cookie
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
    """Will retrun normalized phone gotten form a body of request"""
    raw_phone = data['phone']
    logger.info(f"Got {raw_phone}")
    standart_phone = get_standart_phone(raw_phone)
    logger.info(f"Will return {standart_phone}")
    return Response(standart_phone, media_type="text/html")

@app.post("/unify_phone_from_form")
def noramlize_phone_from_form(phone : str = Form(...)):
    """Will return normalized phone gotten from form"""
    logger.info(f"Got {phone}")
    standart_phone = get_standart_phone(phone)
    logger.info(f"Will return {standart_phone}")
    return Response(standart_phone, media_type="text/html")

@app.get("/unify_phone_from_query")
def normalize_phone_from_query(phone: str):
    """Will return normalized phone gotten from query"""
    logger.info(f"Got {phone}")
    standart_phone = get_standart_phone(phone)
    logger.info(f"Will return {standart_phone}")
    return Response(standart_phone, media_type="text/html")

@app.get("/unify_phone_from_cookies")
def normalize_phone_from_cookies(phone: str = Cookie(...)):
    """Will return normalized phone gottern from cookies"""
    logger.info(f"Got {phone}")
    standart_phone = get_standart_phone(phone)
    logger.info(f"Will return {standart_phone}")
    return Response(standart_phone, media_type="text/html")
