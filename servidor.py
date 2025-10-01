import grpc
from concurrent import futures
import calculadora_pb2
import calculadora_pb2_grpc

class CalculadoraServicer(calculadora_pb2_grpc.CalculadoraServicer):
    def Suma(self, request, context):
        resultado = request.a + request.b
        return calculadora_pb2.Resultado(valor=resultado)
    
    def Resta(self, request, context):
        resultado = request.a - request.b
        return calculadora_pb2.Resultado(valor=resultado)

    def Multiplicacion(self, request, context):
        resultado = request.a * request.b
        return calculadora_pb2.Resultado(valor=resultado)
    
    def Division(self, request, context):
        if request.b == 0:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("No se puede dividir entre cero")
            return calculadora_pb2.Resultado(valor=0)
        resultado = request.a / request.b
        return calculadora_pb2.Resultado(valor=int(resultado))  # O usar float si lo prefieres


def servir():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculadora_pb2_grpc.add_CalculadoraServicer_to_server(CalculadoraServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor corriendo en el puerto 50051...")
    server.wait_for_termination()

if __name__ == "__main__":
    servir()
