import sys
from ip_tracer import main
import time
from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from collections import deque

class Window(QtWidgets.QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initWindow()

    def initWindow(self):
        self.setWindowTitle(self.tr("IP TRACKER"))
        self.setFixedSize(1500, 800)
        self.buttonUI()

    def buttonUI(self):

        self.label1 = QtWidgets.QLabel()
        self.label2 = QtWidgets.QLabel()

        self.next_button = QtWidgets.QPushButton(self.tr("Next IP"))
        self.next_button.setFixedSize(120, 50)
        self.next_button.clicked.connect(self.controller.load_next_ip)

        self.label1.setFixedSize(120, 50)
        self.label2.setFixedSize(120, 50)

        self.view = QtWebEngineWidgets.QWebEngineView()
        self.view.setContentsMargins(50, 50, 50, 50)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        lay = QtWidgets.QHBoxLayout(central_widget)

        button_container = QtWidgets.QWidget()
        vlay = QtWidgets.QVBoxLayout(button_container)
        vlay.setSpacing(20)
        vlay.addStretch()
        vlay.addWidget(self.label1)
        vlay.addWidget(self.label2)
        vlay.addWidget(self.next_button)
        vlay.addStretch()
        lay.addWidget(button_container)
        lay.addWidget(self.view, stretch=1)




class AppController(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ip_queue = deque()
        self.ip_list = ['54.163.76.76', '184.169.250.146', '35.182.98.197', '54.207.159.35', '3.11.88.57', '13.246.114.251', '16.16.9.17', '43.204.105.75', '20.203.5.144', '124.222.228.228']
        self.window = None

    def start(self):
        self.window = Window(self)
        self.window.show()
        self.window.view.loadFinished.connect(self.on_load_finished)
        self.load_next_ip()
        

    def load_next_ip(self):
        if self.ip_queue:
            ip = self.ip_queue.popleft()
            data, coords = main(ip)
            try:
                self.window.label1.setText(f"{ip}")
                self.window.label2.setText(f"{coords}")
                self.window.view.setHtml(data.getvalue().decode())
            except:
                print("Gui not working!")
                sys.exit(1)

    def on_load_finished(self, success):
        if success:
            # self.load_next_ip()
            pass

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    controller = AppController()
    controller.ip_queue.extend(controller.ip_list)
    controller.start()
    sys.exit(App.exec())
        