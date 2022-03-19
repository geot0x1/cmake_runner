from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt6.QtWidgets import QSplitter
from PyQt6.QtGui import QPixmap, QCursor, QAction
import pickle
import sys
import os

CURRENT_SCRIPT_DIR = (os.path.dirname(os.path.abspath(__file__)))

def save_settings(settings):
	file = os.path.join(CURRENT_SCRIPT_DIR, ".usrsettings.cfg")
	f = open(file, "wb")
	pickle.dump(settings, f)
	f.close()

def read_settings():
	file = os.path.join(CURRENT_SCRIPT_DIR, ".usrsettings.cfg")
	f = open(file, "rb")
	settings = pickle.load(f)
	f.close()
	return settings



class MainApplication(QMainWindow):
	def __init__(self):
		super().__init__()
		self.resize(800, 600)
		self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
		self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
		# self.move(QCursor.pos())
		self.setStyleSheet("background-color: #252121;")
		self.create_widgets()
	
	def create_widgets(self):
		self.buttons = list()
		button = QPushButton(self)
		button.setText("Debug")
		button.move(20, 20)
		button.resize(150, 30)
		button.setStyleSheet("background-color: #524340;")
		self.buttons.append(button)
	
	def resizeEvent(self, event):
		QWidget.resizeEvent(self, event)
	
	def closeEvent(self, event):
		save_settings(self.userSettings)
	
	def focusOutEvent(self, event):
		sys.exit(0)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = MainApplication()
	window.show()
	app.exec()
	sys.exit()