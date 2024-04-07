from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler


#Las cuatro operaciones básicas
def suma(num1, num2):
  return num1 + num2

def resta(num1, num2):
  return num1 - num2

def multiplicacion(num1, num2):
  return num1 * num2

def division(num1, num2):
  if num2 == 0:
    raise ValueError("El dividendo no puede ser cero")
  return num1 // num2

dispatcher = SoapDispatcher(
  "soap-server",
  location="http://localhost:8000",
  action="http://localhost:8000",
  namespace="http://localhost:8000",
  trace=True,
  ns=True,
)
dispatcher.register_function(
  "SumaDosNumeros",
  suma,
  returns={"resultado": int},
  args={"num1": int, "num2": int},
)
dispatcher.register_function(
  "RestaDosNumeros",
  resta,
  returns={"resultado": int},
  args={"num1": int, "num2": int},
)
dispatcher.register_function(
  "MultiplicacionDosNumeros",
  multiplicacion,
  returns={"resultado": int},
  args={"num1": int, "num2": int},
)
dispatcher.register_function(
  "DivisionDosNumeros",
  division,
  returns={"resultado": int},
  args={"num1": int, "num2": int},
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()