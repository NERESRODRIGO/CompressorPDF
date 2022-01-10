from __future__ import print_function
import os
import subprocess

for root, dirs, files in os.walk("C:\comp"): #Diretório onde será realizada a compressão
    for file in files:
        if file.endswith(".pdf"):
            filename = os.path.join(root, file)
            print (filename)
            arg1= '-sOutputFile=' + "c" +  file #Adiciona a letra c ao nome de cada arquivo gerado
            #Para alterar a qualidade/compressão do arquivo o parâmetro -dPDFSETTINGS= pode receber os seguintes valores
                #/screen - baixa resolução
                #/ebook - média resolução
                #/printer - saída similar ao Acrobat Distiller "Print Optimized"
                #/prepress - saída similar ao Acrobat Distiller "Prepress Optimized"
                #Outras configurações podem ser encontradas em https://www.ghostscript.com/doc/9.54.0/VectorDevices.htm
            p = subprocess.Popen(['C:/Program Files/gs/gs9.55.0/bin/gswin64c.exe',
                                  '-sDEVICE=pdfwrite', 
                                  '-dCompatibilityLevel=1.4', 
                                  '-dPDFSETTINGS=/ebook', '-dNOPAUSE', 
                                  '-dBATCH', '-dQUIET', str(arg1), filename], 
                                 stdout=subprocess.PIPE)
            print (p.communicate())