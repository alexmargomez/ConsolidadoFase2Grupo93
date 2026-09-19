import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class GestionClientes:
    def __init__(
        self,
        identificacion,
        nombre,
        genero,
        tipo_menu,
        sesiones,
        costo_sesion,
        fecha_registro
    ):
        self.identificacion = identificacion
        self.nombre = nombre
        self.genero = genero
        self.tipo_menu = tipo_menu
        self.sesiones = sesiones
        self.costo_sesion = costo_sesion
        self.fecha_registro = fecha_registro

    def calcular_costo_total(self):
        return self.sesiones * self.costo_sesion

class Aplicacion:
    def __init__(self, ventana_principal):
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Sabor & Sazón - Acceso")
        self.ventana_principal.geometry("500x550")
        self.ventana_principal.update_idletasks()
        w, h = 500, 550
        x = (self.ventana_principal.winfo_screenwidth() // 2) - (w // 2)
        y = (self.ventana_principal.winfo_screenheight() // 2) - (h // 2)
        self.ventana_principal.geometry(f"{w}x{h}+{x}+{y}")
        self.ventana_principal.resizable(False, False)
        self.ventana_principal.configure(bg="#F1F8F4")

        self.cliente = None
        self.colores = {
            "verde": "#155D43",
            "verde_claro": "#DDF3E4",
            "azul": "#1E3A5F",
            "fondo": "#F1F8F4",
            "rojo": "#A52A2A"
        }

        self.mostrar_acceso()

    def limpiar_ventana(self):
        for componente in self.ventana_principal.winfo_children():
            componente.destroy()

    def crear_encabezado(self, titulo, subtitulo):
        encabezado = tk.Frame(
            self.ventana_principal,
            bg=self.colores["verde"],
            height=110
        )
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            text="🍽  SABOR & SAZÓN",
            font=("Century Gothic", 22, "bold"),
            fg="white",
            bg=self.colores["verde"]
        ).pack(pady=(18, 3))

        tk.Label(
            encabezado,
            text=titulo,
            font=("Century Gothic", 14, "bold"),
            fg="white",
            bg=self.colores["verde"]
        ).pack()

        tk.Label(
            self.ventana_principal,
            text=subtitulo,
            font=("Century Gothic", 12),
            fg="#4D4D4D",
            bg=self.colores["fondo"]
        ).pack(pady=12)

    def mostrar_acceso(self):
        self.limpiar_ventana()

        self.ventana_principal.title("Sabor & Sazón - Acceso")
        self.crear_encabezado(
            "Sistema de Gestión de Clientes",
            "Ingeniería de Sistemas - UNAD"
        )

        marco = tk.Frame(
            self.ventana_principal,
            bg="white",
            padx=28,
            pady=22
        )
        marco.pack(padx=35, pady=5, fill="both", expand=True)

        tk.Label(
            marco,
            text="Autor de la aplicación:",
            font=("Century Gothic", 12, "bold"),
            bg="white",
            fg="#333333"
        ).pack(pady=(0, 3))

        tk.Label(
            marco,
            text="Sandra Yamile Ortega Blanco",
            font=("Century Gothic", 16),
            bg="white",
            fg=self.colores["verde"]
        ).pack(pady=(0, 20))

        tk.Label(
            marco,
            text="Ingrese la contraseña:",
            font=("Century Gothic", 12, "bold"),
            bg="white"
        ).pack(anchor="w")

        self.campo_contrasena = tk.Entry(
            marco,
            show="*",
            font=("Century Gothic", 14),
            justify="center",
            width=25
        )
        self.campo_contrasena.pack(pady=8)
        self.campo_contrasena.focus()

        self.campo_contrasena.bind(
            "<Return>",
            lambda evento: self.validar_acceso()
        )

        tk.Label(
            marco,
            text="La contraseña se encuentra enmascarada.",
            font=("Century Gothic", 12),
            fg="#777777",
            bg="white"
        ).pack(pady=(0, 18))

        tk.Button(
            marco,
            text="Ingresar al Sistema",
            command=self.validar_acceso,
            bg=self.colores["verde"],
            fg="white",
            font=("Century Gothic", 14, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8
        ).pack()

    def validar_acceso(self):
        contrasena = self.campo_contrasena.get()

        if contrasena == "1793":
            self.mostrar_formulario()
        else:
            messagebox.showerror(
                "Acceso denegado",
                "La contraseña ingresada no es correcta."
            )
            self.campo_contrasena.delete(0, tk.END)
            self.campo_contrasena.focus()

    def mostrar_formulario(self):
        self.limpiar_ventana()

        self.ventana_principal.title("Sabor & Sazón - Registro de Cliente")
        self.ventana_principal.geometry("650x650")
        self.ventana_principal.update_idletasks()
        w, h = 650, 650
        x = (self.ventana_principal.winfo_screenwidth() // 2) - (w // 2)
        y = (self.ventana_principal.winfo_screenheight() // 2) - (h // 2)
        self.ventana_principal.geometry(f"{w}x{h}+{x}+{y}")

        self.crear_encabezado(
            "Registro de Cliente",
            "Complete los datos solicitados"
        )

        formulario = tk.Frame(
            self.ventana_principal,
            bg="white",
            padx=25,
            pady=18
        )
        formulario.pack(padx=25, pady=5, fill="both", expand=True)

        formulario.columnconfigure(1, weight=1)

        self.campo_identificacion = self.crear_campo(
            formulario,
            "Identificación:",
            0
        )

        self.campo_nombre = self.crear_campo(
            formulario,
            "Nombre Completo:",
            1
        )

        tk.Label(
            formulario,
            text="Género:",
            font=("Century Gothic", 12, "bold"),
            bg="white"
        ).grid(row=2, column=0, sticky="w", pady=10)

        self.genero = tk.StringVar(value="Masculino")

        marco_genero = tk.Frame(formulario, bg="white")
        marco_genero.grid(row=2, column=1, sticky="w", pady=10)

        tk.Radiobutton(
            marco_genero,
            text="Masculino",
            variable=self.genero,
            value="Masculino",
            bg="white",
            activebackground="white"
        ).pack(side="left", padx=(0, 20))

        tk.Radiobutton(
            marco_genero,
            text="Femenino",
            variable=self.genero,
            value="Femenino",
            bg="white",
            activebackground="white"
        ).pack(side="left")

        tk.Label(
            formulario,
            text="Tipo de Menú:",
            font=("Century Gothic", 12, "bold"),
            bg="white"
        ).grid(row=3, column=0, sticky="w", pady=10)

        self.tipo_menu = tk.StringVar()
        menus = [
            "Menú Ejecutivo",
            "Menú Vegetariano",
            "Menú Degustación",
            "Menú Infantil",
            "Menú Gourmet"
        ]

        self.lista_menu = ttk.Combobox(
            formulario,
            textvariable=self.tipo_menu,
            values=menus,
            state="readonly",
            width=35
        )
        self.lista_menu.grid(row=3, column=1, sticky="ew", pady=10)
        self.lista_menu.bind("<<ComboboxSelected>>", self.actualizar_costo)

        self.lista_menu.current(0)

        tk.Label(
            formulario,
            text="Costo por Sesión:",
            font=("Century Gothic", 12, "bold"),
            bg="white"
        ).grid(row=4, column=0, sticky="w", pady=10)

        self.campo_costo = tk.Entry(
            formulario,
            state="readonly",
            readonlybackground="#E8E8E8",
            width=38,
            font=("Century Gothic", 12)
        )
        self.campo_costo.grid(row=4, column=1, sticky="ew", pady=10)

        tk.Label(
            formulario,
            text="Número de Sesiones:",
            font=("Century Gothic", 12, "bold"),
            bg="white"
        ).grid(row=5, column=0, sticky="w", pady=10)

        self.campo_sesiones = tk.Entry(
            formulario,
            width=38,
            font=("Century Gothic", 12)
        )
        self.campo_sesiones.grid(row=5, column=1, sticky="ew", pady=10)

        tk.Label(
            formulario,
            text="Fecha de Registro:",
            font=("Century Gothic", 12, "bold"),
            bg="white"
        ).grid(row=6, column=0, sticky="w", pady=10)

        fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M")

        self.campo_fecha = tk.Entry(
            formulario,
            width=38,
            state="readonly",
            readonlybackground="#E8E8E8",
            font=("Century Gothic", 12)
        )
        self.campo_fecha.grid(row=6, column=1, sticky="ew", pady=10)

        self.campo_fecha.config(state="normal")
        self.campo_fecha.insert(0, fecha_actual)
        self.campo_fecha.config(state="readonly")

        tk.Label(
            formulario,
            text="* Todos los campos son obligatorios.",
            font=("Century Gothic", 12, "italic"),
            fg="#777777",
            bg="white"
        ).grid(row=7, column=0, columnspan=2, pady=(10, 20))

        botones = tk.Frame(
            self.ventana_principal,
            bg=self.colores["fondo"]
        )
        botones.pack(fill="x", padx=25, pady=15)

        tk.Button(
            botones,
            text="Guardar Registro",
            command=self.guardar_registro,
            bg=self.colores["verde"],
            fg="white",
            font=("Century Gothic", 12, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=8
        ).pack(side="left", expand=True, padx=5)

        tk.Button(
            botones,
            text="Calcular / Reporte",
            command=self.mostrar_reporte,
            bg=self.colores["azul"],
            fg="white",
            font=("Century Gothic", 12, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=8
        ).pack(side="left", expand=True, padx=5)

        tk.Button(
            botones,
            text="Salir",
            command=self.salir_aplicacion,
            bg=self.colores["rojo"],
            fg="white",
            font=("Century Gothic", 12, "bold"),
            relief="flat",
            cursor="hand2",
            padx=12,
            pady=8
        ).pack(side="left", expand=True, padx=5)

        self.actualizar_costo()

    def crear_campo(self, contenedor, texto, fila):
        tk.Label(
            contenedor,
            text=texto,
            font=("Century Gothic", 12, "bold"),
            bg="white"
        ).grid(row=fila, column=0, sticky="w", pady=10)

        campo = tk.Entry(
            contenedor,
            width=38,
            font=("Century Gothic", 12)
        )
        campo.grid(row=fila, column=1, sticky="ew", pady=10)

        return campo

    def obtener_precios(self):
        return {
            "Menú Ejecutivo": 35000,
            "Menú Vegetariano": 28000,
            "Menú Degustación": 75000,
            "Menú Infantil": 20000,
            "Menú Gourmet": 95000
        }

    def actualizar_costo(self, evento=None):
        precios = self.obtener_precios()
        menu_seleccionado = self.tipo_menu.get()
        costo = precios.get(menu_seleccionado, 0)

        self.campo_costo.config(state="normal")
        self.campo_costo.delete(0, tk.END)
        self.campo_costo.insert(0, self.formatear_moneda(costo))
        self.campo_costo.config(state="readonly")

    def formatear_moneda(self, valor):
        return f"$ {valor:,.0f}".replace(",", ".")

    def validar_datos(self):
        identificacion = self.campo_identificacion.get().strip()
        nombre = self.campo_nombre.get().strip()
        sesiones_texto = self.campo_sesiones.get().strip()

        if not identificacion:
            messagebox.showwarning(
                "Dato Requerido",
                "Ingrese la Identificación del Cliente."
            )
            self.campo_identificacion.focus()
            return None

        if not nombre:
            messagebox.showwarning(
                "Dato Requerido",
                "Ingrese el Nombre Completo del Cliente."
            )
            self.campo_nombre.focus()
            return None

        if not sesiones_texto:
            messagebox.showwarning(
                "Dato Requerido",
                "Ingrese el Número de Sesiones."
            )
            self.campo_sesiones.focus()
            return None

        try:
            sesiones = int(sesiones_texto)

            if sesiones <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Dato Inválido",
                "El Número de Sesiones debe ser un entero mayor que cero."
            )
            self.campo_sesiones.focus()
            return None

        precios = self.obtener_precios()
        menu_seleccionado = self.tipo_menu.get()
        costo_sesion = precios[menu_seleccionado]

        fecha = self.campo_fecha.get()

        return GestionClientes(
            identificacion=identificacion,
            nombre=nombre,
            genero=self.genero.get(),
            tipo_menu=menu_seleccionado,
            sesiones=sesiones,
            costo_sesion=costo_sesion,
            fecha_registro=fecha
        )

    def guardar_registro(self):
        cliente = self.validar_datos()

        if cliente is not None:
            self.cliente = cliente

            messagebox.showinfo(
                "Registro Guardado",
                "La información del cliente fue guardada correctamente."
            )

    def mostrar_reporte(self):
        cliente = self.validar_datos()

        if cliente is None:
            return

        self.cliente = cliente

        reporte = tk.Toplevel(self.ventana_principal)
        reporte.title("Sabor & Sazón - Reporte")
        reporte.geometry("560x570")
        reporte.update_idletasks()
        w, h = 560, 570
        x = (reporte.winfo_screenwidth() // 2) - (w // 2)
        y = (reporte.winfo_screenheight() // 2) - (h // 2)
        reporte.geometry(f"{w}x{h}+{x}+{y}")
        reporte.resizable(False, False)
        reporte.configure(bg=self.colores["fondo"])

        encabezado = tk.Frame(
            reporte,
            bg=self.colores["verde"],
            height=90
        )
        encabezado.pack(fill="x")
        encabezado.pack_propagate(False)

        tk.Label(
            encabezado,
            text="REPORTE - SABOR & SAZÓN",
            font=("Century Gothic", 20, "bold"),
            fg="white",
            bg=self.colores["verde"]
        ).pack(pady=28)

        contenido = tk.Frame(
            reporte,
            bg="white",
            padx=25,
            pady=20
        )
        contenido.pack(padx=25, pady=20, fill="both", expand=True)

        datos = [
            ("Identificación", cliente.identificacion),
            ("Nombre Completo", cliente.nombre),
            ("Género", cliente.genero),
            ("Tipo de Menú", cliente.tipo_menu),
            ("Sesiones Tomadas", str(cliente.sesiones)),
            ("Costo por Sesión", self.formatear_moneda(cliente.costo_sesion)),
            ("Fecha de Registro", cliente.fecha_registro)
        ]

        for fila, (etiqueta, valor) in enumerate(datos):
            tk.Label(
                contenido,
                text=f"{etiqueta}:",
                font=("Century Gothic", 12, "bold"),
                bg="white",
                anchor="w"
            ).grid(row=fila, column=0, sticky="w", pady=7)

            tk.Label(
                contenido,
                text=valor,
                font=("Century Gothic", 12),
                bg="white",
                anchor="w"
            ).grid(row=fila, column=1, sticky="w", padx=20, pady=7)

        costo_total = cliente.calcular_costo_total()

        tk.Frame(
            contenido,
            height=2,
            bg="#DDDDDD"
        ).grid(row=7, column=0, columnspan=2, sticky="ew", pady=12)

        tk.Label(
            contenido,
            text="COSTO TOTAL DEL SERVICIO:",
            font=("Century Gothic", 14, "bold"),
            bg=self.colores["verde_claro"],
            fg=self.colores["verde"],
            padx=8,
            pady=10
        ).grid(row=8, column=0, sticky="w")

        tk.Label(
            contenido,
            text=self.formatear_moneda(costo_total),
            font=("Century Gothic", 16, "bold"),
            bg=self.colores["verde_claro"],
            fg=self.colores["verde"],
            padx=8,
            pady=10
        ).grid(row=8, column=1, sticky="w")

        tk.Label(
            contenido,
            text=(
                f"Fórmula aplicada: {cliente.sesiones} sesiones "
                f"x {self.formatear_moneda(cliente.costo_sesion)}"
            ),
            font=("Century Gothic", 12, "italic"),
            fg="#666666",
            bg="white"
        ).grid(row=9, column=0, columnspan=2, pady=15)

        tk.Button(
            reporte,
            text="Cerrar Reporte",
            command=reporte.destroy,
            bg=self.colores["rojo"],
            fg="white",
            font=("Century Gothic", 12, "bold"),
            relief="flat",
            cursor="hand2",
            padx=20,
            pady=8
        ).pack(pady=(0, 20))

    def salir_aplicacion(self):
        respuesta = messagebox.askyesno(
            "Confirmar Salida",
            "¿Está seguro de que desea salir de la aplicación?"
        )

        if respuesta:
            self.ventana_principal.destroy()

if __name__ == "__main__":
    ventana = tk.Tk()
    aplicacion = Aplicacion(ventana)
    ventana.mainloop()
