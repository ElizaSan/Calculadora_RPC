import grpc
from concurrent import futures
import calculadora_pb2
import calculadora_pb2_grpc
import time, threading

class CalculadoraServicer(calculadora_pb2_grpc.CalculadoraServicer):
    lock = threading.Lock()

    def block(self, request, context):
        if not self.lock.acquire(blocking=False):
            context.set_code(grpc.StatusCode.RESOURCE_EXHAUSTED)
            context.set_details("Servidor ocupado. Intenta más tarde.")
            return calculadora_pb2.Resultado()
    
    def Suma(self, request, context):

        self.block(request, context)

        try:
            peer = context.peer()
            print(f"Conexión recibida de: {peer}")
            print(f"Solicitud de suma: {request.a} + {request.b}")
            resultado = request.a + request.b
            time.sleep(5)  
            return calculadora_pb2.Resultado(valor=resultado)
        except Exception as e:
            print(f"Error procesando la solicitud: {e}")
            context.set_details("Error interno al sumar.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return calculadora_pb2.Resultado()
        finally: 
            self.lock.release()

    
    def Resta(self, request, context):

        self.block(request, context)
        try:
            peer = context.peer()
            print(f"Conexión recibida de: {peer}")
            print(f"Solicitud de resta recibida: {request.a} + {request.b}")
            time.sleep(5) 
            resultado = request.a - request.b
            return calculadora_pb2.Resultado(valor=resultado)
        except Exception as e:
            print(f"Error procesando la solicitud: {e}")
            context.set_details("Error interno al restar.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return calculadora_pb2.Resultado()
        finally: 
            self.lock.release()



    def Multiplicacion(self, request, context):
        self.block(request, context)
        try:
            peer = context.peer()
            print(f"Conexión recibida de: {peer}")
            print(f"Solicitud de multiplicacion recibida: {request.a} + {request.b}")
            time.sleep(5) 
            resultado = request.a * request.b
            return calculadora_pb2.Resultado(valor=resultado)
        except Exception as e:
            print(f"Error procesando la solicitud: {e}")
            context.set_details("Error interno al multiplicar.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return calculadora_pb2.Resultado()
        finally: 
            self.lock.release()
    
    def Division(self, request, context):
        self.block(request, context)
        print(f"Solicitud de division recibida: {request.a} + {request.b}")
        try:
            peer = context.peer()
            print(f"Conexión recibida de: {peer}")
            if request.b == 0:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("No se puede dividir entre cero")
                return calculadora_pb2.Resultado(valor=0)
            time.sleep(5) 
            resultado = request.a / request.b
            return calculadora_pb2.Resultado(valor=resultado)  
        except Exception as e:
            print(f"Error procesando la solicitud: {e}")
            context.set_details("Error interno al dividir.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return calculadora_pb2.Resultado()
        finally: 
            self.lock.release()


def servir():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculadora_pb2_grpc.add_CalculadoraServicer_to_server(CalculadoraServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor corriendo en el puerto 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    servir()
