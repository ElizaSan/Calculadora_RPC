import grpc
import calculadora_pb2
import calculadora_pb2_grpc

def pedir_operando(nombre):
    while True:
        try:
            return float(input(f"Introduce el valor de {nombre}: "))
        except ValueError:
            print("Entrada inválida. Debes ingresar un número real.")

def mostrar_menu():
    print("\n------ CALCULADORA RPC ------")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("0. Salir")

    while True:
        opcion = input("Selecciona una opción: ")
        if opcion in {"1", "2", "3", "4", "0"}:
            return opcion
        print("Opción inválida.")

def main():
    canal = grpc.insecure_channel('localhost:50051')
    stub = calculadora_pb2_grpc.CalculadoraStub(canal)

    while True:
        
        opcion = mostrar_menu()

        if opcion == "0":
            print("Saliendo del programa.")
            break

        a = pedir_operando("a")
        b = pedir_operando("b")
        operacion = calculadora_pb2.Operacion(a=a, b=b)

        try:
            if opcion == "1":
                resultado = stub.Suma(operacion)
                print(f"Resultado de la suma: {resultado.valor}")
            elif opcion == "2":
                resultado = stub.Resta(operacion)
                print(f"Resultado de la resta: {resultado.valor}")
            elif opcion == "3":
                resultado = stub.Multiplicacion(operacion)
                print(f"Resultado de la multiplicación: {resultado.valor}")
            elif opcion == "4":
                resultado = stub.Division(operacion)
                print(f"Resultado de la división: {resultado.valor}")
        except grpc.RpcError as e:
            print(f"Error en la operación: {e.code().name} - {e.details()}")

if __name__ == "__main__":
    main()
