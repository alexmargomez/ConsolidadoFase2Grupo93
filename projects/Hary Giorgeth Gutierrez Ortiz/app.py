import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime

# Clase para la gestion del cliente
class GestionClientes:
    def __init__(self):
        self.identificacion = ""
        self.nombre_completo = ""
        self.genero = ""
        self.tipo_menu = ""
        self.costo_sesion = 0.0
        self.num_sesiones = 0
        self.fecha_registro = ""

    # Metodo que calcula el costo total
    def calcular_costo_total(self, num_sesiones: int, costo_sesion: float) -> float:
        return float(num_sesiones) * float(costo_sesion)

# Variable global para guardar los datos instanciando la clase
cliente_actual = GestionClientes()

# Precios de los menus
PRECIOS_MENU = {
    "Menú ejecutivo": 35000,
    "Menú vegetariano": 28000,
    "Menú degustación": 75000,
    "Menú infantil": 20000,
    "Menú gourmet": 95000
}

# --- VENTANA DE REPORTE ---
def abrir_ventana_reporte(parent):
    total_pagar = cliente_actual.calcular_costo_total(cliente_actual.num_sesiones, cliente_actual.costo_sesion)

    ven_rep = tk.Toplevel(parent)
    ven_rep.title("Sabor & Sazón — Reporte")
    ven_rep.geometry("450x580")
    ven_rep.resizable(False, False)
    ven_rep.configure(bg="#F9F9F9")

    # Encabezado
    f_head = tk.Frame(ven_rep, bg="#800000", pady=14)
    f_head.pack(fill="x")
    tk.Label(f_head, text="📋  Reporte — Sabor & Sazón", font=("Segoe UI", 15, "bold"), fg="#F1C40F", bg="#800000").pack()

    # Contenedor principal
    f_content = tk.Frame(ven_rep, bg="#F9F9F9", padx=20, pady=15)
    f_content.pack(fill="both", expand=True)

    # Tarjeta de usuario
    f_card_user = tk.Frame(f_content, bg="white", highlightbackground="#E0E0E0", highlightthickness=1, padx=15, pady=12)
    f_card_user.pack(fill="x", pady=(0, 12))

    # Avatar sencillo de cliente
    lbl_avatar = tk.Label(f_card_user, text="👤", font=("Segoe UI", 18), fg="#800000", bg="#FFF2CC", width=3, height=1)
    lbl_avatar.pack(side="left", padx=(0, 15))

    f_user_info = tk.Frame(f_card_user, bg="white")
    f_user_info.pack(side="left", fill="x", expand=True)

    tk.Label(f_user_info, text=cliente_actual.nombre_completo, font=("Segoe UI", 12, "bold"), fg="#2C3E50", bg="white", anchor="w").pack(fill="x")
    tk.Label(f_user_info, text="ID: " + str(cliente_actual.identificacion) + "  |  " + str(cliente_actual.genero), font=("Segoe UI", 9), fg="#7F8C8D", bg="white", anchor="w").pack(fill="x", pady=(3, 0))

    # Detalles del servicio
    f_card_det = tk.Frame(f_content, bg="white", highlightbackground="#E0E0E0", highlightthickness=1, padx=15, pady=12)
    f_card_det.pack(fill="x")

    def crear_fila(padre, icono, titulo, valor):
        f_row = tk.Frame(padre, bg="white")
        f_row.pack(fill="x", pady=5)
        
        f_left = tk.Frame(f_row, bg="white")
        f_left.pack(side="left")
        tk.Label(f_left, text=icono, font=("Segoe UI", 10), bg="white").pack(side="left", padx=(0, 6))
        tk.Label(f_left, text=titulo, font=("Segoe UI", 9), fg="#555555", bg="white").pack(side="left")
        
        tk.Label(f_row, text=valor, font=("Segoe UI", 9, "bold"), fg="#2C3E50", bg="white").pack(side="right")

    # Formateo simple de pesos
    costo_str = "$ " + str(int(cliente_actual.costo_sesion))
    total_str = "$ " + str(int(total_pagar))

    crear_fila(f_card_det, "⚙️", "Tipo de menú", cliente_actual.tipo_menu)
    crear_fila(f_card_det, "📅", "Sesiones tomadas", str(cliente_actual.num_sesiones))
    crear_fila(f_card_det, "💳", "Costo por sesión", costo_str)
    crear_fila(f_card_det, "🕒", "Fecha de registro", cliente_actual.fecha_registro)

    tk.Frame(f_card_det, height=1, bg="#F0F0F0").pack(fill="x", pady=8)

    # Mostrar total
    r_total = tk.Frame(f_card_det, bg="#FFF2CC", padx=10, pady=8)
    r_total.pack(fill="x")
    tk.Label(r_total, text="💰 Costo total del servicio", font=("Segoe UI", 10, "bold"), fg="#800000", bg="#FFF2CC").pack(side="left")
    tk.Label(r_total, text=total_str, font=("Segoe UI", 13, "bold"), fg="#800000", bg="#FFF2CC").pack(side="right")

    # Texto con la formula
    formula_txt = "costoTotal = " + str(cliente_actual.num_sesiones) + " sesiones × " + costo_str
    tk.Label(f_card_det, text=formula_txt, font=("Segoe UI", 8, "italic"), fg="#7F8C8D", bg="white").pack(anchor="w", pady=(8, 0))

    # Botones
    f_bot = tk.Frame(f_content, bg="#F9F9F9")
    f_bot.pack(fill="x", pady=(15, 0))

    btn_imp = tk.Button(f_bot, text="🖨️ Imprimir", font=("Segoe UI", 9), bg="white", fg="#2C3E50", bd=1, relief="solid", cursor="hand2", command=lambda: messagebox.showinfo("Imprimir", "Enviando documento a la impresora..."))
    btn_imp.pack(side="left", expand=True, fill="x", padx=(0, 5), ipady=5)

    btn_cls = tk.Button(f_bot, text="❌ Cerrar reporte", font=("Segoe UI", 9, "bold"), bg="white", fg="#C0392B", bd=1, relief="solid", cursor="hand2", command=ven_rep.destroy)
    btn_cls.pack(side="right", expand=True, fill="x", padx=(5, 0), ipady=5)

