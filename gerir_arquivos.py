#!/usr/bin/env python3
#-*-coding:utf8;-*-
#qpy:console
 
"""
Criado por: @DjEdu28
em: 13/02/20

• Organiza arquivos
  >> move e/ou renomeia
  
• une arquivos
  >> para uma pasta com arquivos fragmentados 
  >> arquivos sequenciados segundo padrão: 
        ".*-\d+\..+"
        exemplo: nome-1.mp4

criado com o objetivo de unir arquivos de vídeos que estávamos fragmentados
"""

#Importando Bibliotecas
import os     #usado: os.system,os.chdir
import shutil #usado: shutil.move
#from datetime import datetime



class Dj_vid_Uniao:
    
    ## pode editar vvvvvv
    djend_busca='./' #pasta de busca
    nova_pasta ='./' #pasta pra onde vai ser movido

    def verificar(self, file):
        # TRATAMENTO DE DADOS
        
        # Gerando novo nome pelo Padrão dos nomes dos pacotes do G1
        # padrão: bla...blabla-X.ts; com X um número inteiro
        d = str(file).split(".")[0]
        d1   = d[-2:-1]
        nome = d[-1:]+"."+str(file).split(".")[1]
        if d1 != "-": nome = d1+nome
        print(nome)
        self.mover(self.djend_busca+file, self.nova_pasta + nome)
    
    ## pode editar ^^^^^
    
    
    ##  nao editar vvvvv    
    #    extensions = ['jpg', 'jpeg', 'JPG', 'JPEG','webp']
    extensions = ['ts', 'mp4', 'avi', 'flv', 'txt']
    extension  = ""
    
    arquivos=[]
    
    def buscar_em(self,pasta):
        self.djend_busca=pasta
        if self.djend_busca[-1]!='/': self.djend_busca +='/'
        os.chdir(self.djend_busca)
        
    def mover_para(self,pasta):
        self.nova_pasta=pasta
        if self.nova_pasta[-1]!='/': self.nova_pasta +='/'

    def listar_arquivos(self):
        print("pasta de busca:",self.djend_busca)
        #listando arquivos
        self.arquivos = [
            filename for filename in os.listdir(self.djend_busca) if ( any(filename.endswith(ext) for ext in self.extensions))
        ]
        print(f"são {len(self.arquivos)} arquivos")
        if len(self.arquivos)==0:
            print("\n\nSaindo pois não tem arquivos que atende as restrições")
            exit(1)#erro 404)
        
    def mover(self,de,para):
        # move ou renomeia
        #movendo(de_pasta+nome_arquivo,para_pasta+nome_arquivo)
        shutil.move(de,para)

    def organizar(self):
        print("pasta pra onde vai:",self.nova_pasta)        
        input('organizar: tecle enter para continuar')
        for filename in self.arquivos:
            print(filename, end=' >> ')
            self.verificar(filename)
        print("organizar: concluído")
        print("\n\n")

    def juntar(self):
        self.extension = str(self.arquivos[1]).split(".")[-1]
                
        input('união: tecle enter para continuar')
        
        ark_ok=f"1.{self.extension}" #nome do arquivo Unido (to dizendo que é o primeiro pedaço)
        for numero in range(2,len(self.arquivos)+1):
            nome=f"{numero}.{self.extension}" #nome do arquivo pedaço
            print(nome, end='\r')
            self.unir(nome,ark_ok)
        print("união: concluído")
        print("\n\n")
        
    def unir(self,pedaco,base):
        os.system(f"cat {pedaco} >> {base}")
        
####################################
#----------------------------------#
####################################

DJ = Dj_vid_Uniao() # criando obj DJ


#Definindo pastas
dj_endereco_busca = './modelo_test'
DJ.buscar_em(dj_endereco_busca)

#DJ.mover_para('./nova_pasta/')


# iniciando processo

DJ.listar_arquivos()

DJ.organizar()

DJ.juntar()

#FIM