from PyQt5.QtWidgets import QApplication
import sys
from new import HomeWindow

# Starting the application
app = QApplication(sys.argv)
mainwindow = HomeWindow()

# Exiting
try:
	sys.exit(app.exec_())
except: 
	print("Arigato")