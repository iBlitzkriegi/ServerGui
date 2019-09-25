from PyQt5.QtCore import QThread, QObject, pyqtSignal, pyqtSlot
import time
import psutil
import os
from math import ceil


class GuiWorker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(int)

    @pyqtSlot()
    def procCounter(self):  # A slot takes no params
        while True:
            time.sleep(1)
            pid = os.getpid()
            py = psutil.Process(pid)
            memoryUse = py.memory_info()[0] / 2. ** 30
            self.intReady.emit(ceil(memoryUse))
        self.finished.emit()
