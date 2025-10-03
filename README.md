**Práctica RPC - Sistemas Distribuidos**

Instrucciones: Implementar una calculadora con cuatro operaciones (suma, resta, multiplicación, división) que se ejecute con:

* Conectividad RPC, Cliente - Servidor Local
* Conectividad RPC, Cliente - Servidor (varios dispositivos)
* Corroborar envío de mensajes de fallo tanto en servidor, petición del cliente y funciones
* Las entradas de los datos los ingresa el usuario (cliente)


Esta práctica se elaboró utilizando Python con gRPC

**Comando para actualizar el código calculadora.protoc**
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. calculadora.proto

Posteriormente
calculadora_pb2_grpc.py y calculadora_pb2.py se generan de forma automática la primera vez o se actualizan después de ser generados.

**Instalar dependencias (gRPC)**
pip install grpcio grpcio-tools


**Como ejecutar**
1. Ejecuta el servidor con:
python3 servidor.py desde la terminal

2. En otra terminal ejecuta python3 cliente.py