# --- VENTANA DE REGISTRO ---
def abrir_ventana_registro():
    ven_reg = tk.Tk()
    ven_reg.title("Sabor & Sazón — Registro de Cliente")
    ven_reg.geometry("520x600")
    ven_reg.resizable(False, False)
    ven_reg.configure(bg="#F9F9F9")

    # Banner superior
    f_head = tk.Frame(ven_reg, bg="#800000", pady=12)
    f_head.pack(fill="x")
    
    f_logo_title = tk.Frame(f_head, bg="#800000")
    f_logo_title.pack()
    tk.Label(f_logo_title, text="🍽️", font=("Segoe UI", 16), bg="#800000").pack(side="left", padx=(0, 8))
    tk.Label(f_logo_title, text="Sabor & Sazón — Registro de Cliente", font=("Segoe UI", 14, "bold"), fg="#F1C40F", bg="#800000").pack(side="left")

    # Card del formulario
    f_card = tk.Frame(ven_reg, bg="white", highlightbackground="#E0E0E0", highlightthickness=1, padx=25, pady=20)
    f_card.pack(fill="both", expand=True, padx=20, pady=15)

    # Campo ID
    tk.Label(f_card, text="Identificación *", font=("Segoe UI", 9, "bold"), bg="white", fg="#333333").pack(anchor="w")
    entry_id = tk.Entry(f_card, font=("Segoe UI", 10), bd=1, relief="solid")
    entry_id.pack(fill="x", pady=(2, 10), ipady=3)

    # Campo Nombre
    tk.Label(f_card, text="Nombre completo *", font=("Segoe UI", 9, "bold"), bg="white", fg="#333333").pack(anchor="w")
    entry_nombre = tk.Entry(f_card, font=("Segoe UI", 10), bd=1, relief="solid")
    entry_nombre.pack(fill="x", pady=(2, 10), ipady=3)

    # Campo Genero
    tk.Label(f_card, text="Género *", font=("Segoe UI", 9, "bold"), bg="white", fg="#333333").pack(anchor="w")
    var_genero = tk.StringVar(value="Masculino")
    f_gen = tk.Frame(f_card, bg="white")
    f_gen.pack(anchor="w", pady=(2, 10))
    tk.Radiobutton(f_gen, text="Masculino", variable=var_genero, value="Masculino", bg="white").pack(side="left", padx=(0, 20))
    tk.Radiobutton(f_gen, text="Femenino", variable=var_genero, value="Femenino", bg="white").pack(side="left")

    # Campo Combo Menu
    tk.Label(f_card, text="Tipo de menú *", font=("Segoe UI", 9, "bold"), bg="white", fg="#333333").pack(anchor="w")
    cb_menu = ttk.Combobox(f_card, values=["Menú ejecutivo", "Menú vegetariano", "Menú degustación", "Menú infantil", "Menú gourmet"], state="readonly", font=("Segoe UI", 9))
    cb_menu.pack(fill="x", pady=(2, 10))

    # Campo Costo por sesion
    tk.Label(f_card, text="Costo por sesión", font=("Segoe UI", 9, "bold"), bg="white", fg="#333333").pack(anchor="w")
    entry_costo = tk.Entry(f_card, font=("Segoe UI", 10), bd=1, relief="solid", bg="#F2F2F2", state="disabled")
    entry_costo.pack(fill="x", pady=(2, 10), ipady=3)

    # Evento para cambiar costo al seleccionar del combobox
    def al_seleccionar_menu(event):
        menu_sel = cb_menu.get()
        precio = PRECIOS_MENU.get(menu_sel, 0)
        entry_costo.config(state="normal")
        entry_costo.delete(0, tk.END)
        entry_costo.insert(0, "$ " + str(precio))
        entry_costo.config(state="disabled")

    cb_menu.bind("<<ComboboxSelected>>", al_seleccionar_menu)

    # Campo Sesiones
    tk.Label(f_card, text="Número de sesiones *", font=("Segoe UI", 9, "bold"), bg="white", fg="#333333").pack(anchor="w")
    entry_sesiones = tk.Entry(f_card, font=("Segoe UI", 10), bd=1, relief="solid")
    entry_sesiones.pack(fill="x", pady=(2, 10), ipady=3)

    # Campo Fecha
    fecha_hoy = datetime.now().strftime("%d/%m/%Y %H:%M")
    tk.Label(f_card, text="Fecha de registro", font=("Segoe UI", 9, "bold"), bg="white", fg="#333333").pack(anchor="w")
    entry_fecha = tk.Entry(f_card, font=("Segoe UI", 10), bd=1, relief="solid", bg="#F2F2F2")
    entry_fecha.insert(0, fecha_hoy)
    entry_fecha.config(state="disabled")
    entry_fecha.pack(fill="x", pady=(2, 5), ipady=3)

    tk.Label(f_card, text="* Campos obligatorios", font=("Segoe UI", 8, "italic"), fg="#888888", bg="white").pack(anchor="w")

    # Validacion de los datos
    def guardar_datos():
        if entry_id.get().strip() == "" or entry_nombre.get().strip() == "" or cb_menu.get() == "" or entry_sesiones.get().strip() == "":
            messagebox.showwarning("Atención", "Por favor diligencie todos los campos obligatorios.")
            return False
        
        try:
            sesiones = int(entry_sesiones.get().strip())
            if sesiones <= 0:
                messagebox.showerror("Error", "El número de sesiones tomadas debe ser mayor a 0.")
                return False
        except ValueError:
            messagebox.showerror("Error", "El número de sesiones debe ser un número entero.")
            return False

        # Guardar en la clase
        cliente_actual.identificacion = entry_id.get().strip()
        cliente_actual.nombre_completo = entry_nombre.get().strip()
        cliente_actual.genero = var_genero.get()
        cliente_actual.tipo_menu = cb_menu.get()
        cliente_actual.costo_sesion = PRECIOS_MENU[cb_menu.get()]
        cliente_actual.num_sesiones = sesiones
        cliente_actual.fecha_registro = fecha_hoy
        return True

    def btn_guardar_click():
        if guardar_datos():
            messagebox.showinfo("Éxito", "¡Datos registrados correctamente!")

    def btn_reporte_click():
        if guardar_datos():
            abrir_ventana_reporte(ven_reg)

    def btn_salir_click():
        if messagebox.askyesno("Confirmar Salida", "¿Realmente desea salir de la aplicación?"):
            ven_reg.destroy()

    # Botones de la ventana
    f_botones = tk.Frame(ven_reg, bg="#F9F9F9")
    f_botones.pack(fill="x", padx=20, pady=(0, 15))

    tk.Button(f_botones, text="💾 Guardar Registro", bg="#800000", fg="#F1C40F", font=("Segoe UI", 9, "bold"), bd=0, cursor="hand2", command=btn_guardar_click).pack(side="left", expand=True, fill="x", padx=2, ipady=7)
    tk.Button(f_botones, text="📊 Calcular / Reporte", bg="#1A365D", fg="white", font=("Segoe UI", 9, "bold"), bd=0, cursor="hand2", command=btn_reporte_click).pack(side="left", expand=True, fill="x", padx=2, ipady=7)
    tk.Button(f_botones, text="🚪 Salir", bg="white", fg="#C0392B", font=("Segoe UI", 9, "bold"), bd=1, relief="solid", cursor="hand2", command=btn_salir_click).pack(side="left", expand=True, fill="x", padx=2, ipady=7)

    ven_reg.mainloop()

