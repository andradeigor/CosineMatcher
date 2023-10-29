#/* Disciplina: Programacao Concorrente */
#/* Prof.: Silvana Rossetto */
#/* Módulo 4 - Laboratório: 7 */
#/* Codigo: exemplo de aplicacao IO-bound */ 


#extraido de: "Python 3 Object-oriented Programming" (Cap 13), Dusty Phillips, 2nd edition, 2015  
#WeatherAPI (https://www.weatherapi.com/) 

from threading import Thread
import requests
import time

CITIES = ['Sao Paulo', 'Rio de Janeiro', 'Salvador', 'Porto Alegre', "Macapa", 
        'Manaus', 'Natal', 'Belo Horizonte', 'Vitoria', 'Rio Branco']

class TempGetter(Thread):
    def __init__(self, city):
        super().__init__()
        self.city = city

    def run(self):
        chave_api = "sua chave"
        url = f"http://api.weatherapi.com/v1/current.json?key={chave_api}&q={self.city}"
        try:
            response = requests.get(url)
            data = response.json()
            self.local = data["location"]["name"]
            self.temperature = data["current"]["temp_c"]
            self.condition = data["current"]["condition"]["text"]
        except requests.exceptions.RequestException as e:
            print("Conection error:", e)

threads = [TempGetter(c) for c in CITIES]
start = time.time()

for thread in threads:
    thread.start()
 #   thread.run()

for thread in threads:
    thread.join()

for thread in threads:
    print("Tempo em {0.local}: {0.temperature:.0f}°C and {0.condition}".format(thread))

print("Got {} temps in {} seconds".format(len(threads), time.time() - start))








