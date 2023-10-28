import platform
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkfont
import cv2
import chardet


def boton_calibrar():  
    # Muestra un mensaje en el cuadrado
    cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#000000")
    cuadrado.grid(row=0, column=0, sticky="nsew")
    cuadrado.delete("all")
    cuadrado.create_text(0, 0, text="Se presionó el botón detectar", anchor="nw", fill="#ffffff")
    cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)

    # Crea un label para mostrar la imagen
    muestra_imagen = tk.Label(cuadrado, width=480, height=480, bg="#cccccc")
    muestra_imagen.place(x=0, y=0)

    # Abre la imagen
    captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    while True:
      ret, frame = captura.read()
      # Muestra la imagen en el label
      #frame = imutils.resize(frame, width=480, height=480)
      img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      img = Image.fromarray(img)
      img = ImageTk.PhotoImage(img)
      muestra_imagen.configure(image=img)
      muestra_imagen.image = img
      #Actualiza la pantalla
      ventana.update()

      # Si se presiona la tecla ESC, se detiene el video
      tecla = cv2.waitKey(1) & 0xFF
      if tecla == 27:
        break

# Función para el botón Configurar
def boton_configurar():
    apagar_camara()
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

    # Crea un label para mostrar la imagen
    muestra_imagen = tk.Label(cuadrado, width=480, height=480, bg="#cccccc")
    muestra_imagen.place(x=0, y=0)
     # Minimiza la ventana
    ventana.iconify()

    # Coloca la ventana en la barra de la hora
    if platform.system() == "Windows":
      ventana.wm_state("iconic")
    elif platform.system() == "Darwin":
      ventana.wm_state("iconified")
    else:
      ventana.wm_state("minimized")


    # Abre la imagen
    captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    
    while True:
      ret, frame = captura.read()
      # Muestra la imagen en el label
      #frame = imutils.resize(frame, width=480, height=480)
      img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
      img = Image.fromarray(img)
      img = ImageTk.PhotoImage(img)
      muestra_imagen.configure(image=img)
      muestra_imagen.image = img
      #Actualiza la pantalla
      ventana.update()

      # Si se presiona la tecla ESC, se detiene el video
      tecla = cv2.waitKey(1) & 0xFF
      if tecla == 27:
        break


# Función para el botón Documentación
def boton_documentacion():
    # Obtener la codificación del archivo
    with open("documentacion.txt", "rb") as archivo:
        contenido = archivo.read()

    # Detectar la codificación del archivo
    encoding = chardet.detect(contenido)["encoding"]

    # Si la codificación es desconocida, establecerla a ISO-8859-1
    if encoding is None:
        encoding = "iso-8859-1"

    # Abre el archivo de texto
    with open("documentacion.txt", "r", encoding=encoding) as archivo:
        # Lee el contenido del archivo
        texto = archivo.read()

    # Muestra un mensaje en el cuadrado
    cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#FFFFFF")
    cuadrado.grid(row=0, column=0, sticky="nsew")
    cuadrado.delete("all")
    cuadrado.create_text(10, 2, text=texto, anchor="nw", fill="#220202")
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

# Comprobar si la camara esta encendida
def apagar_camara():
    captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, frame = captura.read()
    if ret == True:
      captura.release() 
      return True
    else:
      return False



# Interface principal de la aplicacion 
# Crea la ventana
ventana = tk.Tk()
ventana.title("Aplicación de detección y alerta")
ventana.geometry('480x536')
ventana.resizable(width=False, height=False)

# Crea el cuadrado negro
cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#ffffff")
cuadrado.grid(row=0, column=0, sticky="nsew")
fuente_titulo = tk.font.Font(family="Arial", size=13, weight="bold")
cuadrado.create_text(240, 50, text="Aplicación informática para la detección y alerta de", font=fuente_titulo, anchor="center")
cuadrado.create_text(240, 70, text="posturas corporales incorrectas en usuarios", font=fuente_titulo, anchor="center")
cuadrado.create_text(240, 90, text="de equipos de computación", font=fuente_titulo, anchor="center")
# Crea la imagen
imagen = Image.open("logo.jpg")
image = ImageTk.PhotoImage(imagen)

# Coloca la imagen debajo del texto
cuadrado.create_image(240, 200, image=image, anchor="center")

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

