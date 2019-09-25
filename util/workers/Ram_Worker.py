from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time
import psutil


class RamWorker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(int)

    @pyqtSlot()
    def procCounter(self):  # A slot takes no params
        while True:
            time.sleep(1)
            memory = psutil.virtual_memory()[2]
            self.intReady.emit(memory)
        self.finished.emit()
