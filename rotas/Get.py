from fastapi import APIRouter
from database.Interface.SQL_Interface import DB

all_router = APIRouter()
db = DB(path="./database/repo.db")


@all_router.get("/all")
async def get_all():
    return db.get_all()


@all_router.get("/name")
async def get_list_name():
    names = db.get_name()
    exit = []
    for x in names:
        exit.append(x[0])
    return exit
