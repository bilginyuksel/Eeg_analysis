import sys
from PyQt5.QtWidgets import (QMainWindow,QListWidget,QErrorMessage ,QComboBox, QMessageBox,QWidget,QVBoxLayout,QHBoxLayout,QApplication,QLabel,QLineEdit,QCheckBox,QPushButton)
from PyQt5.QtGui import QFont,QPen,QBrush,QPainter,QColor
from PyQt5.QtCore import QRect,Qt
import test
import _thread
import time




class ConfigProperties():

    def __init__(self,x1,x2,y1,y2,width,height,width2,height2,delay,isChecked):
        self.obj_x = x1
        self.target_x = x2
        self.obj_y = y1
        self.target_y = y2
        self.obj_width = width
        self.obj_height = height
        self.target_width = width2
        self.target_height = height2
        self.delay = delay
        self.isChecked = isChecked
        self.model = test.rf_model

    def _setLogs(self,log):
        self.logs = log

    def _setModel(self,model):
        self.model = model

    def log_output(self):
        with open("log.txt","w") as f:
            f.write(self.logs)

class ConfigScreen(QWidget):

    
    def __init__(self):
        super().__init__()

        self.__RANDOM_FOREST_CLASSIFIER = 0
        self.__KNEIGHBORS_CLASSIFIER = 1
        self.__LOGISTIC_REGRESSION = 2
        self.__DECISION_TREE_CLASSIFIER = 3

        vertical1 = QVBoxLayout()
        self.setLayout(vertical1)
        self.setWindowTitle("Simulation Config")
        label_title1 = QLabel("Object Configuration")
        label_title1.setFont(QFont("Times", 10, QFont.Bold))
        
        label_title2 = QLabel("Target Configuration")
        label_title2.setFont(QFont("Times",10,QFont.Bold))

        label_title3 = QLabel("Simulation Configuration")
        label_title3.setFont(QFont("Times",10,QFont.Bold))

        # positions horizontal box
        positions = QHBoxLayout()
        # Size horizontal box
        size = QHBoxLayout()

        positions.addWidget(QLabel("X:"))
        self.pos_x = QLineEdit("200")
        positions.addWidget(self.pos_x)
        positions.addWidget(QLabel("Width:"))
        self.obj_width = QLineEdit("30")
        positions.addWidget(self.obj_width)
       

        size.addWidget(QLabel("Y:"))
        self.pos_y = QLineEdit("100")
        size.addWidget(self.pos_y)
        size.addWidget(QLabel("Height:"))
        self.obj_height = QLineEdit("30")
        size.addWidget(self.obj_height)

        
        
        # TARGET CONFIGURATION

        # positions horizontal box
        positions2 = QHBoxLayout()
        # Size horizontal box
        size2 = QHBoxLayout()

        positions2.addWidget(QLabel("X:"))
        self.pos_x2 = QLineEdit("230")
        positions2.addWidget(self.pos_x2)
        positions2.addWidget(QLabel("Width:"))
        self.obj_width2 = QLineEdit("30")
        positions2.addWidget(self.obj_width2)
       

        size2.addWidget(QLabel("Y:"))
        self.pos_y2 = QLineEdit("50")
        size2.addWidget(self.pos_y2)
        size2.addWidget(QLabel("Height:"))
        self.obj_height2 = QLineEdit("30")
        size2.addWidget(self.obj_height2)



        # SIMULATION CONFIGURATION
        
        conf = QHBoxLayout()

        conf.addWidget(QLabel("Delay(seconds):"))
        self.delay = QLineEdit("0.3")
        conf.addWidget(self.delay)

        combo = QHBoxLayout()

        combo.addWidget(QLabel("Pick a simulation Machine Learning Model:"))
        self.combobox = QComboBox()
        self.combobox.setObjectName(("comboBoxModels"))
        self.combobox.addItem("Random Forest Classifier")
        self.combobox.addItem("KNeighbors Classifier")
        self.combobox.addItem("Logistic Regression")
        self.combobox.addItem("Decision Tree Classifier")
        combo.addWidget(self.combobox)

        self.holdLogs = QCheckBox("Save Logs")

        buttons = QHBoxLayout()

        self.error_dialog = QErrorMessage()

        self.approvement = QPushButton("Okay")
        self.approvement.clicked.connect(self.approve)
        
        self.quit = QPushButton("Close")
        self.quit.clicked.connect(self.cancel)
        buttons.addWidget(self.approvement)
        buttons.addWidget(self.quit)

        vertical1.addWidget(label_title1)
        vertical1.addLayout(positions)
        vertical1.addLayout(size)
        vertical1.addWidget(label_title2)
        vertical1.addLayout(positions2)
        vertical1.addLayout(size2)
        vertical1.addWidget(label_title3)
        vertical1.addLayout(conf)
        vertical1.addLayout(combo)
        vertical1.addWidget(self.holdLogs)
        vertical1.addLayout(buttons)

    def cancel(self):
        self.destroy(destroyWindow=True)

    def __border(self):
        self.error_dialog.showMessage("Please give x greater than 50, lower than 700 and y lower than 500, greater than 50")

    def __numberFormat(self):
        self.error_dialog.showMessage("Please enter numbers to white fields.")

    def appro(self):
        #limit 700,500 (x,y)
        try:
            self.x1 = int(self.pos_x.text())
            self.y1 = int(self.pos_y.text())

            self.x2 = int(self.pos_x2.text())
            self.y2 = int(self.pos_y2.text())

            if self.x1>700 or self.x2>700 or self.x1<50 or self.x2<50 or self.y1>500 or self.y2>500 or self.y1<50 or self.y2<50:
                self.__border()  


            self.width = int(self.obj_width.text())
            self.height = int(self.obj_height.text())

            self.width2 = int(self.obj_width2.text())
            self.height2 = int(self.obj_height2.text())

            self.dela = float(self.delay.text())

            self.isChecked = self.holdLogs.isChecked()

            print("x1:{0}\nx2:{1}\ny1:{2}\ny2:{3}\nobj_width:{4}\nobj_height:{5}\nobj_width2:{6}\nobj_height2:{7}\ndelay:{8}\nisChecked:{9}"
            .format(self.x1,self.x2,self.y1,self.y2,self.width
            ,self.height,self.width2,self.height2,self.dela,self.isChecked))


            properties = ConfigProperties(self.x1,
            self.x2,self.y1,self.y2,self.width,self.height,self.width2,self.height2,self.dela,self.isChecked)
            index = self.combobox.currentIndex()
            if index == self.__RANDOM_FOREST_CLASSIFIER:
                properties._setModel(test.rf_model)
            elif index == self.__KNEIGHBORS_CLASSIFIER:
                properties._setModel(test.knn_model)
            elif index == self.__DECISION_TREE_CLASSIFIER:
                properties._setModel(test.dt_model)
            elif index == self.__LOGISTIC_REGRESSION:
                properties._setModel(test.lr_model)

            # QMessageBox().about(self,"Process","Simulation configuration successfully completed.")

            return properties

        except Exception as e:
            print(e)
            self.__numberFormat()
    def approve(self):
        #limit 700,500 (x,y)
        try:
            self.x1 = int(self.pos_x.text())
            self.y1 = int(self.pos_y.text())

            self.x2 = int(self.pos_x2.text())
            self.y2 = int(self.pos_y2.text())

            if self.x1>700 or self.x2>700 or self.x1<50 or self.x2<50 or self.y1>500 or self.y2>500 or self.y1<50 or self.y2<50:
                self.__border()  


            self.width = int(self.obj_width.text())
            self.height = int(self.obj_height.text())

            self.width2 = int(self.obj_width2.text())
            self.height2 = int(self.obj_height2.text())

            self.dela = float(self.delay.text())

            self.isChecked = self.holdLogs.isChecked()

            print("x1:{0}\nx2:{1}\ny1:{2}\ny2:{3}\nobj_width:{4}\nobj_height:{5}\nobj_width2:{6}\nobj_height2:{7}\ndelay:{8}\nisChecked:{9}"
            .format(self.x1,self.x2,self.y1,self.y2,self.width
            ,self.height,self.width2,self.height2,self.dela,self.isChecked))


            properties = ConfigProperties(self.x1,
            self.x2,self.y1,self.y2,self.width,self.height,self.width2,self.height2,self.dela,self.isChecked)
            index = self.combobox.currentIndex()
            if index == self.__RANDOM_FOREST_CLASSIFIER:
                properties._setModel(test.rf_model)
            elif index == self.__KNEIGHBORS_CLASSIFIER:
                properties._setModel(test.knn_model)
            elif index == self.__DECISION_TREE_CLASSIFIER:
                properties._setModel(test.dt_model)
            elif index == self.__LOGISTIC_REGRESSION:
                properties._setModel(test.lr_model)

            QMessageBox().about(self,"Process","Simulation configuration successfully completed.")

            return properties

        except Exception as e:
            print(e)
            self.__numberFormat()

class LogScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simulation LOGS")
        self.setGeometry(1000,200,400,500)

        vertical_box = QVBoxLayout()

        self.logList = QListWidget()
        vertical_box.addWidget(self.logList)
        self.button = QPushButton("Export")
        self.button.clicked.connect(self.export_log)
        vertical_box.addWidget(self.button)

        self.setLayout(vertical_box)


    def export_log(self):
        cout = self.logList.count()
        txt = ""
        for i in range(cout):
            txt+=self.logList.item(i).text()


        with open('log.txt','w') as f:
            f.write(txt)

        QMessageBox().about(self,'File','Logs successfully exported. Your log files name is log.txt.')
    
class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("EEG Imaginary Simulation")
        self.menu = self.menuBar() 
        self.setGeometry(600,150,800,600)
        
      
      
        self.config_screen = ConfigScreen()
        self.log_screen = LogScreen()

        system = self.menu.addMenu("System")
        start = self.menu.addMenu("Simulation")
        prepare = start.addAction("Prepare")
        prepare.triggered.connect(self.prepare_simulation)
        run = start.addAction("Run")
        run.triggered.connect(self.run_simulation)
        show_logs = start.addAction("Show Logs")
        show_logs.triggered.connect(self.show_logs)
        log = start.addAction("Export Logs")
        log.triggered.connect(self.export_log)
        config = system.addAction("Configuration")
        config.triggered.connect(self.open_config)
        exit = system.addAction("Exit")
        exit.triggered.connect(self.exitApp)
        help = self.menu.addMenu("Help")
        help.addAction("About")
        help.triggered.connect(self.text_help)


        self.obj =QPushButton("o",self)
        self.target = QPushButton("t",self)
        self.obj.setVisible(False)
        self.target.setVisible(False)
        
        self.finished_thread_count = 0
        self.finished_thread_label = QLineEdit(str(self.finished_thread_count))
        self.finished_thread_label.textChanged.connect(self.end_of_simulation)
        self.isPrepared = False
        self.error_dialog = QErrorMessage()
        
    def show_logs(self):
        self.log_screen.show()

    def exitApp(self):
        sys.exit()

    def closeEvent(self,cls):
        sys.exit()
        return super().closeEvent()
        
    def text_help(self):
        content = None
        with open('about.txt','r') as f:
            content = f.read()
        QMessageBox.about(self,"About",content)

    def export_log(self):
        if self.isPrepared:
            self.properties.log_output()
            QMessageBox().about(self,'File','Logs successfully exported. Your log files name is log.txt.')
        else:
            self.error_dialog.showMessage("First you have to prepare the simulation.")
        
        
    def end_of_simulation(self,main):
        cout = int(self.finished_thread_label.text())
        if cout == 2:
            QMessageBox().about(self,"Process","Simulation is over.")
            self.finished_thread_count = 0
            self.finished_thread_label.setText(str(self.finished_thread_count))

    def prepare_simulation(self):
        self.properties = self.config_screen.appro()

        self.obj.setVisible(True)
        self.target.setVisible(True)
        self.obj.setGeometry(self.properties.obj_x,self.properties.obj_y,self.properties.obj_width,self.properties.obj_height)
        self.target.setGeometry(self.properties.target_x,self.properties.target_y,self.properties.target_width,self.properties.target_height)
        
        test_simulation = test.UserDefinedTests([self.properties.obj_x,self.properties.obj_y,0]
        ,[self.properties.target_x,self.properties.target_y,0])
        test_simulation.setData(test.data1,test.data2,test.data3,test.data4,test.data5,test.data6)
        test_simulation.setModel(self.properties.model)
        test_simulation.prepareTest()
        test_simulation.move()
        self.properties.logs = test_simulation.results()

        # Move on x axis, x unit
        # Move on y axis, y unit
        self.move_x, self.move_y = test_simulation.x_y()
        print("Move x : ",self.move_x)
        print("Move y : ",self.move_y)

        self.isPrepared = True
        # print(self.obj.x())

    def __updateUInX(self,xcount):
        for _ in range(xcount):
            time.sleep(self.properties.delay)
            log ="Object moving on -x axis.\n"
            log+="Objects old position (x,y)->({0},{1})\n".format(self.obj.x(),self.obj.y())
            self.obj.move(self.obj.x()-1,self.obj.y())
            log+= "Objects updated position (x,y)->({0},{1})\n".format(self.obj.x(),self.obj.y())
            self.log_screen.logList.addItem(log)
        self.finished_thread_count += 1
        self.finished_thread_label.setText(str(self.finished_thread_count))
     
    def __updateUIX(self,xcount):
        for _ in range(xcount):
            time.sleep(self.properties.delay)
            log ="Object moving on +x axis.\n"
            log+="Objects old position (x,y)->({0},{1})\n".format(self.obj.x(),self.obj.y())
            self.obj.move(self.obj.x()+1,self.obj.y())
            log+= "Objects updated position (x,y)->({0},{1})\n".format(self.obj.x(),self.obj.y())
            self.log_screen.logList.addItem(log)
        self.finished_thread_count += 1        
        self.finished_thread_label.setText(str(self.finished_thread_count))

     
    def __updateUInY(self,ycount):
        for _ in range(ycount):
            time.sleep(self.properties.delay)
            log ="Object moving on -y axis.\n"
            log+="Objects old position (x,y)->({0},{1})\n".format(self.obj.x(),self.obj.y())
            self.obj.move(self.obj.x(),self.obj.y()-1)
            log+= "Objects updated position (x,y)->({0},{1})\n".format(self.obj.x(),self.obj.y())
            self.log_screen.logList.addItem(log)
        self.finished_thread_count += 1
        self.finished_thread_label.setText(str(self.finished_thread_count))

    
    def __updateUIY(self,ycount):
        for _ in range(ycount):
            time.sleep(self.properties.delay)
            log ="Object moving on +y axis.\n"
            log+="Objects old position (x,y)->({0},{1})\n".format(self.obj.x(),self.obj.y())
            self.obj.move(self.obj.x(),self.obj.y()+1)
            log+= "Objects updated position (x,y)->({0},{1})\n".format(self.obj.x(),self.obj.y())
            self.log_screen.logList.addItem(log)
        self.finished_thread_count +=1        
        self.finished_thread_label.setText(str(self.finished_thread_count))


   
    def run_simulation(self):

        if self.isPrepared:
            # Open log screen if user checked
            if self.properties.isChecked:
                self.log_screen.show()

            if self.move_x <0 :
                self.move_x *=-1
                _thread.start_new_thread(self.__updateUInX,(self.move_x,))
            else:
                _thread.start_new_thread(self.__updateUIX,(self.move_x,))
            
            if self.move_y <0:
                self.move_y *= -1
                _thread.start_new_thread(self.__updateUInY,(self.move_y,))
            else:
                _thread.start_new_thread(self.__updateUIY,(self.move_y,))
            
        else:
            self.error_dialog.showMessage("Prepare first to run simulation.")
            # print("Prepare first")

    def open_config(self):
        self.config_screen.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())