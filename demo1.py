import requests, dotenv, os, json

dotenv.load_dotenv()

EMAIL=os.environ['SIMPLON_EMAIL']
PASSWORD=os.environ['SIMPLON_PASSWORD']
URL="https://api.simplonline.co"


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
print(TOKEN)
headers['Authorization']=f"Bearer {TOKEN}"

# récupération Classrooms, suivant swagger & affichage des résultats (title)
params={'page':'1', 'perPage':'30', 'pagination':'true'}
resp = requests.get(URL+'/classrooms', headers=headers, params=params)
classrooms = resp.json()
for cr in classrooms['hydra:member']:
    print(cr['title'])