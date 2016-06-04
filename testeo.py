import sys
from PyQt4 import QtCore, QtGui

class MiVentana(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("Testeo")
        self.setGeometry(100,100,600,400)
        
        quit = QtGui.QPushButton("Cerrar", self)
        quit.setGeometry(450,300,70,50)
        self.connect(quit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
        
        acepta = QtGui.QPushButton("Aceptar", self)
        acepta.setGeometry(370,300,70,50)
        self.connect(acepta, QtCore.SIGNAL("clicked()"), self.saluda)
        
        etiquetanombe = QtGui.QLabel("Ingresa tu Nombre: ", self)
        etiquetanombe.setGeometry(100,100,150,30)
        self.lineanombre = QtGui.QLineEdit(self)
        self.lineanombre.setGeometry(225,100,150,30)
        self.etiquetamensaje = QtGui.QLabel(self)
        self.etiquetamensaje.setGeometry(150,200,150,30)
        
        self.botonsumar = QtGui.QRadioButton("Sumar", self)
        self.botonsumar.setGeometry(100,250,70,30)
        self.botonsumar.setChecked(True)
        self.botonrestar = QtGui.QRadioButton("Restar", self)
        self.botonrestar.setGeometry(100,280,70,30)
        self.botonmultiplicar = QtGui.QRadioButton("Multiplicar", self)
        self.botonmultiplicar.setGeometry(100,310,90,30)
        self.botondividir = QtGui.QRadioButton("Dividir", self)
        self.botondividir.setGeometry(100,340,70,30)
        
    def saluda(self):
        if len(self.lineanombre.text()) != 0:
            self.etiquetamensaje.setText("Hola " + self.lineanombre.text())
        else:
            self.etiquetamensaje.setText("No te saludare entonces")
        
        
app = QtGui.QApplication(sys.argv)
myapp = MiVentana()
myapp.show()
sys.exit(app.exec_())
