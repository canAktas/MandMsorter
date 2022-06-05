import cv2
import numpy as np
import serial
import time
import hsv7Color
from ui_interface import *  # designer uretiyor
import sys


# Com(UART) Portlarını kontrol edip açık olan com portları 'COM3, COM2' şeklinde list of strings olarak döndürüyor
def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    ports = ['COM%s' % (i + 1) for i in range(256)]

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


# Eğer Arduino port'u açılmazsa exception atıyor
def showWarningMessage():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Warning)
    msg.setText("Arduino is not connected properly!")
    msg.setWindowTitle("Warning")

    x = msg.exec_()


# Sub thread - kameradan gelen görüntüleri dictonary üzerinde tutar
class WorkerThread(QRunnable):

    # Default constructor
    # ser: serial port ismi
    # GUI'de com port ve baud rate belirlenip worker thread üzerinde kullanılır
    def __init__(self, ser):
        super().__init__()

        self.arduinoData = ser
        self.pyCmd = 0

        # VideoCapture 0 : WebCam
        # cv2.CAP_DSHOW: Kamerayı main thread'de kullanmadığımız zaman kullanılır
        self.cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # Thread safe quit yapılabilmesi için döngüyü kontrol eder
        self.worker_thread_flag = True

        # Gelen renk görüntülerinin okunmasını durdurmak ve kontrol etmek için kullanılır
        self.interrupt_flag = False

        self.color_counter = {
            "pink": 0,
            "brown": 0,
            "red": 0,
            "orange": 0,
            "yellow": 0,
            "green": 0,
            "purple": 0
        }

    # Callback fonksiyon. Thread çağırıldığında otomatik olarak çalışır
    def run(self):

        # Sürekli olarak webcam görüntüsünü handle etme döngüsü
        while True:

            # Thread safe çıkış - break
            if not self.worker_thread_flag:
                break

            # Verilerin okunmasını durdurur - continue
            if self.interrupt_flag:
                continue

            # Kameradan gelen görüntü string olarak alınır
            self.pyCmd = hsv7Color.find_color(self.cam)
            pyCmd1 = str(self.pyCmd) + "\r"
            self.color_counter[self.pyCmd] = self.color_counter[self.pyCmd] + 1
            self.arduinoData.write(pyCmd1.encode())
            # print("message sent ", self.pyCmd)
            while (self.arduinoData.inWaiting() == 0):
                time.sleep(0.1)
            print("message received")
            dataPacket = self.arduinoData.readline()
            dataPacket = str(dataPacket, "utf-8")
            #Dictionary üzerindeki ilgili key'e ait veriyi bir arttırır (Counter)


    # Dictionary get - GUI Tarafından çağrılır
    def get_color_counter(self):
        return self.color_counter

        # Dictionary set as default - GUI Tarafından çağrılır

    def set_color_counter(self):
        self.color_counter = {
                "pink": 0,
                "brown": 0,
                "red": 0,
                "orange": 0,
                "yellow": 0,
                "green": 0,
                "empty": 0,
                "purple": 0
        }

    # Safe thread exit function - GUI Tarafından çağrılır
    def change_worker_thread_flag(self):
        self.worker_thread_flag = False

    # Main thread - GUI


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)

        # ui_interface dosyasındaki class çağrılır ve designer üstündeki bütün nesneler self.ui ismiyle kontrol edilir
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Minimize butona basıldığında showMinimized built in function çağrılır
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())

        # Close butona basıldığında close_window function çağrılır
        self.ui.close_window_button.clicked.connect(lambda: self.close_window())

        # restore_window_button butona basıldığında restore_or_maximize_window function çağrılır
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        # Arayüzü header kısmından tutup sürükle bırak yaptırmak için kullanılır
        self.ui.header_frame.mouseMoveEvent = self.moveWindow

        flags = Qt.WindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        # Combo box üzerinde kullanılabilir com port'ları sıralamak için kullanılır
        self.ui.comPortCombo.setEditable(True)
        self.ui.comPortCombo.addItem("Choose COM")
        self.listOfPorts = serial_ports()
        self.ui.comPortCombo.addItems(self.listOfPorts)

        # Com porta bağlı buton işlemleri
        self.ui.refreshComBtn.clicked.connect(self.refreshCOM)
        self.ui.comPortCombo.activated[str].connect(self.comboClicked)
        self.ui.comOpenBtn.clicked.connect(self.comOpen)
        self.ui.comCloseBtn.clicked.connect(self.comClose)

        # System işlerine bağlı buton işlemleri  - Kameradan gelen etiketleri GUI'de gösterme
        self.ui.start_button.clicked.connect(self.start_function)
        self.ui.interrupt_button.clicked.connect(self.interrupt_function)
        self.ui.move_on_button.clicked.connect(self.move_on_function)
        self.ui.stop_button.clicked.connect(self.stop_function)

        # Butonlara basılıp basılmamasını kontrol eder
        self.ui.comOpenBtn.setEnabled(False)
        self.ui.comCloseBtn.setEnabled(False)
        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setEnabled(False)
        self.ui.move_on_button.setEnabled(False)
        self.ui.interrupt_button.setEnabled(False)

        # Worker thread yalnızca bir kere çağrılabilir bu yüzden açık olup olmadığı kontrol edilmelidir
        self.threadActiveFlag = False

        self.default_color_dict = {
                "pink": 0,
                "brown": 0,
                "red": 0,
                "orange": 0,
                "yellow": 0,
                "green": 0,
                "purple": 0
        }

        self.show()

    # Eğer thread açıksa safe thread yaparak quit et
    # Eğer thread açık değilse direkt quit et
    def close_window(self):
        if self.threadActiveFlag:
            self.worker_thread.change_worker_thread_flag()
            cv2.destroyAllWindows()
        self.close()

    # Start butonuna basınca çalışır
    def start_function(self):
        self.ui.status_label.setText("WORKING!")

        # Thread açık değilse threadi başlat
        if not self.threadActiveFlag:
            self.worker_pool = QThreadPool.globalInstance()

            self.worker_thread = WorkerThread(
                self.ser)  # Thread'e argüman olarak başlatılan serial communication verilir

            self.worker_pool.start(self.worker_thread)
            self.threadActiveFlag = True

        self.worker_thread.interrupt_flag = False  # Interrupt kapatılır ve thread gelen renkleri saymaya başlar
        self.worker_thread.set_color_counter()  # Thread'e ait değerler sıfırlanır : baştan başlatma durumu
        self.result_function(self.default_color_dict)  # Sıfırlanmış değerler GUI'de gösterilir

        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setEnabled(True)
        self.ui.interrupt_button.setEnabled(True)

    # Interrupt butonuna basılınca çalışır
    def interrupt_function(self):
        self.color_dict = self.worker_thread.get_color_counter()  # Thread'in o zamana kadar okumuş olduğu değerleri alır
        self.result_function(self.color_dict)  # Alınan değerleri GUI'de gösterir
        self.ui.move_on_button.setEnabled(True)
        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setEnabled(False)
        self.worker_thread.interrupt_flag = True  # Interrupt flag'ini açar
        self.ui.status_label.setText("PAUSED!")

    # Move on butonuna basılınca çalışır
    def move_on_function(self):
        self.ui.start_button.setEnabled(False)
        self.ui.interrupt_button.setEnabled(True)
        self.ui.stop_button.setEnabled(True)
        self.ui.status_label.setText("WORKING!")
        self.worker_thread.interrupt_flag = False  # Interrupt flag'i kapatılır

    # Stop butonuna basılınca çalışır
    def stop_function(self):
        self.ui.status_label.setText("DONE!")
        self.ui.stop_button.setEnabled(False)
        self.ui.start_button.setEnabled(True)
        self.worker_thread.interrupt_flag = True
        self.color_dict = self.worker_thread.get_color_counter()  # Thread'in o zamana kadar okumuş olduğu değerleri alır
        self.result_function(self.color_dict)  # Alınan değerleri GUI'de gösterir

    # GUI'de alınan değerleri gösterir
    def result_function(self, color_dict):
        for key in color_dict:
            if key == "pink":
                self.ui.blue_counter.setText(str(color_dict[key]))

            elif key == "red":
                self.ui.red_counter.setText(str(color_dict[key]))
            elif key == "orange":
                self.ui.orange_counter.setText(str(color_dict[key]))
            elif key == "yellow":
                self.ui.yellow_counter.setText(str(color_dict[key]))
            elif key == "green":
                self.ui.green_counter.setText(str(color_dict[key]))

            elif key == "brown":
                self.ui.gray_counter.setText(str(color_dict[key]))
            else:
                self.ui.purple_counter.setText(str(color_dict[key]))

    # GUI'yı header üzerinden tutup hareket ettirirken kullanılır
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QIcon(":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QIcon(":/icons/icons/minimize-2.svg"))

    def moveWindow(self, e):
        if self.isMaximized() == False:
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos() + e.globalPos() - self.clickPosition)
                self.clickPosition = e.globalPos()
                e.accept()

    # COM PORT aktifleştirilir
    # Eğer arduinoya bağlanırken problem olursa except atar
    def comOpen(self):
        try:
            self.ui.comOpenBtn.setEnabled(False)
            self.ui.comCloseBtn.setEnabled(True)

            self.ui.start_button.setEnabled(True)
            self.BAUD = 115200
            self.ser = serial.Serial(self.PORT, self.BAUD)
            time.sleep(2)
        except:
            showWarningMessage()

    # COM PORT kapatılabilir
    def comClose(self):
        self.SerialPortClose()
        self.ui.comOpenBtn.setEnabled(True)
        self.ui.comCloseBtn.setEnabled(False)

    def SerialPortClose(self):
        self.ser.close()
        self.serialPortOpenFlag = False

    # Kullanılabilir com port'lar refresh edilir. GUI'deki combo Box üzerinde listelenir
    def refreshCOM(self):
        self.listOfPorts = serial_ports()
        comPortNames = [self.ui.comPortCombo.itemText(i) for i in range(self.ui.comPortCombo.count())]

        lenComPortNames = len(comPortNames) - 1
        lenListOfPorts = len(self.listOfPorts)

        lengthFlag = lenComPortNames >= lenListOfPorts

        if lengthFlag:
            forLength = lenComPortNames
        else:
            forLength = lenListOfPorts

        for i in range(forLength):
            if not lengthFlag:
                if self.listOfPorts[i] not in comPortNames:
                    self.ui.comPortCombo.addItem(self.listOfPorts[i])
            else:
                if comPortNames[i + 1] not in self.listOfPorts:
                    self.ui.comPortCombo.removeItem(i + 1)

    # Combo Box'a basıldığında seçilen değer alınır.
    def comboClicked(self, val):
        if not val == "Choose Com":
            self.PORT = val
            self.ui.selectedComPortLabel.setText(self.PORT)
            self.ui.comOpenBtn.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
