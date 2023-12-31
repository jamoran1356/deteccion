import pygame
from tkinter import filedialog
import platform
import time
import winsound
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.font as tkfont
import cv2
import chardet
import mediapipe as mp
import os
import tkinter.messagebox as messagebox
import numpy as np

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


# Inicializa el mezclador de pygame
pygame.mixer.init()

# Crea una variable para almacenar el sonido
sound = None

def ajustar_volumen():
    # Aquí puedes ajustar el volumen. El valor debe estar entre 0.0 y 1.0.
    volumen = 0.5
    if sound is not None:
        sound.set_volume(volumen)

def seleccionar_sonido():
    global sound
    # Abre un cuadro de diálogo para seleccionar un archivo de sonido
    filename = filedialog.askopenfilename(filetypes=[("Sound files", "*.wav")])
    if filename:
        # Carga el sonido y lo almacena en la variable sound
        sound = pygame.mixer.Sound(filename)


def boton_calibrar():  
    # Define una variable para almacenar el tiempo actual
    tiempo_actual = time.time()
    image_counter = 0
    # Define una variable para almacenar el tiempo de inicio de la grabación
    tiempo_inicio = tiempo_actual + 5
    # Muestra un mensaje en el cuadrado
    cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#000000")
    cuadrado.grid(row=0, column=0, sticky="nsew")
    cuadrado.delete("all")
    cuadrado.create_text(0, 0, text="Se presionó el botón detectar", anchor="nw", fill="#ffffff")
    cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)
    
    # Crea un label para mostrar la imagen
    muestra_imagen = tk.Label(cuadrado, width=480, height=480, bg="#cccccc")
    muestra_imagen.place(x=0, y=0)
    # Lanza mensaje para preparar al usuario para almacenar la pose
    messagebox.showinfo("Alerta", "La grabación comenzará pronto, por favor colocate en la posición adecuada")

    # Abre la imagen
    captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    fourcc = cv2.VideoWriter_fourcc(*'MP4V') # Cambia el códec a 'mp4v'
    salida = cv2.VideoWriter('calibracion.mp4', fourcc, 10.0, (640,480))
    salida_img = "calibracion_.png".format(image_counter)

    # Crea un objeto Pose
    with mp_pose.Pose(static_image_mode=False) as pose:

      while True:
        ret, frame = captura.read()
        if ret == False:
          break

        
        results = pose.process(frame)
        
        # Dibuja los puntos de referencia de la pose
        if results.pose_landmarks is  not  None:
           mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                          mp_drawing.DrawingSpec(color=(85, 43, 9), thickness=2, circle_radius=3),
                                          mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))
           
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        imgex = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        muestra_imagen.configure(image=img)
        muestra_imagen.image = img

        # Verifica si el tiempo actual es mayor que el tiempo de inicio
        tiempo_actual = time.time()
        if tiempo_actual > tiempo_inicio:
            salida.write(imgex)
            cv2.imwrite(salida_img, imgex)
            image_counter += 1

        tiempo_transcurrido = time.time() - tiempo_inicio
        if tiempo_transcurrido > 5:
            messagebox.showinfo("Alerta", "La grabación ha finalizado")
            break

        ventana.update()

        # Si se presiona la tecla ESC, se detiene el video
        tecla = cv2.waitKey(1) & 0xFF
        if tecla == 27:
          break
    salida.release()
    captura.release()

# Función para el botón Configurar
def boton_configurar():
    apagar_camara()
    # Muestra un mensaje en el cuadrado
    cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#DAD9D9")
    cuadrado.grid(row=0, column=0, sticky="nsew")
    cuadrado.delete("all")
    cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)

    # Crea los botones de sonido
    boton_volumen = tk.Button(cuadrado, text="Volumen", padx=20, pady=10, width=20, anchor="center", command=ajustar_volumen) 
    boton_volumen.place(x=150, y=100)
    boton_tono = tk.Button(cuadrado, text="Tono", padx=20, pady=10, width=20, anchor="center", command=seleccionar_sonido) 
    boton_tono.place(x=150, y=150)
    


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

    # Obtenemos la imagen de referencia
    img_ref = cv2.imread('calibracion_.png')

    #creamos el objeto pose
    with mp_pose.Pose(static_image_mode=False) as pose:
        #procesamos la imagen de referencia para obtener los puntos de pose
        results_ref = pose.process(cv2.cvtColor(img_ref, cv2.COLOR_BGR2RGB))
        if results_ref.pose_landmarks is None:
            messagebox.showinfo("Alerta", "No se detectaron puntos de referencia")
            return
         #convertimos los puntos de pose a un array numpy para facilitar las comparaciones
        pose_ref = np.array([[lmk.x, lmk.y, lmk.z] for lmk in results_ref.pose_landmarks.landmark], dtype=np.float32)

        # Crea un label para mostrar la imagen
        muestra_imagen = tk.Label(cuadrado, width=480, height=480, bg="#cccccc")
        muestra_imagen.place(x=0, y=0)

        # Abre la imagen
        captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # Crea un objeto Pose

        while True:
          ret, frame = captura.read()
          if ret == False:
            break
          results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
          # Dibuja los puntos de referencia de la pose
          if results.pose_landmarks is  not  None:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                            mp_drawing.DrawingSpec(color=(85, 43, 9), thickness=2, circle_radius=3),
                                            mp_drawing.DrawingSpec(color=(255, 255, 255), thickness=2))
          
            pose_current = np.array([[lmk.x, lmk.y, lmk.z] for lmk in results.pose_landmarks.landmark], dtype=np.float32)
            # Calculamos la diferencia entre los puntos de pose
            diff = np.linalg.norm(pose_current - pose_ref) / len(pose_current)

            # Si la diferencia es mayor que el 5%, lanzamos un mensaje de alerta
            if diff > 0.15:
              ventana.wm_state("normal")
              winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
              messagebox.showinfo("Alerta", "Has adoptado una postura incorrecta, por favor corrigela")
              break

          img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
          img = Image.fromarray(img)
          img = ImageTk.PhotoImage(img)
          muestra_imagen.configure(image=img)
          muestra_imagen.image = img
          ventana.update()
          
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


