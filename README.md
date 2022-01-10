# CompressorPDF
Script para compressão de arquivos em pdf.

O script recria a árvore de diretórios já existente.

Tecnologias utilizadas: Python + Ghostscript

<br>root_src_dir - Diretório com os arquivos a serem manipulados
<br>root_dst_dir - Diretório de saída dos arquivos

Para alterar a qualidade/compressão dos arquivos o parâmetro -dPDFSETTINGS= pode receber os seguintes valores:
<br>/screen - baixa resolução
<br>/ebook - média resolução
<br>/printer - saída similar ao Acrobat Distiller "Print Optimized"
<br>/prepress - saída similar ao Acrobat Distiller "Prepress Optimized"
<br><br>Outras configurações podem ser encontradas em https://www.ghostscript.com/doc/9.54.0/VectorDevices.htm
