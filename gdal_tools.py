import gdal
import numpy as np

class raster_load(object):
	def __init__(self, file):
		self.path = file
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

	def matriz(self):

		arr = self.raster_ds.ReadAsArray()
		print(arr.shape)

	def info(self):
		print('path archivo: ',self.path)
		print('Dimensiones: ',self.dimensiones)
		print('Proyeccion: ',self.raster_ds.GetProjection())
		print('Coordenadas Origen',self.raster_ds.GetGeoTransform())

		"""

		band1 = ds.GetRasterBand(1)
		band2 = ds.GetRasterBand(2)
		band3 = ds.GetRasterBand(3)

		arr_band1 = band1.ReadAsArray()
		arr_band2 = band2.ReadAsArray()
		arr_band3 = band3.ReadAsArray()

		[cols, rows] = arr_band1.shape
		arr_min = arr.min()
		arr_max = arr.max()
		arr_mean = int(arr.mean())

		#arr_out = np.where((arr < arr_mean), 10000, arr)

		driver = gdal.GetDriverByName("GTiff")
		outdata = driver.Create(fileout, rows, cols, 1, gdal.GDT_UInt16)
		outdata.SetGeoTransform(ds.GetGeoTransform())##sets same geotransform as input
		outdata.SetProjection(ds.GetProjection())##sets same projection as input

		outdata.GetRasterBand(1).WriteArray(mask)
		outdata.GetRasterBand(1).SetNoDataValue(0)##if you want these values transparent transparent

		outdata.FlushCache() ##saves to disk!!
		outdata = None
		band=None
		ds=None

		"""