# -*- coding: utf-8 -*-
import random
import os
def sifreleme(dosyaYoluyapma,dosyaAdi, mesaj, enektar,  x):
    sifreli_mesaj=''
    nedir=''
    klasoryolu=dosyaYoluyapma
    os.chdir(klasoryolu)
    
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
    
    enektTar =  enektar      
     
    for i in mesaj:
        if i not in alfabe:
            sifreli_mesaj += i
        else:
            sifreli_mesaj += alfabe[(alfabe.index(i) + enektTar) % len(alfabe)]
    for i in x:
        if i not in alfabe:
            nedir += i
        else:
            nedir += alfabe[(alfabe.index(i) + enektTar) % len(alfabe)]
    
    
    f = open(str(dosyaAdi), "a")
    fBelge = open(str(dosyaAdi))
    fkontrol = fBelge.read()
    rakam1 = int(random.randint(10,100))
    rakam2 = int(random.randint(10,100))
    rakam3 = int(random.randint(10,100))
    rakam4 = int(random.randint(10,100))
    rakam5 = int(random.randint(10,100))
    rakam6 = int(random.randint(10,100))
    rakam7 = int(random.randint(10,100))
        
    if not fkontrol:
        fBelge.close()
        f.write( "*"+"?"+ str(rakam1) +"?"+ str(rakam5) +"?"+ str(rakam6) +"?"+"*" + str(nedir) + "_"+ str(sifreli_mesaj) +"*"+"?"+str(rakam4)+"?"+str(rakam7)+"?"+str(rakam2)+"?"+str(rakam3)+"?"+"*")
        f.close()
    else:
        fBelge.close()
        f.write( "\n*"+"?"+ str(rakam1) +"?"+ str(rakam5) +"?"+ str(rakam6) +"?"+"*" + str(nedir) + "_"+ str(sifreli_mesaj) +"*"+"?"+str(rakam4)+"?"+str(rakam7)+"?"+str(rakam2)+"?"+str(rakam3)+"?"+"*")
        f.close()