# --- VENTANA DE LOGIN ---
def validar_acceso():
    if entry_password.get() == "1793":
        ventana_login.destroy()
        abrir_ventana_registro()
    else:
        messagebox.showerror("Error", "Contraseña incorrecta. Intente nuevamente.")

ventana_login = tk.Tk()
ventana_login.title("Sabor & Sazón — Acceso")
ventana_login.geometry("440x490")
ventana_login.resizable(False, False)
ventana_login.configure(bg="#F9F9F9")

# Header del Login
frame_header = tk.Frame(ventana_login, bg="#800000", pady=16)
frame_header.pack(fill="x")

frame_title_box = tk.Frame(frame_header, bg="#800000")
frame_title_box.pack()

tk.Label(frame_title_box, text="🍽️", font=("Segoe UI", 22), bg="#800000").pack(side="left", padx=(0, 10))
tk.Label(frame_title_box, text="Sabor & Sazón", font=("Segoe UI", 22, "bold"), fg="#F1C40F", bg="#800000").pack(side="left")
tk.Label(frame_header, text="Gestión de Clientes", font=("Segoe UI", 10, "italic"), fg="#FFFFFF", bg="#800000").pack(pady=(4, 0))

# Seccion del estudiante
frame_autor = tk.Frame(ventana_login, bg="#FFF2CC", pady=10)
frame_autor.pack(fill="x")

