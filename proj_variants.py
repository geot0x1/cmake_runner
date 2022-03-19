from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt6.QtWidgets import QSplitter, QBoxLayout
from PyQt6.QtGui import QPixmap, QCursor, QAction
import pickle
import sys
import os

from openpyxl import Workbook
import project_settings
from project_settings import Variant


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


def program_terminate():
	print("program closing...")
	sys.exit(0)

class Button(QPushButton):
	def __init__(self, widget, variant):
		super().__init__(widget)
		self.variant = variant
		self.setStyleSheet("QPushButton{background-color: #252121; border-style: inset; text-align: left; color: #ccc4c4; font-size: 15px;}")
		self.clicked.connect(self.mouse_click)
		self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
		self.setText("  " + variant.buildType + ": " + variant.shortName)
		self.setToolTip(variant.description)
		font_width = self.fontMetrics().boundingRect(self.text()).width()
		self.label = QLabel(self)
		self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)
		self.label.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
		self.label.move(font_width + 30, 7)
		self.label.setText(variant.longName)
		self.label.resize(300, self.height()-15)
		self.label.setStyleSheet("QLabel{color: #918787;}")

	def enterEvent(self, event):
		self.setStyleSheet("QPushButton{background-color: #332d2d; border-style: inset; text-align: left; color: #ccc4c4; font-size: 15px;}")

	def leaveEvent(self, event):
		self.setStyleSheet("QPushButton{background-color: #252121; border-style: inset; text-align: left; color: #ccc4c4; font-size: 15px;}")
	
	def save_variant(self):
		var = dict()
		var['variantName'] = self.variant.variantName
		var['buildType'] = self.variant.buildType
		var['settings'] = self.variant.settings
		project_settings.save_current_variant(var, ".")

	def mouse_click(self):
		self.save_variant()
		program_terminate()


class MainApplication(QMainWindow):
	def __init__(self, variants:Variant):
		super().__init__()
		self.variants = variants
		self.resize(400, 0)
		self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
		self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
		# self.move(QCursor.pos())
		self.setStyleSheet("background-color: #252121;")
		self.create_widgets()
	
	def create_widgets(self):
		self.buttons = list()
		for i in range(len(self.variants)):
			variant = self.variants[i]
			button = Button(self, variant)
			button.move(0, i * 30)
			button.resize(self.width(), 30)
			self.resize(400, self.height()+30)
			self.buttons.append(button)
	
	def resizeEvent(self, event):
		QWidget.resizeEvent(self, event)
	
	def closeEvent(self, event):
		program_terminate()



if __name__ == '__main__':
	if len(sys.argv) < 2:
		print(" -- Error: No workspace given")
		sys.exit(0)
	workspace =  sys.argv[1]
	variants = project_settings.read_project_variants(workspace)
	app = QApplication(sys.argv)
	window = MainApplication(variants)
	window.show()
	app.exec()
	program_terminate()