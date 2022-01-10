from __future__ import print_function
import os
import subprocess
import shutil

root_src_dir = r'C:\pdf' #Diretório com os arquivos a serem manipulados
root_dst_dir = 'C:\pdf2' #Diretório de saída dos arquivos

for root, dirs, files in os.walk(root_src_dir):
    dst_dir = root.replace(root_src_dir, root_dst_dir, 1)
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
        for file in files:
            src_file = os.path.join(root, file)
            dst_file = os.path.join(dst_dir ,file)
            if file.endswith(".pdf"):
                filename = os.path.join(root, file)
                print (filename)
                arg1= '-sOutputFile=' + file
                p = subprocess.Popen(['C:/Program Files/gs/gs9.55.0/bin/gswin64c.exe',
                                    '-sDEVICE=pdfwrite', 
                                    '-dCompatibilityLevel=1.4', 
                                    '-dPDFSETTINGS=/ebook', '-dNOPAUSE', 
                                    '-dBATCH', '-dQUIET', str(arg1), filename], 
                                    stdout=subprocess.PIPE)
                print (p.communicate())
                shutil.copy(file, dst_dir) #Realiza cópia do arquivo para o diretório correspondente na árvore
                os.remove(file) #Remove o arquivo após a cópia
