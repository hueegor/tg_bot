import requests


url = 'https://wttr.in'

weather_parameters = {
    '0' : '', #Текущая погода
    'T' : '', #Тихая версия
    'lang': 'ru' #Язык
}

responce = requests.get(url,params=weather_parameters)

print(responce.text)



#url = 'https://yandex.ru/search/'
#response = requests.get(url)
#print(response.status_code)

