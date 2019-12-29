# -*- coding: utf-8 -*-


import pdftotext
import os
#Pergunta qual o diretorio
print("Qual o diretorio")
caminho = raw_input()
arquivos = os.listdir(caminho)

#lista os arquivos do diretorio
for arquivo in arquivos:
    print(arquivo)

#pergunta qual arquivo (provisorio, intencao é fazer com todos)
arquivo = raw_input("Qual arquivo vai converter ")
#carrega arquivo pdf
def carregaConverte(carminho, arquivo):
    with open(caminho+arquivo, "rb") as f:
        pdf = pdftotext.PDF(f)
        arquivo = arquivo.replace('.pdf', '')
    with open(caminho+arquivo+'.txt', 'w') as f:
        f.write("\n\n".join(pdf).encode('utf-8'))

carregaConverte(caminho,arquivo)

escolha = raw_input("Quer converter mais ")
while escolha == "sim":
    arquivo = raw_input("Qual arquivo ")
    carregaConverte(caminho,arquivo)
    escolha = raw_input("Quer converter mais ")
else:
    print("fim!")