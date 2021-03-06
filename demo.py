import sys, json
from PySide.QtGui import *
from PySide.QtCore import *

qt_app = QApplication(sys.argv)
 
class LayoutExample(QWidget):

	
	
	def __init__(self):
		# Initialize the object as a QWidget and
		# set its title and minimum width
		QWidget.__init__(self)
		self.setWindowTitle('Show, Image!')
		self.setMinimumWidth(400)
 
		# Create the QVBoxLayout that lays out the whole form
		self.layout = QVBoxLayout()
		self.setLayout(self.layout)

		# Create the form layout that manages the labeled controls
		
		self.widget1 = QWidget()
		self.layout.addWidget(self.widget1)

		self.image_layout = QFormLayout()
		self.widget1.setLayout(self.image_layout)

		#SQL
		#self.connection = sqlite3.connect('teste.db')
		#self.c = self.connection.cursor()
		#self.c.execute('SELECT image FROM dados')
		
		data = {
		   'image' : ['planet.jpg', 'cat.png', 'building.jpg']
		}



		self.option = QComboBox(self)
		#for row in self.c.fetchall():
		#	self.option.addItems(row)
		self.option.addItems(data['image'])
 
		# Add it to the form layout with a label
		self.label = QLabel() 
		self.pixmap = QPixmap(self.save())
		self.label.setPixmap(self.pixmap)

		self.button = QPushButton('Configurations', self)
		self.button.clicked.connect(lambda: self.alternate(False))
		# Add it to the form layout with a label
		self.image_layout.addRow(self.label)
		self.image_layout.addRow(self.button)

		self.widget2 = QWidget()
		self.layout.addWidget(self.widget2)

		self.config_layout = QVBoxLayout()
		self.widget2.setLayout(self.config_layout)

		self.buttonSave = QPushButton('Save', self)
		self.buttonSave.clicked.connect(lambda: self.save())
		self.buttonSave.clicked.connect(lambda: self.alternate(True))

		self.config_layout.addWidget(self.option)
		self.config_layout.addWidget(self.buttonSave)
  
		# Add the form layout to the main VBox layout
		self.layout.addLayout(self.config_layout)
		self.widget1.setVisible(True)
		self.widget2.setVisible(False)
		# Add stretch to separate the form layout from the button
		self.layout.addStretch(1)
	
	def alternate(self, status):
		self.widget1.setVisible(status)
		self.widget2.setVisible(not status)

	def save(self):
		self.text = str(self.option.currentText())
		self.px = QPixmap()
		self.px.load(self.text);
		self.label.setPixmap(self.px);
		return self.text

	def run(self):
		# Show the form
		self.show()
		# Run the qt application
		qt_app.exec_()


 
# Create an instance of the application window and run it
app = LayoutExample()
app.run()
