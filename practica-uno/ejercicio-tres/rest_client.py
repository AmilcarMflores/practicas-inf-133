import requests

url = "http://localhost:8000/"

#POST /pacientes
nuevo_paciente = {
  "ci": 13212241,
  "nombre": "María",
  "apellido": "Lopez",
  "edad": 32,
  "genero": "Femenino",
  "diagnostico": "Gripe",
  "doctor": "Carlos Mesa",
}
ruta_post = url + "pacientes"
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_paciente)
# print(nuevo_paciente)
# print(post_response.text)

#GET /pacientes
ruta_get = url + "pacientes"
get_response = requests.request(method="GET", url=ruta_get)
# print(get_response.text)

#GET /pacientes/{ci}
ruta_filtrar_nombre_ci = url + "pacientes/13021224"
filtrar_nombre_response_ci = requests.request(method="GET", url=ruta_filtrar_nombre_ci)
#print(filtrar_nombre_response_ci.text)

#GET /pacientes/?diagnostico={diagnostico}
ruta_get = url + "pacientes?diagnostico=Diabetes"
get_response = requests.request(method="GET", url=ruta_get)
#print(get_response.text)

#GET /pacientes/?doctor={doctor}
ruta_get = url + "pacientes?doctor=Pedro Pérez"
get_response = requests.request(method="GET", url=ruta_get)
#print(get_response.text)

# PUT /pacientes/{ci}
ruta_actualizar = url + "pacientes/13212240"
paciente_actualizado = {
  "ci": 12315541,
  "nombre": "Erick",
  "apellido": "Cartman",
  "edad": 8,
  "genero": "Masculino",
  "diagnostico": "Fiebre",
  "doctor": "Randy Orton",
}
put_response = requests.request(method="PUT", url=ruta_actualizar, json=paciente_actualizado)
# print(paciente_actualizado)
# print(put_response.text)

# DELETE /pacientes/{ci}
ruta_eliminar = url + "pacientes/13021224"
delete_response = requests.request(method="DELETE", url=ruta_eliminar)
print(delete_response.text)