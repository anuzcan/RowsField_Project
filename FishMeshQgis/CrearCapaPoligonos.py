from qgis import utils

# Crear Capa de poligonos temporar
mem_layer = QgsVectorLayer("Polygon?crs=epsg:4326&field=id:integer""&field=area:double&index=yes","sectors","memory")

# Agregamos la capa al mapa de trabajo de Qgis
QgsProject.instance().addMapLayer(mem_layer)
  

count = 1
area = 10

poligono = QgsFeature()
vertices_poligono = [QgsPointXY(-85.49972,10.39034),QgsPointXY(-85.49922,10.39050),QgsPointXY(-85.49953,10.39072)]

print(len([vertices_poligono]))

poligono.setGeometry(QgsGeometry.fromPolygonXY([vertices_poligono]))
poligono.setAttributes([count,area])	

# Iniciamos su edicion
mem_layer.startEditing()
mem_layer.addFeatures([poligono])


# Finalizar edicion y guardar cambios
mem_layer.commitChanges()
utils.iface.mapCanvas().refresh()
iface.zoomToActiveLayer()

"""  
#points to add

points = [QgsPoint(-85.49972,10.39034),QgsPoint(-85.49922,10.39050),QgsPoint(-85.49953,10.39072)]
 
#Calculate number points
n = len(points)
 
#Set feature
feature = []
 
for i in range(n):
    feat =QgsFeature()
    feature.append(feat)
  
#values arbitraries for area attribute
area=[0.5,0.6,0.7]
  
#set attributes values 
for i in range(n):
    feature[i].setGeometry(QgsGeometry.fromPointXY(points[i]))  #Set geometry
    feature[i].setAttributes([i,area[i]])
    mem_layer.addFeature(feature[i], True)
  
#stop editing and save changes
mem_layer.commitChanges()
 
#zoom to Active Layer
#iface.zoomToActiveLayer()
"""