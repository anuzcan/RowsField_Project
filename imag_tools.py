import cv2
import numpy as np

class raster_read(object):
	def __init__(self, file):
		self.path = file
		self.raster_imagen = cv2.imread(self.path,cv2.IMREAD_COLOR)

	def show_imagen(self,resize):

		raster_imagen_resize = self.resize(self.raster_imagen, resize)
		cv2.imshow('tif',raster_imagen_resize)

	def filter_imagen(self,resize):

		self.hsv = cv2.cvtColor(self.raster_imagen,cv2.COLOR_BGR2HSV)
		raster_imagen_hsv_resize = self.resize(self.hsv,resize)
		cv2.imshow('hsv',raster_imagen_hsv_resize)

		h0 = 33
		h1 = 104
		s0 = 41
		s1 = 125
		v0 = 118
		v1 = 204

		HSVbajo = np.array((h0,s0,v0))
		HSValto = np.array((h1,s1,v1))

		self.mask = cv2.inRange(self.hsv,HSVbajo,HSValto)
		cv2.imshow('Macara', self.mask)

	def save_imagen(self,path):

		#cv2.imwrite(path,self.hsv)
		cv2.imwrite(path,self.mask)

	def resize(self,file,resize):
		scale_percent = resize
		width = int(self.raster_imagen.shape[1] * scale_percent / 100)
		height = int(self.raster_imagen.shape[0] * scale_percent / 100)
		dsize = (width,height)
		return cv2.resize(file, dsize)

	def info(self):
		print('path archivo: ',self.path)
		
