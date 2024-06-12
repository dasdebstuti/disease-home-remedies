from fastapi import FastAPI
import logging

from service import fetch_disease_details

app = FastAPI()


from pydantic import BaseModel


class Query(BaseModel):
    disease_name: str
    disease_type: str


@app.get("/query")
async def get_disease_info(query: Query):
    print(f'Fetching disease info for {query}')
    logging.info(f'Fetching disease info for {query}')
    disease_type = query.disease_type
    disease_name = query.disease_name
    return fetch_disease_details(disease_name, disease_type)