# -*- coding: utf-8 -*-
import random

def sifreleOlustur(uzunluk, rakam, specialkarakter, turkceKaraktermi):
    xux = int(uzunluk)
    sayiOlsunmu = bool(rakam)
    ozelKarakterOlsunMu = bool(specialkarakter)
    trOlsunmu = bool(turkceKaraktermi)
    alfabe = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','r','s','t','u','v','y','z','w','x',
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','R','S','T','U','V','Y','Z','W','X' 
        ]
    turkceKarakter = [
        'ç','ğ','ı','ö','ş','ü','Ç','Ğ','İ','Ö','Ş','Ü',
        ]
    rakamlar = [
        '0','1','2','3','4','5','6','7','8','9'
        ]
    ozelKarakterler = [
        '"','é','!',"'",'£','^','#','+','$','%','½','&','_',
        '/','{','(','[',')',']','=','}','?',"~",'_','-','*',
        '¨',',',';','`','.',':','<','>','|','´','*','æ','@'
        ]
    sifreliMesaj = ''
    for i in range(0, xux):
        if ozelKarakterOlsunMu == True and sayiOlsunmu == True and trOlsunmu == True:
            yeniAlfabe = alfabe + rakamlar + ozelKarakterler + turkceKarakter
            rastgeleAlfabe = int(random.randint(1,len(yeniAlfabe)-1))
            sifreliMesaj += str(yeniAlfabe[rastgeleAlfabe])
            
        elif ozelKarakterOlsunMu == True and sayiOlsunmu == True and trOlsunmu == False :
            yeniAlfabe = alfabe + rakamlar + ozelKarakterler
            rastgeleAlfabe = int(random.randint(1,len(yeniAlfabe)-1))
            sifreliMesaj += str(yeniAlfabe[rastgeleAlfabe])    
            
        elif ozelKarakterOlsunMu == False and sayiOlsunmu == True and trOlsunmu == True :
            yeniAlfabe = alfabe + rakamlar + turkceKarakter
            rastgeleAlfabe = int(random.randint(1,len(yeniAlfabe)-1))
            sifreliMesaj += str(yeniAlfabe[rastgeleAlfabe])    
            
        elif ozelKarakterOlsunMu == False and sayiOlsunmu == True and trOlsunmu == False:
            yeniAlfabe = alfabe + rakamlar 
            rastgeleAlfabe = int(random.randint(1,len(yeniAlfabe)-1))
            sifreliMesaj += str(yeniAlfabe[rastgeleAlfabe]) 
            
        elif ozelKarakterOlsunMu == True and sayiOlsunmu == False and trOlsunmu == True :
            yeniAlfabe = alfabe + ozelKarakterler + turkceKarakter
            rastgeleAlfabe = int(random.randint(1,len(yeniAlfabe)-1))
            sifreliMesaj += str(yeniAlfabe[rastgeleAlfabe]) 
            
        elif ozelKarakterOlsunMu == True and sayiOlsunmu == False and trOlsunmu == False:
            yeniAlfabe = alfabe  + ozelKarakterler
            rastgeleAlfabe = int(random.randint(1,len(yeniAlfabe)-1))
            sifreliMesaj += str(yeniAlfabe[rastgeleAlfabe])
            
        elif ozelKarakterOlsunMu == False and sayiOlsunmu == False and trOlsunmu == True:
             yeniAlfabe = alfabe  + turkceKarakter
             rastgeleAlfabe = int(random.randint(1,len(yeniAlfabe)-1))
             sifreliMesaj += str(yeniAlfabe[rastgeleAlfabe])   
        
        elif ozelKarakterOlsunMu == False and sayiOlsunmu == False and trOlsunmu == False: 
            yeniAlfabe = alfabe
            rastgeleAlfabe = int(random.randint(1,len(yeniAlfabe)-1))
            sifreliMesaj += str(yeniAlfabe[rastgeleAlfabe])

    return sifreliMesaj

