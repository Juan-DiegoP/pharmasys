import tkinter as tk
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.geometry('800x400')
root.title("PharmaSys")

# Crear el widget Notebook (pestañas)
notebook = ttk.Notebook(root)

# Crear los frames que irán dentro de las pestañas
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
tab3 = ttk.Frame(notebook)
tab4 = ttk.Frame(notebook)

# Añadir las pestañas al Notebook
notebook.add(tab1, text="Principios Activos")
notebook.add(tab2, text="Medicamentos")
notebook.add(tab3, text="Producción")
notebook.add(tab4, text="Control de Calidad")

# Empaquetar el Notebook
notebook.pack(expand=True, fill="both")

# MODULO 1 - PRINCIPIOS ACTIVOS

titulo = tk.Label(tab1,
                  text="FORMULARIO DE PRINCIPIOS ACTIVOS",
                  font=("Arial", 16, "bold"),
                  fg="blue")
titulo.pack(pady=20)

form_frame = tk.Frame(tab1)
form_frame.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame, text="Codigo:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0,10), pady=10)
codigo = tk.Entry(form_frame, width=25)
codigo.grid(row=1, column=1)

tk.Label(form_frame, text="Nombre Cientifico:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0,10), pady=10)
nombre = tk.Entry(form_frame, width=25)
nombre.grid(row=2, column=1)

tk.Label(form_frame, text="Formula Quimica:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0,10), pady=10)
formula = tk.Entry(form_frame, width=25)
formula.grid(row=3, column=1)

tk.Label(form_frame, text="Clasificacion:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0,10), pady=10)
clasificacion = tk.Entry(form_frame, width=25)
clasificacion.grid(row=4, column=1)

tk.Label(form_frame, text="Origen:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0,10), pady=10)
origen = tk.Entry(form_frame, width=25)
origen.grid(row=5, column=1)

tk.Label(form_frame, text="Metodo Obtencion:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0,10), pady=10)
metodo = tk.Entry(form_frame, width=25)
metodo.grid(row=6, column=1)

button_frame = tk.Frame(tab1)
button_frame.pack(pady=20)

tk.Button(button_frame, text="Guardar", bg="#4CAF50", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Actualizar", bg="#2196F3", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Eliminar", bg="#f44336", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame, text="Limpiar", bg="#FF9800", fg="white", width=10).pack(side=tk.LEFT, padx=5)

# MODULO 2 - MEDICAMENTO

titulo2 = tk.Label(tab2,
                   text="FORMULARIO DE MEDICAMENTOS",
                   font=("Arial", 16, "bold"),
                   fg="green")
titulo2.pack(pady=20)

form_frame2 = tk.Frame(tab2)
form_frame2.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame2, text="Codigo:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0,10), pady=10)
codigo_m = tk.Entry(form_frame2, width=25)
codigo_m.grid(row=1, column=1)

tk.Label(form_frame2, text="Nombre Comercial:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0,10), pady=10)
nombre_m = tk.Entry(form_frame2, width=25)
nombre_m.grid(row=2, column=1)

tk.Label(form_frame2, text="Forma Farmaceutica:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0,10), pady=10)
forma = tk.Entry(form_frame2, width=25)
forma.grid(row=3, column=1)

tk.Label(form_frame2, text="Indicaciones:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0,10), pady=10)
indicaciones = tk.Entry(form_frame2, width=25)
indicaciones.grid(row=4, column=1)

tk.Label(form_frame2, text="Contraindicaciones:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0,10), pady=10)
contra = tk.Entry(form_frame2, width=25)
contra.grid(row=5, column=1)

tk.Label(form_frame2, text="Precio:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0,10), pady=10)
precio = tk.Entry(form_frame2, width=25)
precio.grid(row=6, column=1)

button_frame2 = tk.Frame(tab2)
button_frame2.pack(pady=20)

tk.Button(button_frame2, text="Guardar", bg="#4CAF50", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame2, text="Actualizar", bg="#2196F3", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame2, text="Eliminar", bg="#f44336", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame2, text="Limpiar", bg="#FF9800", fg="white", width=10).pack(side=tk.LEFT, padx=5)

# MODULO 3 - PRODUCCION

titulo3 = tk.Label(tab3,
                   text="FORMULARIO DE PRODUCCION",
                   font=("Arial", 16, "bold"),
                   fg="red")
titulo3.pack(pady=20)

form_frame3 = tk.Frame(tab3)
form_frame3.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame3, text="Numero de Lote:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0,10), pady=10)
lote = tk.Entry(form_frame3, width=25)
lote.grid(row=1, column=1)

tk.Label(form_frame3, text="Medicamento:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0,10), pady=10)
medicamento = tk.Entry(form_frame3, width=25)
medicamento.grid(row=2, column=1)

tk.Label(form_frame3, text="Fecha Fabricacion:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0,10), pady=10)
fecha = tk.Entry(form_frame3, width=25)
fecha.grid(row=3, column=1)

tk.Label(form_frame3, text="Cantidad Producida:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0,10), pady=10)
cantidad = tk.Entry(form_frame3, width=25)
cantidad.grid(row=4, column=1)

tk.Label(form_frame3, text="Responsable:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0,10), pady=10)
responsable = tk.Entry(form_frame3, width=25)
responsable.grid(row=5, column=1)

tk.Label(form_frame3, text="Equipos Utilizados:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0,10), pady=10)
equipos = tk.Entry(form_frame3, width=25)
equipos.grid(row=6, column=1)

button_frame3 = tk.Frame(tab3)
button_frame3.pack(pady=20)

tk.Button(button_frame3, text="Guardar", bg="#4CAF50", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame3, text="Actualizar", bg="#2196F3", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame3, text="Eliminar", bg="#f44336", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame3, text="Limpiar", bg="#FF9800", fg="white", width=10).pack(side=tk.LEFT, padx=5)

# MODULO 4 - CONTROL CALIDAD

titulo4 = tk.Label(tab4,
                   text="FORMULARIO DE CONTROL DE CALIDAD",
                   font=("Arial", 16, "bold"),
                   fg="purple")
titulo4.pack(pady=20)

form_frame4 = tk.Frame(tab4)
form_frame4.pack(pady=20, anchor="w", padx=50)

tk.Label(form_frame4, text="Codigo Analisis:", font=("Arial", 12)).grid(row=1, column=0, sticky="w", padx=(0,10), pady=10)
analisis = tk.Entry(form_frame4, width=25)
analisis.grid(row=1, column=1)

tk.Label(form_frame4, text="Lote Evaluado:", font=("Arial", 12)).grid(row=2, column=0, sticky="w", padx=(0,10), pady=10)
lote_eval = tk.Entry(form_frame4, width=25)
lote_eval.grid(row=2, column=1)

tk.Label(form_frame4, text="Tipo de Prueba:", font=("Arial", 12)).grid(row=3, column=0, sticky="w", padx=(0,10), pady=10)
prueba = tk.Entry(form_frame4, width=25)
prueba.grid(row=3, column=1)

tk.Label(form_frame4, text="Resultados:", font=("Arial", 12)).grid(row=4, column=0, sticky="w", padx=(0,10), pady=10)
resultado = tk.Entry(form_frame4, width=25)
resultado.grid(row=4, column=1)

tk.Label(form_frame4, text="Analista Responsable:", font=("Arial", 12)).grid(row=5, column=0, sticky="w", padx=(0,10), pady=10)
analista = tk.Entry(form_frame4, width=25)
analista.grid(row=5, column=1)

tk.Label(form_frame4, text="Conformidad:", font=("Arial", 12)).grid(row=6, column=0, sticky="w", padx=(0,10), pady=10)
conformidad = tk.Entry(form_frame4, width=25)
conformidad.grid(row=6, column=1)

button_frame4 = tk.Frame(tab4)
button_frame4.pack(pady=20)

tk.Button(button_frame4, text="Guardar", bg="#4CAF50", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame4, text="Actualizar", bg="#2196F3", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame4, text="Eliminar", bg="#f44336", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(button_frame4, text="Limpiar", bg="#FF9800", fg="white", width=10).pack(side=tk.LEFT, padx=5)

root.mainloop()  