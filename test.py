import tkinter as tk
from PIL import Image,ImageTk
import cv2
import imutils

print ('leyendo archivos...')

#funciones de los archivos
def calibrar():
  cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#FFFFFF")
  cuadrado.grid(row=0, column=0, sticky="nsew")
  cuadrado.delete("all")
  cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)

  muestra_video = tk.Label(cuadrado, bg="pink")
  muestra_video.place(x=0, y=0)
  
  def video_stream():
    global video
    video = cv2.VideoCapture(0)
    iniciar()

  def iniciar():
    global video
    ret, frame = video.read()

    if ret == True:
      frame = imutils.resize(frame, width=480)  
      frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RBG)
      img = Image.fromarray(frame)
      image = ImageTk.PhotoImage(image=img)
      muestra_video.configure(image=image)
      muestra_video.image = image
      muestra_video.after(10, iniciar)

def salir():
    # Cierra la ventana
    ventana.destroy()








ventana = tk.Tk()
ventana.title("Aplicación de detección y alerta")

# Crea el cuadrado negro
cuadrado = tk.Canvas(ventana, width=480, height=480, bg="#000000")
cuadrado.grid(row=0, column=0, sticky="nsew")

# Crea los botones
boton_calibrar = tk.Button(ventana, text="Calibrar", command=calibrar)
boton_configurar = tk.Button(ventana, text="Configurar", command="")
boton_detectar = tk.Button(ventana, text="Detectar", command="")
boton_documentacion = tk.Button(ventana, text="Documentación", command="")
boton_acerca_de = tk.Button(ventana, text="Acerca de", command="")
boton_salir = tk.Button(ventana, text="Salir", command=salir)

# Coloca los botones en la ventana
cuadrado.grid(row=0, column=0, sticky="nsew", columnspan=3)
boton_calibrar.grid(row=1, column=0, sticky="nsew")
boton_configurar.grid(row=1, column=1, sticky="nsew")
boton_detectar.grid(row=1, column=2, sticky="nsew")
boton_documentacion.grid(row=2, column=0, sticky="nsew")
boton_acerca_de.grid(row=2, column=1, sticky="nsew")
boton_salir.grid(row=2, column=2, sticky="nsew")

ventana.mainloop()


