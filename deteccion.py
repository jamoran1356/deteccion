import platform
import tkinter as tk
import tkinter.font as tkfont
import cv2



def comenzar_captura():
  cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

  x1, y1 = 190,80
  x2, y2 = 450,398

  count = 0

  while True:
    ret, frame = cap.read()
    if ret == False: break

    cv2.imshow('frame', frame)
      
    k = cv2.waitKey(1) 
    if k == 27:
      break
  cap.release()
  
  cv2.destroyAllWindows()    

# Función para el botón Calibrar
def boton_calibrar():
    # Muestra un mensaje en el cuadrado
    cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#DAD9D9")
    cuadrado.grid(row=0, column=0, sticky="nsew")
    cuadrado.delete("all")
    cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)

    cuadrado.after(50, lambda: comenzar_captura())


# Función para el botón Configurar
def boton_configurar():
    # Muestra un mensaje en el cuadrado
    cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#DAD9D9")
    cuadrado.grid(row=0, column=0, sticky="nsew")
    cuadrado.delete("all")
    cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)

    # Crea los botones de sonido
    boton_volumen = tk.Button(cuadrado, text="Volumen", padx=20, pady=10, width=20, anchor="center") 
    boton_volumen.place(x=150, y=100)
    boton_tono = tk.Button(cuadrado, text="Tono", padx=20, pady=10, width=20, anchor="center") 
    boton_tono.place(x=150, y=150)
    boton_eco = tk.Button(cuadrado, text="Eco", padx=20, pady=10, width=20, anchor="center") 
    boton_eco.place(x=150, y=200)


# Función para el botón Detectar
def boton_detectar():
  # Muestra un mensaje en el cuadrado
  cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#000000")
  cuadrado.grid(row=0, column=0, sticky="nsew")
  cuadrado.delete("all")
  cuadrado.create_text(0, 0, text="Se presionó el botón detectar", anchor="nw", fill="#ffffff")
  cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)

  # Minimiza la ventana
  ventana.iconify()

  # Coloca la ventana en la barra de la hora
  if platform.system() == "Windows":
    ventana.wm_state("iconic")
  elif platform.system() == "Darwin":
    ventana.wm_state("iconified")
  else:
    ventana.wm_state("minimized")

  # Muestra un mensaje en el cuadrado
  cuadrado.delete("all")
  cuadrado.create_text(0, 0, text="Se ha comenzado con la detección", anchor="nw", fill="#ffffff")
  cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)



# Función para el botón Documentación
def boton_documentacion():
    # Abre el archivo de texto
    archivo = open("documentacion.txt", "r")
    # Lee el contenido del archivo
    contenido = archivo.read()

    # Muestra un mensaje en el cuadrado
    cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#FFFFFF")
    cuadrado.grid(row=0, column=0, sticky="nsew")
    cuadrado.delete("all")
    cuadrado.create_text(10, 2, text=contenido, anchor="nw", fill="#220202")
    cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)





# Función para el botón Acerca de
def boton_acerca_de():
  # Muestra un mensaje en el cuadrado
  cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#FFFFFF")
  cuadrado.grid(row=0, column=0, sticky="nsew")
  cuadrado.delete("all")
  cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)

  # Crea los botones de sonido

  # Título de la aplicación
  fuente_titulo = tk.font.Font(family="Arial", size=13, weight="bold")
  cuadrado.create_text(240, 50, text="Aplicación informática para la detección y alerta de", font=fuente_titulo, anchor="center")
  cuadrado.create_text(240, 70, text="posturas corporales incorrectas en usuarios", font=fuente_titulo, anchor="center")
  cuadrado.create_text(240, 90, text="de equipos de computación", font=fuente_titulo, anchor="center")

  # Tutores académicos
  fuente_contenido = tk.font.Font(family="Arial", size=10, weight="normal")
  cuadrado.create_text(240, 140, text="Tutor académico:", font=fuente_titulo, anchor="center")
  
  cuadrado.create_text(240, 160, text="DR. JOSÉ OROPEZA", font=fuente_contenido, anchor="center")

  # Tutor metodológico
  cuadrado.create_text(240, 190, text="Tutor metodológico:", font=fuente_titulo, anchor="center")
  cuadrado.create_text(240, 210, text="MSC. JORGE TORREALBA", font=fuente_contenido, anchor="center")

  # Integrantes
  cuadrado.create_text(240, 240, text="Integrantes:", font=fuente_titulo, anchor="center")
  cuadrado.create_text(240, 260, text="DAVID, REINALDO", font=fuente_contenido, anchor="center")
  cuadrado.create_text(240, 280, text="MORÁN, JESÚS", font=fuente_contenido, anchor="center")
  cuadrado.create_text(240, 300, text="RUIZ JOSÉ", font=fuente_contenido, anchor="center")

  # Actualiza la ventana
  ventana.update()



# Función para el botón Salir
def boton_salir():
    # Cierra la ventana
    ventana.destroy()



# Crea la ventana
ventana = tk.Tk()
ventana.title("Aplicación de detección y alerta")

# Crea el cuadrado negro
cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#000000")
cuadrado.grid(row=0, column=0, sticky="nsew")

# Crea los botones
boton_calibrar = tk.Button(ventana, text="Calibrar", command=boton_calibrar)
boton_configurar = tk.Button(ventana, text="Configurar", command=boton_configurar)
boton_detectar = tk.Button(ventana, text="Detectar", command=boton_detectar)
boton_documentacion = tk.Button(ventana, text="Documentación", command=boton_documentacion)
boton_acerca_de = tk.Button(ventana, text="Acerca de", command=boton_acerca_de)
boton_salir = tk.Button(ventana, text="Salir", command=boton_salir)

# Coloca los botones en la ventana
cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)
boton_calibrar.grid(row=1, column=0, sticky="nsew")
boton_configurar.grid(row=1, column=1, sticky="nsew")
boton_detectar.grid(row=1, column=2, sticky="nsew")
boton_documentacion.grid(row=2, column=0, sticky="nsew")
boton_acerca_de.grid(row=2, column=1, sticky="nsew")
boton_salir.grid(row=2, column=2, sticky="nsew")

ventana.mainloop()

