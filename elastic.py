from elasticsearch import Elasticsearch
from datetime import datetime
import requests, dotenv, os, json, time

dotenv.load_dotenv()

# Suppression des messages de warning à propos du certificat...
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", os.environ['ELASTIC_PASSWORD']),
    verify_certs=False
)
print(client.info())

index = "p4-ego-test"

doc = {
    'author': 'author_name',
    'text': 'Interesting content...',
    'timestamp': datetime.now(),
}
#resp = client.index(index=index, id=1, document=doc)
#print(resp)

resp = client.get(index=index, id=1)
print(resp)

resp = client.search(index=index, query={"match_all": {}})
print(resp)