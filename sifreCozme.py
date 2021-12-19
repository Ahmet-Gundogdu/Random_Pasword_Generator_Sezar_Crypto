# -*- coding: utf-8 -*-
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ana_sayfa2 import *

def IlkaDIM(DosyaYlou, dosyaADDi,enektar):
    os.chdir(DosyaYlou)
    gasa = []   
    fBelgeAc = open(str(dosyaADDi), "r")
    x=0
    for i in fBelgeAc:
        mesajDizisi = i
        mesajDizisi0 = str(mesajDizisi)
        mesajDizisi1 = mesajDizisi0.split("*")
        mesajDizisi2 = mesajDizisi1[2]
        mesajDizisi2_1 = mesajDizisi2.split('_')
        mesajDizisi2_2 = mesajDizisi2_1[0]
        mesajDizisi2_3 = mesajDizisi2_1[1]
        mesajDizisi3 = enektar[x]
        gasa += sifrecozme(mesajDizisi2_2, mesajDizisi3, mesajDizisi2_3)
        x+=1
        
    fBelgeAc.close()    
    return gasa

def sifrecozme(sifreliMesaj, sifreliKey, sifreliX ):
    sifresizAciklama = ''
    sifresiz_mesaj = ''
    xasa = []
    alfabe = [
        'a','b','c','ç','d','e','f','g','ğ','h','ı','i','j',
        'k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z','w','x',
        '0','1','2','3','4','5','6','7','8','9',' ',
        'A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J',
        'K','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z','W','X',
        '"','é','!',"'",'£','^','#','+','$','%','½','&','/','{','(','[',')',']',
        '=','}','?',"~",'-','¨',',',';','`','.',':','<','>','|','´','æ','@',
        'a','b','c','ç','d','e','f','g','ğ','h','ı','i','j',
        'k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z','w','x',
        '0','1','2','3','4','5','6','7','8','9',' ',
        'A','B','C','Ç','D','E','F','G','Ğ','H','I','İ','J',
        'K','L','M','N','O','Ö','P','R','S','Ş','T','U','Ü','V','Y','Z','W','X',
        '"','é','!',"'",'£','^','#','+','$','%','½','&','/','{','(','[',')',']',
        '=','}','?',"~",'-','¨',',',';','`','.',':','<','>','|','´','æ','@'
        ] #37 + 10 + 31 + 31 + 1
         
    enektzar = sifreliKey       
      
    for i in sifreliMesaj:
        sifresiz_mesaj += alfabe[(alfabe.index(i) - int(enektzar)) % len(alfabe)]
    for x in sifreliX:
        sifresizAciklama += alfabe[(alfabe.index(x) - int(enektzar)) % len(alfabe)]
    xasa += [sifresiz_mesaj] + [sifresizAciklama]
    return xasa

