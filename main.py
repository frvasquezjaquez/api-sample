from fastapi import FastAPI, status, HTTPException
from azure.cosmos import exceptions, CosmosClient, PartitionKey
from ast import literal_eval
import logging
import json


import redis


app = FastAPI()



@app.get("/")
async def root():
        return {"message": "Hello World"}

@app.get("/ping")
async def health():
        return {"message": "pong"}