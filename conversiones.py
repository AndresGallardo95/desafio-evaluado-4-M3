import sys

def convertir_divisas(tasa_sol, tasa_peso_arg, tasa_dolar, valor_chileno):
    valor_sol = valor_chileno * tasa_sol
    valor_peso_arg = valor_chileno * tasa_peso_arg
    valor_dolar = valor_chileno * tasa_dolar
    return valor_sol, valor_peso_arg, valor_dolar

if __name__ == "__main__":
    # Tasas de conversión almacenadas internamente
    tasa_sol = 0.0046
    tasa_peso_arg = 0.093
    tasa_dolar = 0.0013

    # Verificar que se haya pasado el argumento desde la línea de comandos
    if len(sys.argv) != 2:
        print("Uso: python conversiones.py <valor_chileno>")
        sys.exit(1)

    try:
        valor_chileno = float(sys.argv[1])
    except ValueError:
        print("Por favor, ingrese un número válido.")
        sys.exit(1)

    valor_sol, valor_peso_arg, valor_dolar = convertir_divisas(tasa_sol, tasa_peso_arg, tasa_dolar, valor_chileno)

    print(f"Valor en Soles Peruanos: {valor_sol:.2f}")
    print(f"Valor en Pesos Argentinos: {valor_peso_arg:.2f}")
    print(f"Valor en Dólares Americanos: {valor_dolar:.2f}")

