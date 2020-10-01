from PyQt5.QtCore import Qt
import itertools

class Dlg(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.layout = QGridLayout(self)
        self.label1 = QLabel('Select polygon layer: ')
        self.wcb = QgsMapLayerComboBox()
        self.wcb.setFixedWidth(200)
        self.btn1 = QPushButton('OK', self)
        self.btn1.setFixedWidth(50)

        self.layout.addWidget(self.label1, 0, 0)
        self.layout.addWidget(self.wcb, 0, 1)
        self.layout.addWidget(self.btn1, 1, 1)
        
        self.btn1.clicked.connect(self.borders_features)

    def borders_features(self):
        
        layer = self.wcb.currentLayer()
        
        try:
            features = layer.selectedFeatures()

            list = range(len(features))

            types = [ features[i].geometry().intersection(features[j].geometry()).type()
                      for i,j in itertools.combinations(list, 2)
                      if features[i].geometry().intersects(features[j].geometry()) ]
            
            intersections = [ features[i].geometry().intersection(features[j].geometry()).asWkt()
                              for i,j in itertools.combinations(list, 2)
                              if features[i].geometry().intersects(features[j].geometry()) ]
            
            n = len(intersections)
            
            if n == 0:
                
                iface.messageBar().pushMessage("Warning: ",
                                               "There is not adjacent selected features",
                                               Qgis.Warning, 5)
                
                return

            #creating a memory layer for multilinestring
            crs = layer.crs()
            epsg = crs.postgisSrid()
        
            if crs.isGeographic() is False:
                string = "length_m"
            else:
                string = "length_km"
        
            uri = "MultiLineString?crs=epsg:" + str(epsg) + "&field=id:integer&field=" + string + ":double""&index=yes"
     
            mem_layer = QgsVectorLayer(uri,
                                       "multipolyline",
                                       "memory")
                
            QgsProject.instance().addMapLayer(mem_layer)
             
            mem_layer.startEditing()
             
            #Set features
            feature = [QgsFeature() for i in range(n)]
            
            k = 0
            dao = QgsDistanceArea()
            dao.setEllipsoid('WGS84')
            
            for i in range(n):
                if types[i] == 1:
                    #set geometry
                    geom = QgsGeometry.fromWkt(intersections[i])
                    if crs.isGeographic() is False:
                        l = geom.length()
                    else:
                        l = dao.measureLength(geom)/1000
                    feature[i].setGeometry(geom)
                    #set attributes values
                    feature[i].setAttributes([k, l])
                    mem_layer.addFeature(feature[i])
                    k += 1
            
            #stop editing and save changes
            mem_layer.commitChanges()

        except AttributeError:
            self.iface.messageBar().pushMessage("Warning: ",
                                                "There is not adjacent selected features",
                                                Qgis.Warning, 5)

            return

w = Dlg()
w.setWindowTitle('Borders Features')
w.setWindowFlags(Qt.WindowStaysOnTopHint)
w.move(300,200)
w.show()

#http://blogdezeka.blogspot.com/2020/01/clase-plantilla-con-qdialog-que.html