tk.Label(frame_autor, text="Hary Giorgeth Gutierrez Ortiz", font=("Segoe UI", 11, "bold"), fg="#800000", bg="#FFF2CC").pack()
tk.Label(frame_autor, text="Ingeniería de Sistemas — UNAD", font=("Segoe UI", 9, "bold"), fg="#4A235A", bg="#FFF2CC").pack(pady=(2, 0))

# Formulario
frame_form = tk.Frame(ventana_login, bg="#F9F9F9", padx=35, pady=20)
frame_form.pack(fill="both", expand=True)

tk.Label(frame_form, text="Ingrese la contraseña para continuar", font=("Segoe UI", 10, "bold"), fg="#333333", bg="#F9F9F9").pack(pady=(10, 8))

f_input = tk.Frame(frame_form, bg="white", highlightbackground="#CCCCCC", highlightthickness=1)
f_input.pack(fill="x")

tk.Label(f_input, text="🔒", font=("Segoe UI", 11), bg="white").pack(side="left", padx=8)
entry_password = tk.Entry(f_input, show="*", font=("Consolas", 12), bd=0, bg="white")
entry_password.pack(side="left", fill="x", expand=True, ipady=6)

tk.Label(frame_form, text="La contraseña está enmascarada (***)", font=("Segoe UI", 8), fg="#7F8C8D", bg="#F9F9F9").pack(pady=(6, 18))

btn_ingresar = tk.Button(frame_form, text="Ingresar al sistema →", font=("Segoe UI", 10, "bold"), bg="#800000", fg="#F1C40F", activebackground="#600000", activeforeground="#F1C40F", cursor="hand2", bd=0, command=validar_acceso)
btn_ingresar.pack(fill="x", ipady=9)

# Pie de pagina
tk.Label(ventana_login, text="Estructura de Datos · Cód. 301305 · ECBTI", font=("Segoe UI", 8, "bold"), fg="#A6ACAF", bg="#F9F9F9").pack(side="bottom", pady=12)

ventana_login.mainloop()