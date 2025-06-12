from typing import Union
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from elasticsearch import Elasticsearch
import time, dotenv, os
from datetime import datetime

dotenv.load_dotenv()

# Suppression des messages de warning à propos du certificat...
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", os.environ['ELASTIC_PASSWORD']),
    verify_certs=False
)
print(es.info())

app = FastAPI()

SECRET=os.environ['SECRET']

@app.middleware("http")
async def check_token(request: Request, call_next):
    print(f"check {request.query_params=}")
    if request.query_params.get('token') == SECRET:
        response = await call_next(request)
        return response
    else :
        return JSONResponse(
            status_code=418,
            content={"message": f"Oops!  did something. There goes a rainbow..."},
        )
        #raise HTTPException(status_code=400, detail="Item not found")



@app.middleware("http")
async def add_process_time_header2(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time2"] = str(process_time)

    log_entry = {
        "timestamp": datetime.now(),
        "method": request.method,
        "path": request.url.path,
        "query_params": dict(request.query_params),
        "process_time": process_time,
        "status_code": response.status_code
    }
    es.index(index="fastapi-logs", document=log_entry) # envoi le log -> Elastic

    return response


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
