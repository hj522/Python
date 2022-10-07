from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic.main import BaseModel
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles 
from day09.emp_dao import EmpDao

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates") 

@app.get("/emp_list", response_class=HTMLResponse)
async def emp_list(request: Request):
    ed = EmpDao()
    emps = ed.selects()
    return templates.TemplateResponse("emp_list.html", {"request": request, "emps": emps}) 


# uvicorn myemp:app --reload