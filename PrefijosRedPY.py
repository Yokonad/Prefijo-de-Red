import ipaddress
import tkinter as tk
from tkinter import messagebox

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

    return {
        "Prefijo CIDR": f"/{prefijo}",
        "Máscara (Decimal)": mascara_decimal,
        "Máscara (Binario)": mascara_binaria,
        "Total de IPs": total_ips,
        "IPs Utilizables": utilizables,
        "Reservadas (Red + Broadcast)": reservadas,
    }

def mostrar_resultados():
    try:
        prefijo = int(entry_prefijo.get())
        if not (0 < prefijo <= 32):
            raise ValueError
        resultado = calcular_ips(prefijo)
        if resultado:
            for widget in frame_resultados.winfo_children():
                widget.destroy()

            for i, (clave, valor) in enumerate(resultado.items()):
                texto = f"{clave}: {valor}"
                tk.Label(frame_resultados, text=texto, font=("Arial", 12), anchor="w", bg="white").pack(
                    anchor="w", padx=10, pady=5
                )
        else:
            messagebox.showerror("Error", "Prefijo inválido. Intenta con un número entre 1 y 32.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido entre 1 y 32.")

root = tk.Tk()
root.title("Calculadora de Direcciones IP")
root.geometry("600x450")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

titulo = tk.Label(root, text="Calculadora de Direcciones IP", font=("Arial", 16, "bold"), bg="#f2f2f2", pady=10)
titulo.pack()

instruccion = tk.Label(root, text="Ingresa el prefijo CIDR (por ejemplo, 24 para /24):", font=("Arial", 12), bg="#f2f2f2")
instruccion.pack(pady=5)

entry_prefijo = tk.Entry(root, font=("Arial", 14), justify="center", width=10)
entry_prefijo.pack(pady=5)

btn_calcular = tk.Button(
    root, text="Calcular", command=mostrar_resultados, font=("Arial", 12), bg="#4CAF50", fg="white", padx=20, pady=5
)
btn_calcular.pack(pady=10)

frame_container = tk.Frame(root, bd=2, relief="solid", bg="black", padx=2, pady=2)
frame_container.pack(fill="both", expand=True, padx=20, pady=10)

frame_resultados = tk.Frame(frame_container, bg="white", padx=10, pady=10)
frame_resultados.pack(fill="both", expand=True)

root.mainloop()
