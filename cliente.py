import grpc
import calculadora_pb2
import calculadora_pb2_grpc

def main():
    canal = grpc.insecure_channel('localhost:50051')
    stub = calculadora_pb2_grpc.CalculadoraStub(canal)

    operacion = calculadora_pb2.Operacion(a=10, b=7)
    
    #Suma
    respuesta_suma = stub.Suma(operacion)
    print(f"Resultado de la suma: {respuesta_suma.valor}")

    #Resta
    respuesta_resta = stub.Resta(operacion)
    print(f"Resultado de la resta: {respuesta_resta.valor}")

    # Multiplicación
    respuesta_mult = stub.Multiplicacion(operacion)
    print(f"Resultado de la multiplicación: {respuesta_mult.valor}")

    #Division
    respuesta_div = stub.Division(operacion)
    print(f"Resultado de la división: {respuesta_div.valor}")

if __name__ == "__main__":
    main()

