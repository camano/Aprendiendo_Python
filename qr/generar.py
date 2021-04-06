import qrcode
from PIL import Image

cadena=input("Introdusca el texto para el qr :")
imagen=qrcode.make(cadena)

nombre_imagen=input("Introdusca el nombre de la imagen : ")+".png"
archivo_imagen=open(nombre_imagen,'wb')
imagen.save(archivo_imagen)
archivo_imagen.close()

ruta_imagen='./'+nombre_imagen
Image.open(ruta_imagen).show()