import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

AUTOR = "Rafael Cubides Rangel"
CLAVE = "1793"

PRECIOS = {
    "Menú ejecutivo": 35000,
    "Menú vegetariano": 28000,
    "Menú degustación": 75000,
    "Menú infantil": 20000,
    "Menú gourmet": 95000,
}


def formatear_moneda(valor):
    return "$ " + f"{valor:,.0f}".replace(",", ".")


class GestionClientes:
    def __init__(self, identificacion, nombre, genero, tipo_menu,
                 numero_sesiones, costo_sesion, fecha_registro):
        self.identificacion = identificacion
        self.nombre = nombre
        self.genero = genero
        self.tipo_menu = tipo_menu
        self.numero_sesiones = numero_sesiones
        self.costo_sesion = costo_sesion
        self.fecha_registro = fecha_registro

    def calcular_costo_total(self, numero_sesiones, costo_sesion):
        return numero_sesiones * costo_sesion


class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Sabor & Sazón - Acceso")
        self.ventana.geometry("480x420")
        self.ventana.resizable(False, False)
        self.ventana.configure(bg="#EFEAE3")

        self.color_principal = "#1B4B43"
        self.color_secundario = "#B08A3E"
        self.color_fondo = "#EFEAE3"
        self.color_salir = "#8C2F2F"

        self.cliente_guardado = None
        self.mostrar_acceso()

    def limpiar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def encabezado(self, texto):
        marco = tk.Frame(self.ventana, bg=self.color_principal, height=90)
        marco.pack(fill="x")
        marco.pack_propagate(False)
        tk.Label(marco, text="SABOR & SAZÓN", bg=self.color_principal, fg="white",
                 font=("Verdana", 18, "bold")).pack(pady=(15, 0))
        tk.Label(marco, text=texto, bg=self.color_principal, fg="white",
                 font=("Verdana", 10)).pack()

    def mostrar_acceso(self):
        self.limpiar()
        self.ventana.title("Sabor & Sazón - Acceso")
        self.encabezado("Sistema de Gestión de Clientes")

        marco = tk.Frame(self.ventana, bg="white", padx=25, pady=20)
        marco.pack(padx=30, pady=20, fill="both", expand=True)

        tk.Label(marco, text="Universidad Nacional Abierta y a Distancia", bg="white",
             font=("Verdana", 9)).pack()
        tk.Label(marco, text="Ing de Sistemas", bg="white", fg="gray",
             font=("Verdana", 10, "italic")).pack()
        tk.Label(marco, text=AUTOR, bg="white", fg=self.color_principal,
             font=("Verdana", 13, "bold")).pack(pady=(6, 20))

        tk.Label(marco, text="Ingrese la contraseña", bg="white",
                 font=("Verdana", 10, "bold")).pack(anchor="w")
        self.entrada_clave = tk.Entry(marco, show="*", font=("Verdana", 13), justify="center")
        self.entrada_clave.pack(fill="x", pady=8)
        self.entrada_clave.focus()
        self.entrada_clave.bind("<Return>", lambda e: self.validar_clave())

        tk.Label(marco, text="La contraseña está enmascarada", bg="white", fg="gray",
                 font=("Verdana", 9)).pack(pady=(0, 15))

        tk.Button(marco, text="Ingresar al sistema", command=self.validar_clave,
                  bg=self.color_principal, fg="white", font=("Verdana", 11, "bold"),
                  relief="flat", padx=10, pady=8).pack(fill="x")

    def validar_clave(self):
        if self.entrada_clave.get() == CLAVE:
            self.mostrar_registro()
        else:
            messagebox.showerror("Acceso denegado", "La contraseña no es correcta")
            self.entrada_clave.delete(0, tk.END)

    def mostrar_registro(self):
        self.limpiar()
        self.ventana.title("Sabor & Sazón - Registro de Cliente")
        self.ventana.geometry("620x640")
        self.encabezado("Registro de Cliente")

        form = tk.Frame(self.ventana, bg="white", padx=20, pady=15)
        form.pack(padx=25, pady=10, fill="both", expand=True)
        form.columnconfigure(1, weight=1)

        tk.Label(form, text="Identificación:", bg="white", font=("Verdana", 10, "bold")).grid(row=0, column=0, sticky="w", pady=8)
        self.entrada_id = tk.Entry(form, font=("Verdana", 10))
        self.entrada_id.grid(row=0, column=1, sticky="ew", pady=8)

        tk.Label(form, text="Nombre completo:", bg="white", font=("Verdana", 10, "bold")).grid(row=1, column=0, sticky="w", pady=8)
        self.entrada_nombre = tk.Entry(form, font=("Verdana", 10))
        self.entrada_nombre.grid(row=1, column=1, sticky="ew", pady=8)

        tk.Label(form, text="Género:", bg="white", font=("Verdana", 10, "bold")).grid(row=2, column=0, sticky="w", pady=8)
        self.genero = tk.StringVar(value="Masculino")
        marco_genero = tk.Frame(form, bg="white")
        marco_genero.grid(row=2, column=1, sticky="w", pady=8)
        tk.Radiobutton(marco_genero, text="Masculino", variable=self.genero, value="Masculino", bg="white").pack(side="left")
        tk.Radiobutton(marco_genero, text="Femenino", variable=self.genero, value="Femenino", bg="white").pack(side="left", padx=10)

        tk.Label(form, text="Tipo de menú:", bg="white", font=("Verdana", 10, "bold")).grid(row=3, column=0, sticky="w", pady=8)
        self.menu = tk.StringVar()
        combo = ttk.Combobox(form, textvariable=self.menu, values=list(PRECIOS.keys()), state="readonly")
        combo.grid(row=3, column=1, sticky="ew", pady=8)
        combo.current(0)
        combo.bind("<<ComboboxSelected>>", self.actualizar_costo)

        tk.Label(form, text="Costo por unidad:", bg="white", font=("Verdana", 10, "bold")).grid(row=4, column=0, sticky="w", pady=8)
        self.entrada_costo = tk.Entry(form, state="readonly", readonlybackground="#E8E8E8", font=("Verdana", 10))
        self.entrada_costo.grid(row=4, column=1, sticky="ew", pady=8)

        tk.Label(form, text="Cantidad (unidades):", bg="white", font=("Verdana", 10, "bold")).grid(row=5, column=0, sticky="w", pady=8)
        self.entrada_sesiones = tk.Entry(form, font=("Verdana", 10))
        self.entrada_sesiones.grid(row=5, column=1, sticky="ew", pady=8)

        tk.Label(form, text="Fecha de registro:", bg="white", font=("Verdana", 10, "bold")).grid(row=6, column=0, sticky="w", pady=8)
        self.entrada_fecha = tk.Entry(form, state="readonly", readonlybackground="#E8E8E8", font=("Verdana", 10))
        self.entrada_fecha.grid(row=6, column=1, sticky="ew", pady=8)
        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")
        self.entrada_fecha.config(state="normal")
        self.entrada_fecha.insert(0, fecha_actual)
        self.entrada_fecha.config(state="readonly")

        tk.Label(form, text="* Todos los campos son obligatorios", bg="white", fg="gray",
                 font=("Verdana", 9, "italic")).grid(row=7, column=0, columnspan=2, pady=10)

        botones = tk.Frame(self.ventana, bg=self.color_fondo)
        botones.pack(fill="x", padx=25, pady=10)
        tk.Button(botones, text="Guardar Registro", command=self.guardar_registro,
                  bg=self.color_principal, fg="white", font=("Verdana", 10, "bold"),
                  relief="flat", padx=10, pady=8).pack(side="left", expand=True, padx=5)
        tk.Button(botones, text="Calcular / Reporte", command=self.mostrar_reporte,
                  bg=self.color_secundario, fg="white", font=("Verdana", 10, "bold"),
                  relief="flat", padx=10, pady=8).pack(side="left", expand=True, padx=5)
        tk.Button(botones, text="Salir", command=self.salir,
                  bg=self.color_salir, fg="white", font=("Verdana", 10, "bold"),
                  relief="flat", padx=10, pady=8).pack(side="left", expand=True, padx=5)

        self.actualizar_costo()

    def actualizar_costo(self, evento=None):
        costo = PRECIOS.get(self.menu.get(), 0)
        self.entrada_costo.config(state="normal")
        self.entrada_costo.delete(0, tk.END)
        self.entrada_costo.insert(0, formatear_moneda(costo))
        self.entrada_costo.config(state="readonly")

    def validar_datos(self):
        identificacion = self.entrada_id.get().strip()
        nombre = self.entrada_nombre.get().strip()
        sesiones_texto = self.entrada_sesiones.get().strip()

        if not identificacion.isdigit():
            messagebox.showwarning("Dato inválido", "La identificación debe ser numérica")
            self.entrada_id.focus()
            return None

        if len(nombre.split()) < 2:
            messagebox.showwarning("Dato inválido", "Escriba nombre y apellido")
            self.entrada_nombre.focus()
            return None

        try:
            sesiones = int(sesiones_texto)
            if sesiones <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Dato inválido", "La cantidad (unidades) debe ser un entero mayor que cero")
            self.entrada_sesiones.focus()
            return None

        tipo_menu = self.menu.get()
        costo_sesion = PRECIOS[tipo_menu]
        fecha = self.entrada_fecha.get()

        return GestionClientes(identificacion, nombre, self.genero.get(), tipo_menu,
                                sesiones, costo_sesion, fecha)

    def guardar_registro(self):
        cliente = self.validar_datos()
        if cliente is not None:
            self.cliente_guardado = cliente
            messagebox.showinfo("Registro guardado", "Los datos del cliente se guardaron correctamente")

    def mostrar_reporte(self):
        cliente = self.validar_datos()
        if cliente is None:
            return

        ventana_reporte = tk.Toplevel(self.ventana)
        ventana_reporte.title("Sabor & Sazón - Reporte")
        ventana_reporte.geometry("500x560")
        ventana_reporte.resizable(False, False)
        ventana_reporte.configure(bg=self.color_fondo)

        marco_titulo = tk.Frame(ventana_reporte, bg=self.color_principal, height=80)
        marco_titulo.pack(fill="x")
        marco_titulo.pack_propagate(False)
        tk.Label(marco_titulo, text="REPORTE - SABOR & SAZÓN", bg=self.color_principal,
                 fg="white", font=("Verdana", 15, "bold")).pack(pady=25)

        cuerpo = tk.Frame(ventana_reporte, bg="white", padx=20, pady=15)
        cuerpo.pack(padx=20, pady=15, fill="both", expand=True)

        datos = [
            ("Identificación", cliente.identificacion),
            ("Nombre completo", cliente.nombre),
            ("Género", cliente.genero),
            ("Tipo de menú", cliente.tipo_menu),
            ("Unidades tomadas", str(cliente.numero_sesiones)),
            ("Costo por unidad", formatear_moneda(cliente.costo_sesion)),
            ("Fecha de registro", cliente.fecha_registro),
        ]
        for fila, (etiqueta, valor) in enumerate(datos):
            tk.Label(cuerpo, text=etiqueta + ":", bg="white", font=("Verdana", 10, "bold")).grid(row=fila, column=0, sticky="w", pady=6)
            tk.Label(cuerpo, text=valor, bg="white", font=("Verdana", 10)).grid(row=fila, column=1, sticky="w", padx=15, pady=6)

        total = cliente.calcular_costo_total(cliente.numero_sesiones, cliente.costo_sesion)

        tk.Frame(cuerpo, bg="#DDDDDD", height=2).grid(row=7, column=0, columnspan=2, sticky="ew", pady=10)
        tk.Label(cuerpo, text="COSTO TOTAL:", bg="#F2E9D8", fg=self.color_principal,
                 font=("Verdana", 12, "bold"), padx=6, pady=8).grid(row=8, column=0, sticky="w")
        tk.Label(cuerpo, text=formatear_moneda(total), bg="#F2E9D8", fg=self.color_principal,
                 font=("Verdana", 13, "bold"), padx=6, pady=8).grid(row=8, column=1, sticky="w")
        tk.Label(cuerpo, text=f"{cliente.numero_sesiones} unidades x {formatear_moneda(cliente.costo_sesion)}",
             bg="white", fg="gray", font=("Verdana", 9, "italic")).grid(row=9, column=0, columnspan=2, pady=10)

        tk.Button(ventana_reporte, text="Cerrar reporte", command=ventana_reporte.destroy,
                  bg=self.color_salir, fg="white", font=("Verdana", 10, "bold"),
                  relief="flat", padx=15, pady=6).pack(pady=15)

    def salir(self):
        if messagebox.askyesno("Confirmar salida", "¿Desea salir de la aplicación?"):
            self.ventana.destroy()


if __name__ == "__main__":
    ventana = tk.Tk()
    app = Aplicacion(ventana)
    ventana.mainloop()
    