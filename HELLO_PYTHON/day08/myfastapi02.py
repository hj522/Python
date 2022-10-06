from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic.main import BaseModel
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates") 


@app.get("/hello", response_class=HTMLResponse)
async def hello(request: Request):
    str = "패스트API겁나짜증나"
    arr = ["홍길동","전우치","이순신"]
    emps = [
        {'e_id':'1','e_name':'1','e_sex':'1','e_addr':'1'},
        {'e_id':'2','e_name':'2','e_sex':'2','e_addr':'2'},
        {'e_id':'3','e_name':'3','e_sex':'3','e_addr':'3'}
    ]
    return templates.TemplateResponse("index.html", {"request": request, "str":str, "arr":arr, "emps":emps}) 


# uvicorn myfastapi01:app --reload