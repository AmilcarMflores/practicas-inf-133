import requests

url = "http://localhost:8000/"

#POST /animales
nuevo_animal = {
  "id": 3,
  "nombre": "Paco",
  "especie": "Melopsittacus undulatus",
  "genero": "Macho",
  "edad": 1,
  "peso": 0.05,
}

ruta_post = url + "animales"
post_response = requests.request(method="POST", url= ruta_post, json=nuevo_animal)
print(nuevo_animal)
print(post_response.text)

#GET /animales
ruta_get = url + "animales"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

#GET /animales?especie={especie}
ruta_get = url + "animales?especie=Canis lupus familiaris"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

#GET /animales/?genero={genero}
ruta_get = url + "animales?genero=Hembra"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

#PUT /animales/{id}
ruta_actualizar = url + "animales/1"
animal_actualizado = {
  "id": 1,
  "nombre": "Coco",
  "especie": "Oryctolagus cuniculus",
  "genero": "Hembra",
  "edad": 3,
  "peso": 2.2,
}
put_response = requests.request(method="PUT", url=ruta_actualizar, json=animal_actualizado)
print(animal_actualizado)
print(put_response.text)

#DELETE /animales/{id}
ruta_eliminar = url + "animales/3"
delete_reponse = requests.request(method="DELETE", url=ruta_eliminar)
print(delete_reponse.text)