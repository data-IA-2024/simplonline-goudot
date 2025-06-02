import requests, dotenv, os, json, time

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
#print(TOKEN)
headers['Authorization']=f"Bearer {TOKEN}"

params={'pagination':'true', 'page':1, 'perPage':30}

# Requète les données & les affiche ('hydra:member')
def get_list(path):
    print(f"-------------- {path} --------------")
    resp = requests.get(URL+path, headers=headers, params=params)
    docs = resp.json()
    for doc in docs['hydra:member']:
        print(doc['@id'], doc['title'] if 'title' in doc else '---')
    time.sleep(1)

# récupération Classrooms, suivant swagger & affichage des résultats (title)
get_list('/classrooms')

# Les briefs
get_list('/briefs')

# Les framework
get_list('/frameworks')

get_list('/factories')
get_list('/follow_ups')
#get_list('/group_corrections')
get_list('/missions')
get_list('/professional_situations')
get_list('/skills')
get_list('/skill_levels')
