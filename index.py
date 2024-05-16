from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from rotas.Get import all_router
from rotas.Search import search_router
from rotas.Download import download_route
import uvicorn

app = FastAPI(title="Banco de Dados", description="Banco de dados alura", version="0.1.0")

app.mount("/static", StaticFiles(directory="./static"), name="static")
app.include_router(all_router)
app.include_router(search_router)
app.include_router(download_route)

template = Jinja2Templates(directory="./view")


@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return template.TemplateResponse("view.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("index:app", host="0.0.0.0", port=8000)

