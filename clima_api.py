import requests
import time

API_KEY = "1d31cfc716860b846e4b05ac20c91322"
CIDADE = "Sao Paulo"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={"Sao Paulo"}&appid={"1d31cfc716860b846e4b05ac20c91322"}&units=metric&lang=pt_br"

def check_weather():
    try:
        response = requests.get(URL)
        data = response.json()
        
        
        main_weather = data['weather'][0]['main']
        description = data['weather'][0]['description']
        temp = data['main']['temp']

        print(f"\n--- API FarmTech: {CIDADE} ---")
        print(f"Temperatura: {temp}°C | Condição: {description}")

        if main_weather == "Rain":
            print("COMANDO PARA O WOKWI: Digite 'C' e aperte Enter (Vai chover!)")
        else:
            print("COMANDO PARA O WOKWI: Digite 'S' e aperte Enter (Sem previsão de chuva)")

    except Exception as e:
        print("Erro ao conectar na API:", e)

while True:
    check_weather()
    print("Aguardando 30 segundos para próxima verificação...")
    time.sleep(30)