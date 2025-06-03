import requests, dotenv, os, json, time
from elasticsearch import Elasticsearch

dotenv.load_dotenv()

# Suppression des messages de warning à propos du certificat...
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

EMAIL=os.environ['SIMPLON_EMAIL']
PASSWORD=os.environ['SIMPLON_PASSWORD']
URL="https://api.simplonline.co"

client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", os.environ['ELASTIC_PASSWORD']),
    verify_certs=False
)
response = client.info()
print(response)

headers = {
    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/json;charset=UTF-8',
    'origin': 'https://simplonline.co',
    'referer': 'https://simplonline.co/',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36',
}

data={
    "email": EMAIL,
    "password": PASSWORD
}

resp = requests.post(URL+'/login', headers=headers, data=json.dumps(data))

if resp.status_code!=200:
    print('Erreur authentification')
    quit()

# Récup du token & ajout dans les headers
TOKEN=resp.json()['token']
#print(TOKEN)
headers['Authorization']=f"Bearer {TOKEN}"

params={'pagination':'true', 'page':5, 'perPage':100}

# Requète les données & les affiche ('hydra:member')
def get_list(path, index, page=1):
    params['page']=page
    print(f"-------------- {path} -> {index}, page {page} --------------")
    resp = requests.get(URL+path, headers=headers, params=params)
    docs = resp.json()
    for doc in docs['hydra:member']:
        print(doc['@id'], doc['title'] if 'title' in doc else '---')
        client.index(index=index, id=doc['@id'], document=doc)
    time.sleep(1)

# récupération Classrooms, suivant swagger & affichage des résultats (title)
#get_list('/classrooms')

# Les briefs
for page in range(50,100):
    get_list('/briefs', 'p4-ego-brief', page=page)

get_list('/frameworks', 'p4-ego-framework')

