from fastapi import FastAPI

from service import fetch_disease_details

app = FastAPI()


from pydantic import BaseModel


class Query(BaseModel):
    disease_name: str
    disease_type: str


@app.get("/query")
async def root(query: Query):
    disease_type = query.disease_type
    disease_name = query.disease_name
    return fetch_disease_details(disease_name, disease_type)