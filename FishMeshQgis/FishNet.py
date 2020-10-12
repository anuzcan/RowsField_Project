import numpy as np

def point_pos(origin, amplitude, angle, rotation=0, clockwise=False):
    if abs(rotation) > 360:
        rotation %= 360
    if clockwise:
        rotation *= -1
    if clockwise:
        angle -= rotation
        angle = angle if angle > 0 else angle + 360
    else:
        angle = (360 - angle if angle > 0 else -1 * angle) - rotation
        angle = angle if angle > 0 else angle + 360

    theta_rad = math.radians(angle)
    return float(origin[0] + amplitude * math.sin(theta_rad)), float(origin[1] + amplitude * math.cos(theta_rad))

epsg = "EPSG:5367"

crsSrc = QgsCoordinateReferenceSystem("EPSG:4326")          
crsDest = QgsCoordinateReferenceSystem(epsg) 
transformContext = QgsProject.instance().transformContext()
xform = QgsCoordinateTransform(crsSrc, crsDest, transformContext)

ancho = 10
alto = 20
lineas = 2
columnas = 2
angulo = 45

points = []

p_init = xform.transform(QgsPointXY(-85.56754,10.42588))
print(p_init)
p_final = point_pos(p_init,10,45)

points.append(p_init)
points.append(p_final)
print(points)
print(points[1])

  
uri = "Point?crs=epsg:" + epsg[5:] + "&field=id:integer""&index=yes"

mem_layer = QgsVectorLayer(uri,
                           'grid',
                           'memory')


prov = mem_layer.dataProvider()


feat = QgsFeature()
feat.setAttributes([0])
feat.setGeometry(QgsGeometry.fromPointXY(points[0]))
prov.addFeatures([feat])
QgsProject.instance().addMapLayer(mem_layer)

'''
sideLength = 100
bufferLength = sideLength/(2*np.sin(np.pi*60/180))
polygonSides = 3
 
p_init = QgsPointXY(328903.430,1153762.920)
p1 = QgsPointXY(p_init.x()-sideLength/2, p_init.y()-bufferLength)
 
points = []
 
inc_x = sideLength/2
inc_y = (sideLength/2)*np.tan(np.pi*30/180)
 
x = p1.x() + inc_x
y = p1.y()
 
rows = 8
cols = 20
 
if cols%2 == 0:
    coef = 1
else:
    coef = 1.5
    cols += 1
 
p_final = QgsPointXY(p_init.x() + (cols+2)*sideLength/2-coef*sideLength, p_init.y() - rows*sideLength*np.cos(np.pi*30/180) )
 
for i in range(rows):
    ver2 = i%2
    for j in range(cols+2):
        ver1 = j%2
        point = QgsPointXY(x, y)
        points.append(point)
        x += inc_x
        if ver1 == 0:
            y += inc_y
        else:
            y -= inc_y
     
    y -= sideLength*np.cos(np.pi*30/180)
     
    if ver2 == 0:
        h = 0
    else:
        h = inc_x
 
    x = p1.x() + h
 
epsg = 5367
  
uri = "Polygon?crs=epsg:" + str(epsg) + "&field=id:integer""&index=yes"
  
mem_layer = QgsVectorLayer(uri,
                           'grid',
                           'memory')
  
prov = mem_layer.dataProvider()
 
extent = QgsRectangle(p_init, p_final)
 
geom_rect = QgsGeometry.fromRect(extent)
 
k=0
 
for i, point in enumerate(points):
    ver = i%2
     
    geom = QgsGeometry.fromPolygonXY([[ QgsPointXY(point[0] + np.sin(angle)*bufferLength, point[1] + np.cos(angle)*bufferLength)
                                   for angle in np.linspace(0, 2*np.pi, polygonSides + 1, endpoint = True) ]])
 
    if ver != 0:
        geom.rotate(60,point)
 
    if geom.intersects(geom_rect):
        outFeat = QgsFeature()
        new_geom = geom.intersection(geom_rect)
         
        if new_geom.wkbType() == QgsWkbTypes.Polygon:
  
            outFeat.setGeometry(new_geom)
      
            outFeat.setAttributes([k])
     
            prov.addFeatures([outFeat])
 
            k += 1
 
QgsProject.instance().addMapLayer(mem_layer)
'''
#http://blogdezeka.blogspot.com/2020/01/clase-plantilla-con-qdialog-para.html