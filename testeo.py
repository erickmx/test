import sys
from PyQt4 import QtCore, QtGui

class MiVentana(QtGui.QDialog):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle("Testeo")
        self.setGeometry(100,100,600,400)
        
        quit = QtGui.QPushButton("Cerrar", self)
        quit.setGeometry(460,330,80,30)
        self.connect(quit, QtCore.SIGNAL("clicked()"), QtGui.qApp, QtCore.SLOT("quit()"))
        
        acepta = QtGui.QPushButton("Aceptar", self)
        acepta.setGeometry(370,330,80,30)
        self.connect(acepta, QtCore.SIGNAL("clicked()"), self.calcula)
        
        etiquetavalor1 = QtGui.QLabel("Ingresa el primer valor: ", self)
        etiquetavalor1.setGeometry(50,30,150,30)
        self.lineavalor1 = QtGui.QLineEdit(self)
        self.lineavalor1.setGeometry(210,30,150,30)
        etiquetavalor2 = QtGui.QLabel("Ingresa el segundo valor: ", self)
        etiquetavalor2.setGeometry(50,70,150,30)
        self.lineavalor2 = QtGui.QLineEdit(self)
        self.lineavalor2.setGeometry(210,70,150,30)
        
        self.etiquetaresultado = QtGui.QLabel("Resultado: ",self)
        self.etiquetaresultado.setGeometry(135,110,150,30)
        
        self.botonsumar = QtGui.QRadioButton("Sumar", self)
        self.botonsumar.setGeometry(180,170,70,30)
        self.botonsumar.setChecked(True)
        self.botonrestar = QtGui.QRadioButton("Restar", self)
        self.botonrestar.setGeometry(180,200,70,30)
        self.botonmultiplicar = QtGui.QRadioButton("Multiplicar", self)
        self.botonmultiplicar.setGeometry(180,230,90,30)
        self.botondividir = QtGui.QRadioButton("Dividir", self)
        self.botondividir.setGeometry(180,260,70,30)
        
    def calcula(self):
        if len(self.lineavalor1.text()) != 0:
            a = int(self.lineavalor1.text())
        else:
            a = 0
        if len(self.lineavalor2.text()) != 0:
            b = int(self.lineavalor2.text())
        else:
            b = 0
        
        if self.botonsumar.isChecked() == True:
            res = a + b
        if self.botonrestar.isChecked() == True:
            res = a - b
        if self.botonmultiplicar.isChecked() == True:
            res = a * b
        if self.botondividir.isChecked() == True:
            res = a / b
        
        self.etiquetaresultado.setText("Resultado:  " + str(res))
        
        
app = QtGui.QApplication(sys.argv)
myapp = MiVentana()
myapp.show()
sys.exit(app.exec_())
