import sys, os
from PySide.QtGui import *
from PySide.QtCore import *

qt_app = QApplication(sys.argv)
 
class LayoutExample(QWidget):
	''' An example of PySide/PyQt absolute positioning; the main window
		inherits from QWidget, a convenient widget for an empty window. '''
 
	def __init__(self):
		# Initialize the object as a QWidget and
		# set its title and minimum width
		QWidget.__init__(self)
		self.setWindowTitle('Dynamic Greeter')
		self.setMinimumWidth(400)
 
		# Create the QVBoxLayout that lays out the whole form
		self.layout = QVBoxLayout()
 
		# Create the form layout that manages the labeled controls
		self.form_layout = QFormLayout()
 
		# The salutations that we want to make available
		self.options = ['building.jpg',
							'cat.png',
							'planet.jpg']
 
		# Create and fill the combo box to choose the salutation
		self.option = QComboBox(self)
		self.option.addItems(self.options)
 
		# Add it to the form layout with a label
		self.label = QLabel() 
		self.pixmap = QPixmap('C:/Users/Alexandre/Documents/GitHub/teste/building.jpg')
		self.label.setPixmap(self.pixmap)
		 
		# Add it to the form layout with a label
		self.form_layout.addRow(self.label)
		self.form_layout.addRow(self.option)
  
		# Add the form layout to the main VBox layout
		self.layout.addLayout(self.form_layout)
 
		# Add stretch to separate the form layout from the button
		self.layout.addStretch(1)
 
		# Create a horizontal box layout to hold the button
		self.button_box = QHBoxLayout()
 
		# Add stretch to push the button to the far right
		self.button_box.addStretch(1)
 
		# Add the button box to the bottom of the main VBox layout
		self.layout.addLayout(self.button_box)
 
		# Set the VBox layout as the window's main layout
		self.setLayout(self.layout)
 
	def run(self):
		# Show the form
		self.show()
		# Run the qt application
		qt_app.exec_()


 
# Create an instance of the application window and run it
app = LayoutExample()
app.run()