from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from urllib.parse import urlparse, parse_qs

#Pacientes de un hospital
pacientes = [
  {
    "ci": 13212240,
    "nombre": "Juan",
    "apellido": "Pérez",
    "edad": 45,
    "genero": "Masculino",
    "diagnostico": "Hipertensión",
    "doctor": "Pedro Pérez",
  },
  {
    "ci": 13021224,
    "nombre": "Luis",
    "apellido": "Gonzáles",
    "edad": 60,
    "genero": "Masculino",
    "diagnostico": "Diabetes",
    "doctor": "María Galindo",
  },
]

class RESTRequestHandler(BaseHTTPRequestHandler):
  def response_handler(self, status, data):
    self.send_response(status)
    self.send_header("Content-type", "application/json")
    self.end_headers()
    self.wfile.write(json.dumps(data).encode("utf-8"))
    
  def read_data(self):
    content_length = int(self.headers["Content-Length"])
    data = self.rfile.read(content_length)
    data = json.loads(data.decode("utf-8"))
    return data
  
  def find_paciente_ci(self, ci):
    return next(
      (paciente for paciente in pacientes if paciente["ci"] == ci),
      None,
    )
  def find_paciente_diagnostico(self, diagnostico):
    return next(
      (paciente for paciente in pacientes if paciente["diagnostico"] == diagnostico),
      None,
    )
  
  def do_GET(self):
    parsed_path = urlparse(self.path)
    query_params = parse_qs(parsed_path.query)
    
    if self.path == "/pacientes":
      self.response_handler(200, pacientes)
    #Buscar paciente por CI
    elif self.path.startswith("/pacientes/"):
      ci = int(self.path.split("/")[-1])
      paciente = self.find_paciente_ci(ci)
      if paciente:
        self.response_handler(200, [paciente])
      else:
        self.response_handler(204, [])
    #Listar a los pacientes que tienen diagnostico de Diabetes
    elif parsed_path.path == '/pacientes':
      if 'diagnostico' in query_params:
        diagnostico = query_params['diagnostico'][0]
        pacientes_filtrados = [
          paciente
          for paciente in pacientes
          if paciente['diagnostico'] == diagnostico
        ]
        if pacientes_filtrados != []:
          self.response_handler(200, pacientes_filtrados)
        else:
          self.response_handler(204, [])
      elif 'doctor' in query_params:
        doctor = query_params['doctor'][0]
        pacientes_filtrados = [
          paciente
          for paciente in pacientes
          if paciente['doctor'] == doctor
        ]
        if pacientes_filtrados != []:
          self.response_handler(200, pacientes_filtrados)
        else:
          self.response_handler(204, []) 
    else:
      self.response_handler(404, {"Error": "Ruta no existente"})

  def do_POST(self):
    if self.path == "/pacientes":
      data = self.read_data()
      data["id"] = len(pacientes) + 1
      pacientes.append(data)
      self.response_handler(201, pacientes)

    else:
      self.response_handler(404, {"Error": "Ruta no existente"})

  def do_PUT(self):
    if self.path.startswith("/pacientes/"):
      ci = int(self.path.split("/")[-1])
      paciente = self.find_paciente_ci(ci)
      data = self.read_data()
      if paciente:
        paciente.update(data)
        self.response_handler(200, [pacientes])
      else:
        self.response_handler(404, {"Error": "Paciente no encontrado"})
    else:
      self.response_handler(404, {"Error": "Ruta no existente"})

  def do_DELETE(self):
    if self.path.startswith("/pacientes/"):
      ci = int(self.path.split("/")[-1])
      paciente = self.find_paciente_ci(ci)
      if paciente:
        pacientes.remove(paciente)
        self.response_handler(200, pacientes)
      else:
        self.response_handler(404, {"Error": "Paciente no encontrado"})
    else:
      self.response_handler(404, {"Error": "Ruta no existente"})
      
def run_server(port=8000):
  try:
    server_address = ("", port)
    httpd = HTTPServer(server_address, RESTRequestHandler)
    print(f"Iniciando servidor web en http://localhost:{port}/")
    httpd.serve_forever()
  except KeyboardInterrupt:
    print("Apagando servidor web")
    httpd.socket.close()

if __name__=="__main__":
  run_server()
  