import grpc
import calculadora_pb2
import calculadora_pb2_grpc

def main():
    canal = grpc.insecure_channel('localhost:50051')
    stub = calculadora_pb2_grpc.CalculadoraStub(canal)

    #Lectura por teclado
    try:
        a = float(input("Introduce el valor de a: "))
        b = float(input("Introduce el valor de b: "))
    except ValueError:
        print("Los valores deben ser números reales.")
        return

    operacion = calculadora_pb2.Operacion(a=a, b=b)
    
    #Suma
    respuesta_suma = stub.Suma(operacion)
    print(f"Resultado de la suma: {respuesta_suma.valor}")

    #Resta
    respuesta_resta = stub.Resta(operacion)
    print(f"Resultado de la resta: {respuesta_resta.valor}")

    # Multiplicación
    respuesta_mult = stub.Multiplicacion(operacion)
    print(f"Resultado de la multiplicación: {respuesta_mult.valor}")

    try:
        respuesta_div = stub.Division(operacion)
        print(f"Resultado de la división: {respuesta_div.valor}")
    except grpc.RpcError as e:
        if e.code() == grpc.StatusCode.INVALID_ARGUMENT:
            print(f"Error al dividir: {e.details()}")
        else:
            print(f"Error desconocido: {e}")


if __name__ == "__main__":
    main()

