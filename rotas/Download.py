from fastapi import APIRouter
from fastapi.responses import FileResponse

download_route = APIRouter()


@download_route.get("/download/db")
async def download_db():
    return FileResponse("./database/repo.db")


@download_route.get("/download/list")
async def donwload_list():
    return FileResponse("./database/repositorios.txt")