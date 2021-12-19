
# -*- coding: utf-8 -*-
#---------------------------------------------------------------------
#----------------Gerekli verilerin include edilmesi-------------------
#---------------------------------------------------------------------
import os
import sys
import sifrelEme
import sifreCozme
import rastgeleSifre
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ana_sayfa2 import *
from anahtarpopup import *


#---------------------------------------------------------------------
#-----------------------Pencereyi Çalıştırma--------------------------
#---------------------------------------------------------------------

Uygulama = QApplication(sys.argv)
penAna = QMainWindow()
ui = Ui_sifreOlusturSifreleKaydet()
ui.setupUi(penAna)
penAna.show()

Popup = QApplication(sys.argv)
penuyari = QDialog()
pop = Ui_enektar_popup()
pop.setupUi(penuyari)
#---------------------------------------------------------------------
#-------------------------Fonksiyonlar--------------------------------
#---------------------------------------------------------------------


def OLUSTUR():

    try:
        _sifreUzunlugu = int(ui.sifreUzunluguLine.text())
        pass
    except:
        pass
    
    if ui.turkceKarakterChbox.isChecked():
        trKrkter = True
    else:
        trKrkter = False
        
    if ui.rakamChbox.isChecked():
        rkmlr = True
    else:
        rkmlr = False
        
    if ui.ozelKarakterChbox.isChecked():
        ozlKrkter = True
    else:
        ozlKrkter = False
    try:
        sonuc = rastgeleSifre.sifreleOlustur(int(_sifreUzunlugu) , bool(rkmlr) , bool(ozlKrkter), bool(trKrkter))
        ui.sifreCiktisi.setText(sonuc)
        ui.hata_labeli.setText("")
        pass
    except:
        ui.hata_labeli.setText("Oluşturuken hata meydana geldi. Uzunluğa dikkat ediniz!")
        pass
    

def DOSYAyolu ():
    global dosyayolu, yol, dosyaadi, klasoryolu
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    dosyayolu, _ = QFileDialog.getOpenFileName(filter="*.txt")
    yol = dosyayolu.split("/")
    dosyaadi = yol[-1]
    yol.remove(dosyaadi)
    klasoryolu = str("\\".join(yol))
    ui.dosyaYoluLink.setText(dosyayolu)


def SIFREkaydet():
    try:
        _sifreAciklama = str( ui.sifreAciklamaLine.text() )
        ui.hata_labeli.setText("")
        pass
    except :
        ui.hata_labeli.setText("Şifre açıklaması boş!")
        pass
    try:
        _sifrelenecekMesaj = str( ui.sifresizMesajLine.text() )
        ui.hata_labeli.setText("")
        pass
    except :
        ui.hata_labeli.setText("Şifrelenecek mesaj boş!")
        pass
    try:
        _sifreEnektar = int(ui.sifreAnahtar.text())
        sifrelEme.sifreleme( str(klasoryolu) , str(dosyaadi) , str(_sifrelenecekMesaj), int(_sifreEnektar) , str(_sifreAciklama))
        ui.hata_labeli.setText("")
        pass
    except :
        ui.hata_labeli.setText("Anahtar boş veya rakam girmediniz!")
        pass
    ui.sifresizMesajLine.clear()
    ui.sifreAciklamaLine.clear()
    ui.sifreAnahtar.clear()


def COZME2():
    penuyari.close()
    if len(anahtar_dizisi) == 0:
        ui.hata_labeli.setText("Anahtar/lar'ı girmediniz!")
    else:
        zxz = [sifreCozme.IlkaDIM(klasoryolu, dosyaadi , anahtar_dizisi)]
    ui.sifreListelemeTablo.clear()
    ui.sifreListelemeTablo.setHorizontalHeaderLabels(("Açıklama", "Metin"))
    ui.sifreListelemeTablo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    
    girilen_key_sayisi['key'] = 0
    pop.enektar_line.setEnabled(True)
    try:
        for satirIndeks , satirVeri in enumerate(zxz) :
            for sutunIndeks, sutunVerı in enumerate(satirVeri):
                ui.sifreListelemeTablo.setItem(satirIndeks , sutunIndeks , QTableWidgetItem(str(sutunVerı))) 
        pass
    except:
        ui.hata_labeli.setText("Şifre çözümünde hata meydana geldi!")
        pass
    ui.hata_labeli.setText("Tekrar listelemek için programı kapatıp açınız!")
    pop.enektar_line.clear()
    
    


def COZME():
    global kac_adet_keyx, girilen_key_sayisi, anahtar_dizisi
    anahtar_dizisi=[]
    girilen_key_sayisi= {'key':0}
    kac_adet_keyx = 0
    penuyari.show()
    try:
        fBzaelgeAc = open(str(dosyaadi), "r")
        for iii in fBzaelgeAc:
            kac_adet_keyx += 1
        ui.hata_labeli.setText("")
        pass
    except:
        penuyari.close()
        ui.hata_labeli.setText("Dosya yolu seçmediniz!")
        pass
    
    pop.aciklama.setText("{} adet anahtar girmeniz gerekiyor.".format(kac_adet_keyx))
    pop.label.setText("0 adet anahtar girdiniz.")
    pop.enektar_devam.clicked.connect(COZME1)


def COZME1():
    girilen_key_sayisi['key'] += 1
    try:
        anahtar_dizisi.append(int(pop.enektar_line.text()))
        pass
    except:
        girilen_key_sayisi['key'] -=1

        pass
    pop.aciklama.setText("{} adet anahtar girmeniz gerekiyor.".format(kac_adet_keyx))
    pop.label.setText("{} adet anahtar girdiniz.".format( girilen_key_sayisi['key']) )
    if len(pop.enektar_line.text()) == 0:
        COZME1
    pop.enektar_line.clear()
    if kac_adet_keyx > girilen_key_sayisi['key'] :
        pop.enektar_devam.clicked.connect(COZME1)
    else:
        pop.label.setText("Son adım")
        pop.enektar_line.setEnabled(False)
        pop.enektar_devam.clicked.connect(COZME2)


#---------------------------------------------------------------------
#-------------------------Buton Bağlantıları--------------------------
#---------------------------------------------------------------------


ui.sifreOlusturButon.clicked.connect(OLUSTUR)
ui.dosyaYoluButon.clicked.connect(DOSYAyolu)
ui.sifreKaydetButon.clicked.connect(SIFREkaydet)
ui.sifreGosterButon.clicked.connect(COZME)


#---------------------------------------------------------------------
#-------------------------EXİT----------------------------------------
#---------------------------------------------------------------------

sys.exit(Uygulama.exec_())
