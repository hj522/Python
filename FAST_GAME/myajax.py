from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles 
    
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates") 

@app.get("/", response_class=HTMLResponse)
async def game(request: Request):
    return templates.TemplateResponse("game.html", {"request": request}) 

@app.get("/game2", response_class=HTMLResponse)
async def game2(request: Request):
    return templates.TemplateResponse("game2.html", {"request": request}) 

# uvicorn myajax:app --reload