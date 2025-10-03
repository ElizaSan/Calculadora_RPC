import grpc
from concurrent import futures
import calculadora_pb2
import calculadora_pb2_grpc

class CalculadoraServicer(calculadora_pb2_grpc.CalculadoraServicer):

    
    def Sumar(self, request, context):
        try:
            resultado = request.a + request.b
            return calculadora_pb2.Resultado(valor=resultado)
        except Exception as e:
            print(f"Error procesando la solicitud: {e}")
            context.set_details("Error interno al sumar.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return calculadora_pb2.Resultado()


    
    def Resta(self, request, context):
        try:
            resultado = request.a - request.b
            return calculadora_pb2.Resultado(valor=resultado)
        except Exception as e:
            print(f"Error procesando la solicitud: {e}")
            context.set_details(["Error interno al restar."])
            context.set_code(grpc.StatusCode.INTERNAL)
            return calculadora_pb2.Resultado()



    def Multiplicacion(self, request, context):
        try:
            resultado = request.a * request.b
            return calculadora_pb2.Resultado(valor=resultado)
        except Exception as e:
            print(f"Error procesando la solicitud: {e}")
            context.set_details("Error interno al multiplicar.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return calculadora_pb2.Resultado()
    
    def Division(self, request, context):
        try:
            if request.b == 0:
                context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
                context.set_details("No se puede dividir entre cero")
                return calculadora_pb2.Resultado(valor=0)
            resultado = request.a / request.b
            return calculadora_pb2.Resultado(valor=int(resultado))  
        except Exception as e:
            print(f"Error procesando la solicitud: {e}")
            context.set_details("Error interno al multiplicar.")
            context.set_code(grpc.StatusCode.INTERNAL)
            return calculadora_pb2.Resultado()


def servir():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculadora_pb2_grpc.add_CalculadoraServicer_to_server(CalculadoraServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor corriendo en el puerto 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    servir()
