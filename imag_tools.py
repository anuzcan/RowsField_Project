import cv2
import numpy as np

class raster_read(object):
	def __init__(self, file):
		self.path = file
		self.raster_imagen = cv2.imread(self.path,cv2.IMREAD_COLOR)
		self.raster_origen = self.raster_imagen

	def show_imagen(self):

		cv2.imshow('tif',self.raster_imagen)

	def resize(self,resize):
		scale_percent = resize
		width = int(self.raster_imagen.shape[1] * scale_percent / 100)
		height = int(self.raster_imagen.shape[0] * scale_percent / 100)
		dsize = (width,height)
		self.raster_imagen = cv2.resize(self.raster_imagen, dsize)


	def procesar(self,alpha = 0):

		# (0 < alpha < 1) Menor Contraste; (alpha > 1) Mayor Contraste; (alpha = 1) Sin Cambios      
		beta = 50 #Enter the beta value [0-100]

		b,g,r = cv2.split(self.raster_imagen)
		gscale = 2*g-r-b
		self.img_detection = cv2.Canny(gscale,280,290,apertureSize = 3) 

		#self.img_detection = cv2.addWeighted(self.raster_imagen, alpha, np.zeros(self.raster_imagen.shape, self.raster_imagen.dtype), 0, 0)
		#self.img_detection = cv2.cvtColor(self.img_detection, cv2.COLOR_BGR2GRAY)
		cv2.imshow('Proceso',gscale)


	def filter_imagen(self):

		self.hsv = cv2.cvtColor(self.raster_imagen,cv2.COLOR_BGR2HSV)
		
		cv2.imshow('hsv',self.hsv)

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
		cv2.imwrite(path,self.contrast_img)

	

	def info(self):
		print('path archivo: ',self.path)
		
