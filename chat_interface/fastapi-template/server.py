from fastapi import FastAPI, Request, Form, File, UploadFile, HTTPException
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional
from fastapi.responses import HTMLResponse
import requests
import os
from collections import defaultdict

import random
import json



app = FastAPI()
templates = Jinja2Templates(directory = 'templates')


@app.get("/")
def home(request: Request):
    ''' Returns html jinja2 template render for home page form
    '''

    return templates.TemplateResponse('home.html', {
            "request": request,
        })

class Item(BaseModel):
    search: str

class ItemUpdate(BaseModel):
    ids: List[int]
    lastId: Optional[int] = None

norm_score_breakdown = []

@app.post("/")
async def root(item: Item):
    global norm_score_breakdown

    url = eval(item.search)
    print(url)

 