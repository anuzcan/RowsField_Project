import cv2
import gdal
import numpy as np

class raster_read(object):
	def __init__(self, file):
		self.path = file

		self.raster_imagen = cv2.imread(self.path,cv2.IMREAD_COLOR)
		self.raster_ds = gdal.Open(file)

		#Dimensiones del celdas del archivo y las almacenamos en variables usadas para dimensionar la ventana
		cols = self.raster_ds.RasterXSize
		rows = self.raster_ds.RasterYSize

		self.dimensiones = cols, rows

		#Extraemos las coordenadas del archivo y dimensiones de las celdas
		transform = self.raster_ds.GetGeoTransform()
		xOrigin = transform[0]				#Coordenada x de origen en mts
		yOrigin = transform[3]				#Coordenada y de origen en mts
		pixelWidth = transform[1]			#Ancho de la celda en mts
		pixelHeight = -transform[5]			#Alto de la celda en mts

	def show_imagen(self,resize):

		scale_percent = resize

		width = int(self.raster_imagen.shape[1] * scale_percent / 100)
		height = int(self.raster_imagen.shape[0] * scale_percent / 100)

		dsize = (width,height)

		raster_imagen_resize = cv2.resize(self.raster_imagen, dsize)
		
		cv2.imshow('tif',raster_imagen_resize)
		

	def filter_imagen(self,resize):

		self.hsv = cv2.cvtColor(self.raster_imagen,cv2.COLOR_BGR2HSV)

		scale_percent = resize

		width = int(self.raster_imagen.shape[1] * scale_percent / 100)
		height = int(self.raster_imagen.shape[0] * scale_percent / 100)

		dsize = (width,height)

		raster_imagen_hsv_resize = cv2.resize(self.hsv, dsize)
		cv2.imshow('hsv',raster_imagen_hsv_resize)

	def save_imagen(self,path):

		cv2.imwrite(path,self.hsv)

	def info(self):
		print('path archivo: ',self.path)
		print('raster tipo: ', self.raster_imagen.dtype)
		print('Dimensiones: ',self.dimensiones)
		print('Proyeccion: ',self.raster_ds.GetProjection())
		print('Coordenadas Origen',self.raster_ds.GetGeoTransform())

"""
		h0 = 33
		h1 = 104
		s0 = 41
		s1 = 125
		v0 = 118
		v1 = 204

		HSVbajo = np.array((h0,s0,v0))
		HSValto = np.array((h1,s1,v1))

		hsv = cv2.cvtColor(self.raster_imagen,cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(hsv,HSVbajo,HSValto)

		scale_percent = 10

		width = int(hsv.shape[1] * scale_percent / 100)
		height = int(hsv.shape[0] * scale_percent / 100)
		dsize = (width,height)

		raster_imagen_resize = cv2.resize(mask, dsize)
		cv2.imshow('tif',mask)
"""


		
