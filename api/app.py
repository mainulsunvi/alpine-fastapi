import json
from fastapi import FastAPI, Request	
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="frontend")

@app.get('/', response_class=HTMLResponse)
def index(request: Request):
	context = {"request": request, "msg": "Hello World from App"}
	return templates.TemplateResponse("index.html", context)

@app.get('/hello/', response_class=HTMLResponse)
def hello(request: Request):
    user_details = [
        {
            "name": "Florence Ricardo",
            "email": "fricardo0@ocn.ne.jp",
            "address": "31186 Dorton Way",
        },
        {
            "name": "Torrin Buddington",
            "email": "tbuddington1@ameblo.jp",
            "address": "18 Sunfield Circle",
        },
        {
            "name": "Javier O Molan",
            "email": "jo2@cdc.gov",
            "address": "0441 Roxbury Way",
        },
        {
            "name": "Farlie Cumbers",
            "email": "fcumbers3@shutterfly.com",
            "address": "348 Larry Lane",
        },
        {
            "name": "Gabriell De Bruyne",
            "email": "gde4@berkeley.edu",
            "address": "116 Logan Drive",
        },
        {
            "name": "Clari Stanier",
            "email": "cstanier5@paginegialle.it",
            "address": "010 Reindahl Hill",
        },
        {
            "name": "Uta Marven",
            "email": "umarven6@github.com",
            "address": "397 Daystar Avenue",
        },
        {
            "name": "Kit Martinyuk",
            "email": "kmartinyuk7@tamu.edu",
            "address": "539 Bunker Hill Street",
        },
        {
            "name": "Guillemette Rocks",
            "email": "grocks8@pinterest.com",
            "address": "10812 Almo Junction",
        },
        {
            "name": "Thibaud Tiuit",
            "email": "ttiuit9@nytimes.com",
            "address": "143 Fallview Center",
        },
    ]

    context = {"request": request, 'user_details': user_details, "msg": "Hello World from App"}
    return templates.TemplateResponse("hello.html", context)
