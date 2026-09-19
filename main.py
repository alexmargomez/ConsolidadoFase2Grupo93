import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
import os

class MenuConsolidador:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Consolidador - Fase 2 Grupo 93")
        self.root.geometry("600x650")
        try:
            self.root.eval('tk::PlaceWindow . center')
        except:
            pass
        self.root.configure(bg="#F4F6F7")
        self.root.resizable(False, False)

        # Estilos
        self.bg_color = "#F4F6F7"
        self.primary_color = "#0B3C26"
        self.accent_color = "#D4AC0D"
        self.text_color = "#1C2833"
        
        self.crear_interfaz()

    def crear_interfaz(self):
        # Header
        header_frame = tk.Frame(self.root, bg=self.primary_color, height=80)
        header_frame.pack(fill="x")
        header_frame.pack_propagate(False)

        lbl_title = tk.Label(header_frame, text="🍽️ Sistema Consolidador Grupo 93", 
                             font=("Segoe UI", 16, "bold"), bg=self.primary_color, fg="#FFFFFF")
        lbl_title.pack(pady=10)

        lbl_subtitle = tk.Label(header_frame, text="Estructura de Datos - UNAD", 
                                font=("Segoe UI", 10, "italic"), bg=self.primary_color, fg=self.accent_color)
        lbl_subtitle.pack()

        # Panel Central
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(fill="both", expand=True, padx=40, pady=20)

        lbl_instruccion = tk.Label(main_frame, text="Seleccione el proyecto del estudiante a ejecutar:", 
                                   font=("Segoe UI", 12), bg=self.bg_color, fg=self.text_color)
        lbl_instruccion.pack(pady=20)

        # Botones de estudiantes
        estudiantes = [
            ("Rafael Cubides Rangel", "projects/Rafael Cubides Rangel/app.py"),
            ("Fabio Alexmar Gomez Sanmiguel", "projects/Fabio Alexmar Gomez Sanmiguel/app.py"),
            ("Hary Giorgeth Gutierrez Ortiz", "projects/Hary Giorgeth Gutierrez Ortiz/app.py"),
            ("Sandra Yamile Ortega Blanco", "projects/Sandra Yamile Ortega Blanco/app.py"),
            ("Julio Angel Suarez Galindo", "projects/Julio Angel Suarez Galindo/app.py")
        ]

        for nombre, ruta in estudiantes:
            btn = tk.Button(main_frame, text=f"👤 {nombre}", font=("Segoe UI", 12, "bold"),
                            bg=self.primary_color, fg="#FFFFFF", activebackground=self.accent_color,
                            activeforeground=self.text_color, relief="flat", cursor="hand2",
                            command=lambda r=ruta, n=nombre: self.ejecutar_proyecto(n, r))
            btn.pack(fill="x", pady=10, ipady=12)

        # Botón Salir
        btn_salir = tk.Button(main_frame, text="🚪 Salir", font=("Segoe UI", 10, "bold"),
                              bg="#C0392B", fg="#FFFFFF", activebackground="#A93226",
                              activeforeground="#FFFFFF", relief="flat", cursor="hand2",
                              command=self.root.destroy)
        btn_salir.pack(side="bottom", pady=20, ipadx=20, ipady=5)

    def ejecutar_proyecto(self, nombre, ruta_relativa):
        ruta_script = os.path.join(os.path.dirname(__file__), ruta_relativa)
        
        if not os.path.exists(ruta_script):
            messagebox.showwarning("Aviso", 
                                   "El estudiante no ha compartido sus datos o no ha subido el proyecto aún.")
            return

        try:
            subprocess.Popen([sys.executable, ruta_script])
        except Exception as e:
            messagebox.showwarning("Error de Ejecución", f"No se pudo ejecutar el proyecto {nombre}.\nError: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuConsolidador(root)
    root.mainloop()
