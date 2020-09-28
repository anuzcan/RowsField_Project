import cv2
import numpy as np

import imag_tools
from gdal_tools import raster_load


file = 'Raster/odm.tif'
fileout = 'Resultados/odm.tif'

raster_data = raster_load(file)
raster_data.info()
raster_data.matriz()


raster_img = imag_tools.raster_read(file)
raster_img.show_imagen(10)
#raster_img.contras()
raster_img.filter_imagen(10)
raster_img.info()
raster_img.save_imagen(fileout)

while(True):

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break


