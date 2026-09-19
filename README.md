# 🍽️ Consolidado Fase 2 — Estructura de Datos (Curso 301305)
**Universidad Nacional Abierta y a Distancia (UNAD)**  
**Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)**

---

## 📌 Información General
* **Fase:** Fase 2 — Fundamentos de Abstracción y Modelado de Datos
* **Grupo:** Grupo 93
* **Entorno de Desarrollo:** Python 3.10+ / Visual Studio Code (GUI Tkinter)
* **Rol Compilador:** Integrador de solución grupal

---

## 🚀 Arquitectura del Proyecto

El sistema está organizado bajo un modelo centralizado de menú consolidador que ejecuta los proyectos de software individuales desarrollados por cada integrante:

```text
ConsolidadoFase2Grupo93/
├── main.py                           # Menú principal interactivo de la solución consolidada
├── README.md                         # Documentación del repositorio
├── Tablas_Abstraccion_Consolidadas.pdf # PDF de abstracciones del grupo
└── projects/                         # Módulos individuales
    ├── Rafael Cubides Rangel/
    │   └── app.py
    ├── Fabio Alexmar Gomez Sanmiguel/
    │   └── app.py                    # Sabor & Sazón
    ├── Hary Giorgeth Gutierrez Ortiz/
    │   └── app.py
    ├── Sandra Yamile Ortega Blanco/
    │   └── app.py
    └── Julio Angel Suarez Galindo/
        └── app.py
```

---

## ⚙️ Funcionalidades del Sistema

### 1. Menú Consolidador (`main.py`)

* Interfaz gráfica unificada con los nombres de todos los participantes.
* Lanzamiento independiente de subprocesos Python para ejecutar la app de cada estudiante.
* Tolerancia a fallos para aislar errores de ejecución de proyectos individuales.

### 2. Aplicación Individual "Sabor & Sazón" (`app.py`)

* **Módulo de Autenticación:** Clave genérica `1793` enmascarada.
* **Módulo de Registro:** Captura de identificación, nombre, género, tipo de menú y sesiones.
* **Asignación Automática:** Costo por sesión bloqueado y calculado según el menú gastronómico.
* **Modelado POO:** Uso de la clase pública `GestionClientes` y método de cálculo `calcular_costo_total`.
* **Módulo de Reporte:** Despliegue de factura detallada del servicio prestado.

---

## 📝 Instrucciones para la Integración (Compañeros de Grupo)

Para que el proyecto de cada integrante funcione dentro del menú consolidador de la Fase 2, se deben seguir estos pasos:

1. **Consolidar el código:** Todo el código fuente de su aplicación debe estar consolidado en un único archivo llamado exactamente `app.py`.
2. **Subir a su carpeta:** Cada estudiante debe colocar su archivo `app.py` dentro de la carpeta que lleva su nombre (en la ruta `projects/Su Nombre Completo/`).
3. **Opción alternativa:** Pueden enviarme directamente su archivo `app.py` por los canales de comunicación y yo me encargaré de insertarlo en la carpeta correspondiente.

> **Nota:** El menú principal (`main.py`) ya está programado y diseñado con una arquitectura tolerante a fallos para leer y ejecutar automáticamente cualquier archivo `app.py` que detecte dentro de esas carpetas.

---

## 💻 Instrucciones de Ejecución

1. Clonar o descargar el repositorio completo.
2. Asegurarse de tener instalado **Python 3.10** o superior con soporte para `tkinter`.
3. Abrir la terminal en la carpeta raíz `ConsolidadoFase2Grupo93/`.
4. Ejecutar el menú principal:

```
python main.py
```

1. En la interfaz gráfica del menú, hacer clic en el nombre del estudiante cuyo proyecto se desea probar.
