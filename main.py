
import sys
import cv2
from PyQt5 import QtWidgets, QtGui , QtCore
from arayuz import Ui_MainWindow
from hucre_sayim import hucre_say

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("""
    QMainWindow {
        background-color: #f0f0f0;
    }
    QPushButton {
        background-color: #4CAF50; 
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 6px;
    }
    QLabel#lbl_sayi {
        font-size: 18px;
        color: #333;
    }
""")


        
        self.ui.btn_sec.clicked.connect(self.dosya_sec)

    def dosya_sec(self):
        dosya, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Görsel Seç", "", "Görüntü Dosyaları (*.png *.jpg *.bmp)")
        if dosya:
            try:
               
                sayi, img = hucre_say(dosya)


                img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, ch = img_rgb.shape
                bytes_per_line = ch * w


                qimg = QtGui.QImage(img_rgb.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)

           
                self.ui.lbl_resim.setPixmap(QtGui.QPixmap.fromImage(qimg).scaled(
                    self.ui.lbl_resim.width(),
                    self.ui.lbl_resim.height(),
                    QtCore.Qt.KeepAspectRatio))

             
                self.ui.lbl_sayi.setText(f"Hücre Sayısı: {sayi}")

            except Exception as e:
                QtWidgets.QMessageBox.warning(self, "Hata", f"Bir hata oluştu:\n{str(e)}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    pencere = MainApp()
    pencere.show()
    sys.exit(app.exec_())
