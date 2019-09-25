from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time
import psutil


class CpuWorker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(int)

    @pyqtSlot()
    def procCounter(self):  # A slot takes no params
        while True:
            time.sleep(1)
            percent = psutil.cpu_percent()
            self.intReady.emit(percent)
        self.finished.emit()
