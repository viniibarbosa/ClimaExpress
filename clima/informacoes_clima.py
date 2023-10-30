import requests
from django.utils import timezone
from dotenv import load_dotenv
import os
def informacoes_clima(cidade):
    load_dotenv(override=True)
    
    API_KEY = os.getenv("API_KEY")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}'
    json = faz_requisicao(url)
    
    if json.status_code == 200:
        dicianario_clima = formata_json(json)
    else:
        dicianario_clima = dados_nao_encontrado()
    
    return dicianario_clima
    
def faz_requisicao(url):
    req = requests.get(url)
    req.status_code == 200
    return req

def formata_json(json):
    json = json.json()
    dicionario = {'nome': json['name'],
                  'pais': json['sys']['country'],
                  'icon': json['weather'][0]['icon'],
                  'temp_max': str(round(float(json['main']['temp_max'])-273.15,1)),
                  'temp_min': str(round(float(json['main']['temp_min'])-273.15,1)), 
                  'temp': str(round(float(json['main']['temp'])-273.15,1)),
                  'data': timezone.now()
                  }
    return dicionario

def dados_nao_encontrado():
    dicionario = {
        'dados' : 'Não foi possível localizar essa cidade'
    }
    return dicionario