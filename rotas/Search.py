from fastapi import APIRouter, HTTPException
from database.Interface.SQL_Interface import DB

search_router = APIRouter()
db = DB(path="./database/repo.db")


@search_router.get("/search/name/")
async def search_name(nome: str):
    response = db.search_name(nome)
    if len(response) == 0:
        raise HTTPException(status_code=404, detail="Nenhum competidor foi encontrado")
    return {"resultado": db.search_name(nome)}


@search_router.get("/search/position/")
async def search_position(pos: int):
    response = db.search_position(pos)
    if len(response) == 0:
        raise HTTPException(status_code=404, detail="Posição não encontrada")
    return {"resultado": response[0]}


@search_router.get("/search/vote/")
async def search_vote(vote: int):
    if vote < 0:
        raise HTTPException(status_code=404, detail="Solicite um número positivo")
    response = db.seach_vote(vote)
    if len(response) == 0:
        raise HTTPException(status_code=404, detail="Não possui ninguém com esse número de votos")
    return {"resultado": response}


@search_router.get("/search/repositorio/")
async def search_repo(repo: str):
    response = db.search_repo(repo)
    if len(repo) == 0:
        raise HTTPException(status_code=404, detail="Não possui ninguém com esse repositorio")
    return {"resultado": response}


@search_router.get("/search/")
async def search(term:str, found: str):
    if term == "nome":
        nome = str(found)
        response = db.search_name(nome)
        if len(response) == 0:
            raise HTTPException(status_code=404, detail="Nenhum competidor foi encontrado")
        return {"resultado": db.search_name(nome)}
    elif term == "repo":
        repo = str(found)
        response = db.search_repo(repo)
        if len(repo) == 0:
            raise HTTPException(status_code=404, detail="Não possui ninguém com esse repositorio")
        return {"resultado": response}
    elif found.isdigit():
        if term == "vote":
            vote = int(found)
            if vote < 0:
                raise HTTPException(status_code=404, detail="Solicite um número positivo")
            response = db.seach_vote(vote)
            if len(response) == 0:
                raise HTTPException(status_code=404, detail="Não possui ninguém com esse número de votos")
            return {"resultado": response}
        elif term == "pos":
            pos = int(found)
            response = db.search_position(pos)
            if len(response) == 0:
                raise HTTPException(status_code=404, detail="Posição não encontrada")
            return {"resultado": response[0]}
        else:
            raise HTTPException(status_code=400, detail=f"Termo não encontrado {term}")
    else:
        raise HTTPException(status_code=400, detail=f"Tipagem errada {type(found)}")
