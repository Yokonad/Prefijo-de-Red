import ipaddress

def calcular_ips(prefijo):
    try:
        red = ipaddress.IPv4Network(f"0.0.0.0/{prefijo}", strict=False)
    except ValueError:
        return None

    total_ips = red.num_addresses
    utilizables = total_ips - 2 if total_ips > 2 else 0
    reservadas = total_ips - utilizables
    mascara_decimal = str(red.netmask)
    mascara_binaria = '.'.join(format(int(octeto), '08b') for octeto in mascara_decimal.split('.'))

    # Calcular Wildcard Mask
    octetos_mascara = [int(octeto) for octeto in mascara_decimal.split('.')]
    wildcard_decimal = '.'.join(str(255 - octeto) for octeto in octetos_mascara)
    wildcard_binaria = '.'.join(format(255 - int(octeto), '08b') for octeto in mascara_decimal.split('.'))

    return {
        "Prefijo CIDR": f"/{prefijo}",
        "Máscara (Decimal)": mascara_decimal,
        "Máscara (Binario)": mascara_binaria,
        "Wildcard (Decimal)": wildcard_decimal,
        "Wildcard (Binario)": wildcard_binaria,
        "Total de IPs": total_ips,
        "IPs Utilizables": utilizables,
        "Reservadas (Red + Broadcast)": reservadas,
    }

def mostrar_resultados():
    try:
        prefijo = int(input("Ingresa el prefijo CIDR (por ejemplo, 24 para /24): "))
        if not (0 < prefijo <= 32):
            raise ValueError("El prefijo debe estar entre 1 y 32.")

        resultado = calcular_ips(prefijo)
        if resultado:
            print("\nResultados:")
            for clave, valor in resultado.items():
                print(f"{clave}: {valor}")
        else:
            print("Prefijo inválido. Intenta con un número entre 1 y 32.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    while True:
        mostrar_resultados()
        continuar = input("\n¿Quieres calcular otro prefijo? (s/n): ").strip().lower()
        if continuar != 's':
            print("\nGracias por usar la calculadora de direcciones IP. ¡Hasta luego!")
            break
