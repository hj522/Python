from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates 
from fastapi.staticfiles import StaticFiles 
from starlette.responses import JSONResponse
from mem_dao import MemDao
from pydantic.main import BaseModel

class Mem(BaseModel):
    m_seq: int = 0
    m_name: str = None
    m_tel: str = None
    army_yn: str = None
    
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates") 

@app.get("/mem", response_class=HTMLResponse)
async def mem_list(request: Request):
    return templates.TemplateResponse("mem.html", {"request": request}) 

@app.get("/mem_selects")
async def mem_selects():
    md = MemDao()
    mems = md.selects()
    return JSONResponse(mems)

@app.post("/mem_select")
async def mem_select(mem:Mem):
    md = MemDao()
    mem = md.select(mem.m_seq)
    return JSONResponse(mem)

@app.post("/mem_insert")
async def mem_insert(mem:Mem):
    md = MemDao()
    cnt = md.insert(mem.m_name, mem.m_tel, mem.army_yn)
    return JSONResponse(cnt)

@app.post("/mem_update")
async def mem_update(mem:Mem):
    md = MemDao()
    cnt = md.update(mem.m_seq, mem.m_name, mem.m_tel, mem.army_yn)
    return JSONResponse(cnt)

@app.post("/mem_delete")
async def mem_delete(mem:Mem):
    md = MemDao()
    cnt = md.delete(mem.m_seq)
    return JSONResponse(cnt)

# uvicorn myajax:app --reload