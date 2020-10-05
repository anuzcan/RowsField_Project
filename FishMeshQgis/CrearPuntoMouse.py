from PyQt5.QtCore import Qt
from qgis.gui import QgsMapToolEmitPoint

class Dlg(QDialog):

    def __init__(self):
        QDialog.__init__(self)
        self.layout = QGridLayout(self)
        self.label1 = QLabel('Coordinates of map')
        self.line_edit = QLineEdit()
        self.line_edit.setFixedWidth(350)
        self.sel_proj = QgsProjectionSelectionWidget()
        proj = QgsProject.instance().crs().postgisSrid()
        crs = QgsCoordinateReferenceSystem()
        crs.createFromSrid(proj)
        self.sel_proj.setCrs(crs)
        self.btn1 = QPushButton('Create Point', self)

        # Save reference to the QGIS interface
        self.iface = iface
        
        # a reference to our map canvas
        self.canvas = self.iface.mapCanvas() 
        # this QGIS tool emits as QgsPoint after each click on the map canvas
        self.pointTool = QgsMapToolEmitPoint(self.canvas)

        self.layout.addWidget(self.label1, 0, 0)
        self.layout.addWidget(self.line_edit, 1, 0)
        self.layout.addWidget(self.sel_proj, 2, 0)
        self.layout.addWidget(self.btn1, 3, 0)

        self.pointTool.canvasClicked.connect(self.display_point)
        self.canvas.setMapTool(self.pointTool)
        
        self.btn1.clicked.connect(self.create_point)

    def display_point(self, point, button):
        # report map coordinates from a canvas click
        coords = "{}, {}".format(point.x(), point.y())
        self.line_edit.setText(str(coords))
    
    def create_point(self):
        
        pt = self.line_edit.text().split(',')
        
        try:
            x = float(pt[0])
            y = float(pt[1])
            point = QgsPointXY(x,y)

            epsg = self.sel_proj.crs().postgisSrid()
            
            uri = "Point?crs=epsg:" + str(epsg) + "&field=id:integer""&index=yes"

            mem_layer = QgsVectorLayer(uri,
                                       'point',
                                       'memory')

            prov = mem_layer.dataProvider()

            feat = QgsFeature()
            feat.setAttributes([0])
            feat.setGeometry(QgsGeometry.fromPointXY(point))
            prov.addFeatures([feat])
            QgsProject.instance().addMapLayer(mem_layer)

        except ValueError:
            pass

w = Dlg()
w.setWindowTitle('Point Creator')
w.setWindowFlags(Qt.WindowStaysOnTopHint)
w.show()

#http://blogdezeka.blogspot.com/2020/01/clase-plantilla-con-qdialog-para-crear.html