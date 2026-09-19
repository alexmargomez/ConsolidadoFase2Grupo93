import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class GestionClientes:
    def __init__(self):
        self.identificacion = ""
        self.nombre_completo = ""
        self.genero = ""
        self.tipo_menu = ""
        self.costo_sesion = 0.0
        self.num_sesiones = 0
        self.fecha_registro = ""

    def calcular_costo_total(self, num_sesiones: int, costo_sesion: float) -> float:
        return num_sesiones * costo_sesion

class SaborSazonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sabor & Sazón - Acceso")
        self.root.update_idletasks()
        w, h = 400, 300
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f"{w}x{h}+{x}+{y}")
        self.root.configure(bg="#F4F6F7")
        self.root.resizable(False, False)

        # Colores
        self.c_primary = "#0B3C26"
        self.c_accent = "#D4AC0D"
        self.c_bg = "#F4F6F7"
        self.c_card = "#FFFFFF"
        self.c_text = "#1C2833"
        self.c_btn_report = "#1B4F72"
        self.c_btn_exit = "#C0392B"

        self.cliente = GestionClientes()
        
        self.crear_pantalla_login()

    def crear_pantalla_login(self):
        # Frame principal
        self.frame_login = tk.Frame(self.root, bg=self.c_bg)
        self.frame_login.pack(fill="both", expand=True)

        # Header
        header = tk.Frame(self.frame_login, bg=self.c_primary, height=80)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(header, text="🍽️ Restaurante Sabor & Sazón", font=("Segoe UI", 14, "bold"), bg=self.c_primary, fg="#FFFFFF").pack(pady=5)
        tk.Label(header, text="Autor: Fabio Alexmar Gomez Sanmiguel", font=("Segoe UI", 9, "italic"), bg=self.c_primary, fg=self.c_accent).pack()
        tk.Label(header, text="Programa: Ingeniería de Sistemas / Estructura de Datos", font=("Segoe UI", 9, "italic"), bg=self.c_primary, fg=self.c_accent).pack()

        # Body
        body = tk.Frame(self.frame_login, bg=self.c_bg)
        body.pack(pady=30)

        tk.Label(body, text="🔒 Clave de Acceso:", font=("Segoe UI", 10, "bold"), bg=self.c_bg, fg=self.c_text).pack(pady=5)
        self.ent_clave = tk.Entry(body, font=("Segoe UI", 10), show="*", justify="center")
        self.ent_clave.pack(pady=5)

        tk.Button(body, text="Ingresar 🚪", font=("Segoe UI", 10, "bold"), bg=self.c_primary, fg="#FFFFFF",
                  activebackground=self.c_accent, cursor="hand2", relief="flat", command=self.validar_login).pack(pady=15, ipadx=10)

    def validar_login(self):
        clave = self.ent_clave.get()
        if clave == "1793":
            self.root.destroy()
            self.abrir_registro()
        else:
            messagebox.showerror("Error", "Clave incorrecta. Intente de nuevo.")
            self.ent_clave.delete(0, tk.END)

    def abrir_registro(self):
        self.reg_window = tk.Tk()
        self.reg_window.title("Sabor & Sazón - Registro de Cliente")
        self.reg_window.update_idletasks()
        w, h = 500, 550
        x = (self.reg_window.winfo_screenwidth() // 2) - (w // 2)
        y = (self.reg_window.winfo_screenheight() // 2) - (h // 2)
        self.reg_window.geometry(f"{w}x{h}+{x}+{y}")
        self.reg_window.configure(bg=self.c_bg)
        self.reg_window.resizable(False, False)

        # Header
        header = tk.Frame(self.reg_window, bg=self.c_primary, height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        tk.Label(header, text="🍽️ Registro de Servicio", font=("Segoe UI", 14, "bold"), bg=self.c_primary, fg="#FFFFFF").pack(pady=15)

        # Card de formulario
        card = tk.Frame(self.reg_window, bg=self.c_card, highlightbackground="#E0E0E0", highlightthickness=1)
        card.pack(fill="both", expand=True, padx=20, pady=20)

        # Form elements
        font_lbl = ("Segoe UI", 9, "bold")
        font_ent = ("Segoe UI", 9)

        # Identificación
        tk.Label(card, text="👤 Identificación:", font=font_lbl, bg=self.c_card, fg=self.c_text).grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.ent_id = tk.Entry(card, font=font_ent)
        self.ent_id.grid(row=0, column=1, sticky="w", padx=10)

        # Nombre
        tk.Label(card, text="👤 Nombre Completo:", font=font_lbl, bg=self.c_card, fg=self.c_text).grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.ent_nombre = tk.Entry(card, font=font_ent, width=30)
        self.ent_nombre.grid(row=1, column=1, sticky="w", padx=10)

        # Género
        tk.Label(card, text="🚻 Género:", font=font_lbl, bg=self.c_card, fg=self.c_text).grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.var_genero = tk.StringVar(value="Masculino")
        frame_gen = tk.Frame(card, bg=self.c_card)
        frame_gen.grid(row=2, column=1, sticky="w", padx=10)
        tk.Radiobutton(frame_gen, text="Masculino", variable=self.var_genero, value="Masculino", font=font_ent, bg=self.c_card).pack(side="left")
        tk.Radiobutton(frame_gen, text="Femenino", variable=self.var_genero, value="Femenino", font=font_ent, bg=self.c_card).pack(side="left")

        # Tipo de Menú
        tk.Label(card, text="🍽️ Tipo de Menú:", font=font_lbl, bg=self.c_card, fg=self.c_text).grid(row=3, column=0, sticky="e", padx=10, pady=10)
        self.combo_menu = ttk.Combobox(card, font=font_ent, state="readonly", width=25)
        self.combo_menu['values'] = ("Menú ejecutivo", "Menú vegetariano", "Menú degustación", "Menú infantil", "Menú gourmet")
        self.combo_menu.grid(row=3, column=1, sticky="w", padx=10)
        self.combo_menu.bind("<<ComboboxSelected>>", self.actualizar_costo)

        # Costo por Sesión
        tk.Label(card, text="💳 Costo por Sesión ($):", font=font_lbl, bg=self.c_card, fg=self.c_text).grid(row=4, column=0, sticky="e", padx=10, pady=10)
        self.var_costo = tk.StringVar(value="0")
        self.ent_costo = tk.Entry(card, textvariable=self.var_costo, font=font_ent, state="disabled")
        self.ent_costo.grid(row=4, column=1, sticky="w", padx=10)

        # Número de sesiones
        tk.Label(card, text="📅 Número de sesiones:", font=font_lbl, bg=self.c_card, fg=self.c_text).grid(row=5, column=0, sticky="e", padx=10, pady=10)
        self.ent_sesiones = tk.Entry(card, font=font_ent)
        self.ent_sesiones.grid(row=5, column=1, sticky="w", padx=10)

        # Fecha Registro
        tk.Label(card, text="📅 Fecha de Registro:", font=font_lbl, bg=self.c_card, fg=self.c_text).grid(row=6, column=0, sticky="e", padx=10, pady=10)
        self.var_fecha = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.ent_fecha = tk.Entry(card, textvariable=self.var_fecha, font=font_ent, state="disabled", width=25)
        self.ent_fecha.grid(row=6, column=1, sticky="w", padx=10)

        # Botones de Acción
        frame_btns = tk.Frame(self.reg_window, bg=self.c_bg)
        frame_btns.pack(pady=10)

        tk.Button(frame_btns, text="💾 Guardar Registro", font=font_lbl, bg=self.c_primary, fg="#FFFFFF",
                  cursor="hand2", relief="flat", command=self.guardar_registro).pack(side="left", padx=5, ipadx=5, ipady=5)
        
        tk.Button(frame_btns, text="📊 Calcular / Reporte", font=font_lbl, bg=self.c_btn_report, fg="#FFFFFF",
                  cursor="hand2", relief="flat", command=self.mostrar_reporte).pack(side="left", padx=5, ipadx=5, ipady=5)

        tk.Button(frame_btns, text="🚪 Salir", font=font_lbl, bg=self.c_btn_exit, fg="#FFFFFF",
                  cursor="hand2", relief="flat", command=self.salir_app).pack(side="left", padx=5, ipadx=10, ipady=5)

        self.reg_window.protocol("WM_DELETE_WINDOW", self.salir_app)

    def actualizar_costo(self, event):
        precios = {
            "Menú ejecutivo": 35000,
            "Menú vegetariano": 28000,
            "Menú degustación": 75000,
            "Menú infantil": 20000,
            "Menú gourmet": 95000
        }
        menu = self.combo_menu.get()
        if menu in precios:
            self.var_costo.set(str(precios[menu]))

    def guardar_registro(self):
        try:
            self.cliente.identificacion = self.ent_id.get().strip()
            self.cliente.nombre_completo = self.ent_nombre.get().strip()
            self.cliente.genero = self.var_genero.get()
            self.cliente.tipo_menu = self.combo_menu.get()
            
            if not self.cliente.identificacion or not self.cliente.nombre_completo or not self.cliente.tipo_menu:
                raise ValueError("Por favor complete todos los campos obligatorios.")

            try:
                sesiones = int(self.ent_sesiones.get())
                if sesiones <= 0:
                    raise ValueError
                self.cliente.num_sesiones = sesiones
            except ValueError:
                raise ValueError("El número de sesiones debe ser un entero mayor a 0.")

            self.cliente.costo_sesion = float(self.var_costo.get())
            self.cliente.fecha_registro = self.var_fecha.get()
            
            messagebox.showinfo("Éxito", "Registro guardado correctamente.")
            return True
        except ValueError as ve:
            messagebox.showwarning("Error de Validación", str(ve))
            return False

    def mostrar_reporte(self):
        if self.guardar_registro():
            total = self.cliente.calcular_costo_total(self.cliente.num_sesiones, self.cliente.costo_sesion)
            
            top = tk.Toplevel(self.reg_window)
            top.title("Reporte de Servicio")
            top.update_idletasks()
            w, h = 350, 400
            x = (top.winfo_screenwidth() // 2) - (w // 2)
            y = (top.winfo_screenheight() // 2) - (h // 2)
            top.geometry(f"{w}x{h}+{x}+{y}")
            top.configure(bg=self.c_bg)
            top.resizable(False, False)
            top.grab_set() # Modal

            tk.Label(top, text="📊 Factura Detallada", font=("Segoe UI", 14, "bold"), bg=self.c_primary, fg="#FFFFFF").pack(fill="x", pady=(0,10), ipady=10)

            card = tk.Frame(top, bg=self.c_card, highlightbackground="#E0E0E0", highlightthickness=1)
            card.pack(fill="both", expand=True, padx=20, pady=10)

            font_res = ("Segoe UI", 10)
            
            tk.Label(card, text=f"👤 Cliente: {self.cliente.nombre_completo}", font=font_res, bg=self.c_card).pack(anchor="w", padx=10, pady=5)
            tk.Label(card, text=f"🆔 ID: {self.cliente.identificacion}", font=font_res, bg=self.c_card).pack(anchor="w", padx=10, pady=5)
            tk.Label(card, text=f"🍽️ Menú: {self.cliente.tipo_menu}", font=font_res, bg=self.c_card).pack(anchor="w", padx=10, pady=5)
            tk.Label(card, text=f"💳 Costo Unitario: ${self.cliente.costo_sesion:,.0f}", font=font_res, bg=self.c_card).pack(anchor="w", padx=10, pady=5)
            tk.Label(card, text=f"📅 Sesiones: {self.cliente.num_sesiones}", font=font_res, bg=self.c_card).pack(anchor="w", padx=10, pady=5)
            
            tk.Label(card, text="-"*30, font=font_res, bg=self.c_card).pack(pady=5)
            tk.Label(card, text=f"Fórmula: {self.cliente.num_sesiones} × ${self.cliente.costo_sesion:,.0f}", font=("Segoe UI", 9, "italic"), bg=self.c_card).pack(anchor="w", padx=10)
            tk.Label(card, text=f"💰 TOTAL: ${total:,.0f}", font=("Segoe UI", 12, "bold"), bg=self.c_card, fg=self.c_primary).pack(anchor="w", padx=10, pady=10)

            tk.Button(top, text="Cerrar", font=("Segoe UI", 10, "bold"), bg=self.c_primary, fg="#FFFFFF",
                      cursor="hand2", relief="flat", command=top.destroy).pack(pady=10, ipadx=20)

    def salir_app(self):
        if messagebox.askyesno("Confirmar", "¿Está seguro que desea salir de la aplicación?"):
            self.reg_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SaborSazonApp(root)
    root.mainloop()
