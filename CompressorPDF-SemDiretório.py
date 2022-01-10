from __future__ import print_function
import os
import subprocess

for root, dirs, files in os.walk("C:\comp"): #Diretório onde será realizada a compressão
    for file in files:
        if file.endswith(".pdf"):
            filename = os.path.join(root, file)
            print (filename)
            arg1= '-sOutputFile=' + "c" +  file #Adiciona a letra c ao nome de cada arquivo gerado
            p = subprocess.Popen(['C:/Program Files/gs/gs9.55.0/bin/gswin64c.exe',
                                  '-sDEVICE=pdfwrite', 
                                  '-dCompatibilityLevel=1.4', 
                                  '-dPDFSETTINGS=/ebook', '-dNOPAUSE', 
                                  '-dBATCH', '-dQUIET', str(arg1), filename], 
                                 stdout=subprocess.PIPE)
            print (p.communicate())
