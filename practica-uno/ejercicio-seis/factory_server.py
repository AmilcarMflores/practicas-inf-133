from http.server import HTTPServer, BaseHTTPRequestHandler
import json

#base de datos
animales = {}

#Superclase
class Animales:
  def __init__(self, animal_type, nombre, especie, genero, edad, peso):
    self.animal_type = animal_type
    self.nombre = nombre
    self.especie = especie
    self.genero = genero
    self.edad = edad
    self.peso = peso
  
class Mamifero(Animales):
  def __init__(self, nombre, especie, genero, edad, peso):
    super().__init__("mamifero", nombre, especie, genero, edad, peso)

class Ave(Animales):
  def __init__(self, nombre, especie, genero, edad, peso):
    super().__init__("ave", nombre, especie, genero, edad, peso)

class Reptil(Animales):
  def __init__(self, nombre, especie, genero, edad, peso):
    super().__init__("reptil", nombre, especie, genero, edad, peso)

class Anfibio(Animales):
  def __init__(self, nombre, especie, genero, edad, peso):
    super().__init__("anfibio", nombre, especie, genero, edad, peso)

class Pez(Animales):
  def __init__(self, nombre, especie, genero, edad, peso):
    super().__init__("pez", nombre, especie, genero, edad, peso)
    
class AnimalFactory:
  @staticmethod
  def create_animal(animal_type, nombre, especie, genero, edad, peso):
    if animal_type == "mamifero":
      return Mamifero(nombre, especie, genero, edad, peso)
    elif animal_type == "ave":
      return Ave(nombre, especie, genero, edad, peso)
    elif animal_type == "reptil":
      return Reptil(nombre, especie, genero, edad, peso)
    elif animal_type == "anfibio":
      return Anfibio(nombre, especie, genero, edad, peso)
    elif animal_type == "pez":
      return Pez(nombre, especie, genero, edad, peso)
    else:
      raise ValueError("Tipo de animal no válido")
    
class HTTPDataHandler:
  @staticmethod
  def handle_response(handler, status, data):
    handler.send_response(status)
    handler.send_header("Content-type", "application/json")
    handler.end_headers()
    handler.wfile.write(json.dumps(data).encode("utf-8"))
  
  @staticmethod
  def handler_reader(handler):
    content_length = int(handler. headers["Content-Length"])
    post_data = handler.rfile.read(content_length)
    return json.loads(post_data.decode("utf-8"))
  
class AnimalService:
  def __init__(self):
    self.factory = AnimalFactory()
    
  def add_animal(self, data):
    animal_type = data.get("animal_type", None)
    nombre = data.get("nombre", None)
    especie = data.get("especie", None)
    genero = data.get("genero", None)
    edad = data.get("edad", None)
    peso = data.get("peso", None)

    animal_producto = self.factory.create_animal(
      animal_type, nombre, especie, genero, edad, peso)
    
    animales[len(animales) + 1] = animal_producto
    return animal_producto
  
  def list_animales(self):
    return {index: animales.__dict__ for index, animal in animales.items()}
  
  def update_animal(self, animal_id, data):
    if animal_id in animales:
      animal = animales[animal_id]
      nombre = data.get("nombre", None)
      especie = data.get("especie", None)
      genero = data.get("genero", None)
      edad = data.get("edad", None)
      peso = data.get("peso", None)
      if nombre:
        animal.nombre = nombre
      if especie:
        animal.especie = especie
      if genero:
        animal.genero = genero
      if edad:
        animal.edad = edad
      if peso:
        animal.peso = peso
      return animal
    else:
      raise None
  
  def delete_animal(self, animal_id):
    if animal_id in animales:
      del animales[animal_id]
      return {"message": "Animal eliminado"}
    else:
      return None
  
class AnimalRequestHandler(BaseHTTPRequestHandler):
  def __init__(self, *args, **kwargs):
    self.animal_service = AnimalService()
    super().__init__(*args, **kwargs)
    
  def do_POST(self):
    if self.path == "/animales":
      data = HTTPDataHandler.handler_reader(self)
      response_data = self.animal_service.add_animal(data)
      HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
      
    else:
      HTTPDataHandler.handle_response(
        self, 404, {"message": "Ruta no encontrada"}
      )
  
  def do_GET(self):
    if self.path == "/animales":
      response_data = self.animal_service.list_animales()
      HTTPDataHandler.handle_response(self, 200, response_data)
    else:
      HTTPDataHandler.handle_response(self, 404, {"message": "Ruta no encontrada"})
      
  def do_PUT(self):
    if self.path.startswith("/animales/"):
      animal_id = int(self.path.split("/")[-1])
      data = HTTPDataHandler.handler_reader(self)
      response_data = self.animal_service.update_animal(animal_id, data)
      if response_data:
        HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
      else:
        HTTPDataHandler.handle_response(self, 404, {"message": "Ruta no encontrada"})
    else:
      HTTPDataHandler.handle_response(self, 404, {"message": "Ruta no encontrada"})
      
  def do_DELETE(self):
    if self.path.startswith("/animales/"):
      animal_id = int(self.path.split("/")[-1])
      response_data = self.animal_service.delete_animal(animal_id)
      if response_data:
        HTTPDataHandler.handle_response(self, 200, response_data)
      else:
        HTTPDataHandler.handle_response(self, 404, {"message": "Animal no encontrado"})
    else:
      HTTPDataHandler.handle_response(self, 404, {"message": "Ruta no encontrada"})

def main():
  try:
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, AnimalRequestHandler)
    print("Iniciando servidor HTTP en puerto 8000...")
    httpd.serve_forever()
  except KeyboardInterrupt:
    print("Apagando servidor HTTP")
    httpd.socket.close()
    
if __name__ == "__main__":
  main()