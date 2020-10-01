import cv2
import numpy as np

import imag_tools
from gdal_tools import raster_load


file = 'Raster/odm_cortado.tif'
fileout = 'Resultados/odm.tif'

#raster_data = raster_load(file)
#raster_data.info()
#raster_data.matriz()
#raster_data.new_tif()


raster_img = imag_tools.raster_read(file)
#raster_img.resize(10)
raster_img.show_imagen()
raster_img.procesar(alpha = 1.5)
#raster_img.filter_imagen()
#raster_img.info()
#raster_img.save_imagen(fileout)

while(True):

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break