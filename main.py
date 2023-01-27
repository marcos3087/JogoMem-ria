
import sys, time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QIcon
from fmain import Ui_fmain
from random import shuffle
"""
    Projeto simples de um jogo da memória.
    o jogo possui 9 pares de cartas.

    É possível ajustar as imagens conforme o tema que desejar, basta colocar imagens com o nome img_{numero}.png na pasta Img

    independente de quantas imagens exitam na pasta, o jogo apresentará apenas as primeiras 9 para comparação.

    o jogo pode ser compilado em um exe e basta o exe e a pasta Img estarem na mesma pasta.
    
"""
class main(QMainWindow, Ui_fmain): 
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        #Inicia as variáveis.
        self.cartaSel1 = None
        self.bt1 = None
        self.cartaSel2 = None
        self.bt2 = None
        self.pos1 = None
        self.pos2 = None
        self.numeros_img = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
        self.reinicia()

        # inicia as ações em cada QPushButton
        self.bt_1.clicked.connect(lambda:self.clicou(self.bt_1))
        self.bt_2.clicked.connect(lambda:self.clicou(self.bt_2))
        self.bt_3.clicked.connect(lambda:self.clicou(self.bt_3))
        self.bt_4.clicked.connect(lambda:self.clicou(self.bt_4))
        self.bt_5.clicked.connect(lambda:self.clicou(self.bt_5))
        self.bt_6.clicked.connect(lambda:self.clicou(self.bt_6))
        self.bt_7.clicked.connect(lambda:self.clicou(self.bt_7))
        self.bt_8.clicked.connect(lambda:self.clicou(self.bt_8))
        self.bt_9.clicked.connect(lambda:self.clicou(self.bt_9))
        self.bt_10.clicked.connect(lambda:self.clicou(self.bt_10))
        self.bt_11.clicked.connect(lambda:self.clicou(self.bt_11))
        self.bt_12.clicked.connect(lambda:self.clicou(self.bt_12))
        self.bt_13.clicked.connect(lambda:self.clicou(self.bt_13))
        self.bt_14.clicked.connect(lambda:self.clicou(self.bt_14))
        self.bt_15.clicked.connect(lambda:self.clicou(self.bt_15))
        self.bt_16.clicked.connect(lambda:self.clicou(self.bt_16))
        self.bt_17.clicked.connect(lambda:self.clicou(self.bt_17))
        self.bt_18.clicked.connect(lambda:self.clicou(self.bt_18))
        self.btReset.clicked.connect(self.reinicia)

    #Método para virar a cara e compara a primeira e a segunda.
    #Quando iguais, mantem exibindo as imagens, quando diferente, volta para o verso do baralho
    #@param - bt, Objeto QPushButton que foi pressionado.
    def clicou(self, bt):
        nome = bt.objectName()
        aux = nome.split("_")
        pos = int(aux[1])
        carta = self.numeros_img[pos-1]
        if carta == 0:
            return

        #exibe a imagem da carta selecionada conforme o array
        bt.setIcon(QIcon('Img/img_'+ str(carta)+ '.png'))
        bt.repaint()
        time.sleep(1)
        #Se é o segundo clique, compara as duas cartas viradas.
        #Se forem iguais, mantem virada e aplica 0 no valor do array
        # se forem diferentes, volta a imagem para o verso do baralho
        if(self.cartaSel1 != None and self.cartaSel2==None):    
            self.cartaSel2 = carta
            self.bt2 = bt
            self.pos2 = pos-1
            if(self.cartaSel2 != self.cartaSel1):
                self.bt1.setIcon(QIcon('Img/baralho.png')) 
                self.bt2.setIcon(QIcon('Img/baralho.png')) 
            else:
                self.numeros_img[self.pos1] = 0
                self.numeros_img[self.pos2] = 0

           
        #quando é a primeira carta do par a ser clicada
        if(self.cartaSel1==None):
            self.cartaSel1 = carta
            self.bt1 = bt
            self.pos1 = pos-1
        #Depois do segundo clique, reinicia as variáveis de controle
        if(self.cartaSel1 != None and self.cartaSel2 != None):
            self.cartaSel1 = None
            self.bt1 = None
            self.cartaSel2 = None
            self.bt2 = None
            self.pos1 = None
            self.pos2 = None

        #a cara clique, valida se terminou de virar todas as cartas
        self.validaFim()

    #método para validar se o usuario terminou o jogo.
    # informa a conclusão e reinicia o painel;
    def validaFim(self):
        i=0
        todoszero = True
        while i<17:
            if(self.numeros_img[i] != 0):
                todoszero = False
            i+=1
        
        if(todoszero == True):
            QMessageBox.about(self,"Parabéns","Parabéns, você concluiu!")
            self.reinicia()

    #método para reiniciar o painel do jogo.
    #reinicia o vetor e embaralha seu conteúdo 3 vezes.
    #vira todas as caras para a imagem de verso do baralho.
    def reinicia(self):
        
        self.numeros_img = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
        shuffle(self.numeros_img)
        shuffle(self.numeros_img)
        shuffle(self.numeros_img)
        self.cartaSel1 = None
        self.bt1 = None
        self.cartaSel2 = None
        self.bt2 = None
        self.pos1 = None
        self.pos2 = None

        i=0
        while(i<18):
            bt = self.findChild(QtWidgets.QPushButton, "bt_"+str(i+1))
            bt.setIcon(QIcon('Img/baralho.png')) 
            i+=1


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = main()
    novo.show()
    sys.exit(qt.exec_())