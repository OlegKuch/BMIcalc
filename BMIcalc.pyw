from ui import *
import sys

def calculate():
    try:
        mass = float(ui.massInput.text())
        height = float(ui.heightInput.text())
        BMI = mass / height ** 2
        BMI = round(BMI,1)
        ui.BMIoutput.setText(str(BMI))
    except:
        ui.BMIoutput.setText("Error!")
        
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(window)
ui.calculateButton.clicked.connect(calculate)
window.show()
sys.exit(app.exec_())
