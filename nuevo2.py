# Importa todas las librerías necesarias para el funcionamiento del programa
from cv2 import resize, imwrite, imread, GaussianBlur, IMREAD_COLOR
from os import getcwd, listdir, path, remove, makedirs
from string import ascii_uppercase, digits
from random import randint, choices
from time import sleep
from PIL import Image

# Se crean algunas variables necesarias
total_images = []
total_images2 = []
scaled_images = []

# Obtiene la ruta acutal
current_path = getcwd()
# Se establece la ruta final
final_path = f'{current_path}\\scaled_images\\'

scale_level = int(input('Eliga el nivel de escala(2/4):'))
if scale_level < 4:
	scale_level = 2
else:
	scale_level = 4

keep_images = int(input('Quieres mantener las imágenes originales(1=si/2=no)?: '))
if keep_images < 2:
	keep_images = 1
else:
	keep_images = 2

# Crea la carpeta si no existe
if not path.exists(final_path):
    makedirs(final_path)

# Ejecuta esto por cada archivo en la ruta actual
for archivo in listdir(current_path):
	# Verifica si el archivo es una imágen
	if archivo.endswith('.jpg') or archivo.endswith('.jpeg') or archivo.endswith('.png'):
		# Si el archivo es una imagen entonces la lee
		image_ = imread(path.join(current_path, archivo))
		# Guarda el nombre de cada imagen en otra variable
		image2 = str(archivo)
		# Guarda tanto la información en la imágen como su nombre en listas distintas
		total_images.append(image_)
		total_images2.append(image2)

# Indica que se está empezando el proceso de escalado a cada imagen
print('Iniciando el proceso de escala. . .')
# Si el usuario eligió escalar x2 se ejecuta esto
if scale_level == 2:
	# Ejecuta esto por cada imágen en "total_images"
	for image in total_images:
		# Aplica el filtro de GaussianBlur a la imagen
		blur = GaussianBlur(image, (3,3), 0)
		# Escala la imágen al doble de su resolución original
		scaled_image = resize(blur, (int(image.shape[1]*2), int(image.shape[0]*2)))
		# Agrega la imagen escalada a una lista llamada scaled_images
		scaled_images.append(scaled_image)

# Si el usuario eligió escalar x4 se ejecuta esto
elif scale_level == 4:
	# Ejecuta esto por cada imágen en "total_images"
	for image in total_images:
		# Aplica el filtro de GaussianBlur a la imagen
		blur = GaussianBlur(image, (1,1), 0)
		# Escala la imágen al doble de su resolución original
		scaled_image1 = resize(blur, (int(image.shape[1]*2), int(image.shape[0]*2)))
	
		# Aplica el filtro GaussianBlur a la imagen escalada
		blur2 = GaussianBlur(scaled_image1, (1,1), 0)
		# Escala la imagen escalada al doble de su resolción
		scaled_image2 = resize(blur2, (int(scaled_image1.shape[1]*2), int(scaled_image1.shape[0]*2)))
		# Agrega la imagen 2 veces escalada a una lista llamada scaled_images
		scaled_images.append(scaled_image2)

# Ejecuta esto por cada imágen en "total_images"
for image in total_images2:
	# Verifica si el usuario quiere eliminar las imágenes originales
	if keep_images == 2:
		# Elimina la imágen correspondiente
		remove(path.join(current_path, image))

# Se le asigna un nombre aleatorio a cada imágen
for i in range(len(scaled_images)):
	# Genera un nombre aleatorio para la imágen escalada
	name = ''.join(choices(ascii_uppercase + digits, k = 12))
	# Optiene la extensión de la imágen original para aplicarla en la final
	extension = path.splitext(total_images2[i])[1]
	# "Escribe" la imagen escalada en la 
	imwrite(f'scaled_images/{name}{extension}', scaled_images[i])

# Se indica que el proceso de escalado a finalizado
print('Proceso finalizado!')
sleep(1)