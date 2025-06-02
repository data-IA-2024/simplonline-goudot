import requests, dotenv, os, json, time

dotenv.load_dotenv()

EMAIL=os.environ['SIMPLON_EMAIL']
PASSWORD=os.environ['SIMPLON_PASSWORD']

from helium import *
# Ouvre la page
start_chrome('https://simplonline.co/')

# Accepter les conditions
click('Accepter')

# Page login
write(EMAIL, into='Adresse')
write(PASSWORD, into='Mot')
click('Se') # Se connecter

time.sleep(3) # Attente affichage

# Briefs
go_to('https://simplonline.co/trainer-workspace/briefs')
time.sleep(3) # Attente affichage
# Les titre des briefs : utilisation de selecteur CSS
divs = find_all(S("div.ant-card-body h2"))
#print(divs)
# Affichage des briefs
for div in divs:
    print(div.web_element.text)

kill_browser()