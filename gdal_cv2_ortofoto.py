import cv2
import numpy as np
#import gdal
import imag_tools


file = 'Raster/odm.tif'
fileout = 'Resultados/odm.tif'

raster = imag_tools.raster_read(file)
raster.show_imagen(10)
raster.info()

#hsv = cv2.cvtColor(imagen,cv2.COLOR_BGR2HSV)

while(True):

	if cv2.waitKey(1) & 0xFF == ord("q"):
		break


#arr = ds.ReadAsArray()
"""


h0 = 33
h1 = 104
s0 = 41
s1 = 125
v0 = 118
v1 = 204

HSVbajo = np.array((h0,s0,v0))
HSValto = np.array((h1,s1,v1))

mask = cv2.inRange(hsv,HSVbajo,HSValto)
cv2.imshow('Macara', mask)

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


cv2.imwrite(fileout,raster_imagen)
"""