import cv2
import gdal

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

		raster_imagen = cv2.resize(self.raster_imagen, dsize)
		cv2.imshow('tif',raster_imagen)

	def info(self):
		print('path archivo: ',self.path)
		print('raster tipo: ', self.raster_imagen.dtype)
		print('Dimensiones: ',self.dimensiones)
		print('Proyeccion: ',self.raster_ds.GetProjection())
		print('Coordenadas Origen',self.raster_ds.GetGeoTransform())


		
