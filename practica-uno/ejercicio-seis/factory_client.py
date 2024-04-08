import requests
import json 

url = "http://localhost:8000/animales"
headers = {"Content-Type": "application/json"}

#GET
response = requests.get(url=url)
print(response.json())

#POST
new_animal_data = {
  #animal_type, nombre, especie, genero, edad, peso
  "animal_type": "mamifero",
  "nombre": "Luna",
  "especie": "Felis catus",
  "edad": 2,
  "peso": 4.5, 
}
response = requests.post(url=url, json=new_animal_data, headers=headers)
print(response.json())

