# simplonline-goudot
Extract Simplonline

Extraction de données de Simplonline.co  
-> Une API existe : https://api.simplonline.co/  

## Installation
```bash
 python3 -m venv venv
 source venv/bin/activate
 pip install -r requirements.txt
```

## Utilisation API
```bash
 source venv/bin/activate
 python demo1.py
```

## Execution FastAPI
````bash
 fastapi dev main.py
```

## Scrapping 'dur'
```bash
 source venv/bin/activate
 python scrapping.py
```
Résultat:
```text
(venv) $ python scrapping.py 
dataIA - MOOC 2025
Copie de dataIA - MOOC 2025
Les bases de l'IOT
Application d'optimisation domotique
Veille "IA"
Développer une interface OCR avec Azure
Projet OCR - Analyse de Factures et Clustering
Développement d'une Application de Gestion de courses avec LocalStorage
Veille "Cloud"
```
```json
GET /p4-egobriefs/_search
{
  "query": {
    "match": {
      "title": {
        "query": "champions"
      }
    }
  }
}
```

```bash
 uvicorn sampleAPI:app --host 0.0.0.0 --port 8000 --reload
```