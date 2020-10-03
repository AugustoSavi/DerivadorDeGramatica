import time, threading, random
from tkinter import *

root = Tk()

#global derivacao
derivacao = {}

class Application():
    stop_threads = False
    
    def __init__(self):
        self.root = root
        self.tela()
        self.frame()
        self.inputs()
        self.buttons()
        root.mainloop()

    def tela(self):
        self.root.title('Derivador')
        self.root.geometry('700x350')
        self.root.resizable(False,False)

    # cria os frames para adcionar os componentes
    def frame(self):
        self.frame = Frame(self.root)
        self.frame.place(relx = 0 , rely = 0,relwidth = 1, relheight = 1)

    def buttons(self):
        #Bottao Clear 
        self.btnClear = Button(self.frame, text = 'Limpar Gramatica', command = self.clear)
        self.btnClear.place ( relx = 0.8, rely = 0.1, width = 130, height = 50)
        
        #Bottao Start 
        self.btnStart = Button(self.frame, text = 'Start', command = self.start)
        self.btnStart.place ( relx = 0.8, rely = 0.3, width = 130, height = 50)
        
        #Bottao Stop 
        self.btnStop = Button(self.frame, text = 'Stop', command = self.stop)
        self.btnStop.place ( relx = 0.8, rely = 0.5, width = 130, height = 50)

        #Bottao Input
        self.btnInput = Button(self.frame, text = 'Input', command = self.inputGramatica)
        self.btnInput.place( relx = 0.37, rely = 0.07, width = 80, height = 30)

        #Bottao Input
        self.btnInput = Button(self.frame, text = 'Input', command = self.inputGramatica)
        self.btnInput.place( relx = 0.37, rely = 0.07, width = 80, height = 30)

        #Exemplos
        #Bottao Exemplo1 
        self.btnExemplo1 = Button(self.frame, text = 'Exemplo 1', command = self.Exemplo1)
        self.btnExemplo1.place ( relx = 0.8, rely = 0.65, width = 130, height = 30)

        #Bottao Exemplo2 
        self.btnExemplo2 = Button(self.frame, text = 'Exemplo 2', command = self.Exemplo2)
        self.btnExemplo2.place ( relx = 0.8, rely = 0.75, width = 130, height = 30)
        
        #Bottao Exemplo3 
        self.btnExemplo3 = Button(self.frame, text = 'Exemplo3', command = self.Exemplo3)
        self.btnExemplo3.place ( relx = 0.8, rely = 0.85, width = 130, height = 30)
               


    def inputs(self):
        #input das gramticas
        self.labelInputGramatica = Label(self.frame, text = 'Informe a Gramatica (linha a linha):')
        self.labelInputGramatica.place(relx = 0.02, rely = 0.02)

        self.inputGramaticaText = Entry(self.frame, width = 25)
        self.inputGramaticaText.place(relx = 0.02, rely = 0.09)

        #input do Nao terminal inicial
        self.labelInputNaoTerminalInicial = Label(self.frame, text = 'Nao Terminal Inicial:')
        self.labelInputNaoTerminalInicial.place(relx = 0.50, rely = 0.09)

        self.inputNaoTerminalInicial = Entry(self.frame, width = 2)
        self.inputNaoTerminalInicial.place(relx = 0.7, rely = 0.09)

        #Gramatica
        self.labelGramatica = Label(self.frame, text = 'Gramatica:')
        self.labelGramatica.place(relx = 0.02, rely = 0.18)

        self.textBoxGramatica = Text(self.frame,height=13, width =30)
        self.textBoxGramatica.place(relx = 0.02, rely = 0.25)

        #Derivacao
        self.labelDerivacao = Label(self.frame, text = 'Derivacao:')
        self.labelDerivacao.place(relx = 0.4, rely = 0.18)

        self.textBoxDerivacao = Text(self.frame,height=13, width =30)
        self.textBoxDerivacao.place(relx = 0.4, rely = 0.25)


    def clear(self):
        global derivacao    
        derivacao.clear()
        self.inputNaoTerminalInicial.delete(0,END)
        #self.textBoxGramatica.config(state = 'normal')
        self.textBoxGramatica.delete('1.0',END)
        #self.textBoxGramatica.config(state = 'disabled')

        #self.textBoxDerivacao.config(state = 'normal')
        self.textBoxDerivacao.delete('1.0',END)
        #self.textBoxDerivacao.config(state = 'disabled')
            
            
    def start(self):
        self.startThreading = threading.Thread(target=self.derivacao)
        self.startThreading.start()
        
    def derivacao(self):
        self.textBoxDerivacao.delete('1.0',END)

        if (len(derivacao[self.inputNaoTerminalInicial.get()]) == 1):
            tamanhoVetor = 0
            
        else:
            tamanhoVetor = len(derivacao[self.inputNaoTerminalInicial.get()])-1


        gramaticaASerDerivada = derivacao[self.inputNaoTerminalInicial.get()][random.randint(0, tamanhoVetor)]
            

        self.textBoxDerivacao.insert(END,"{} = {} \n".format(self.inputNaoTerminalInicial.get(), gramaticaASerDerivada))

        while True:

            for letter in list(gramaticaASerDerivada):
                
                if (letter.isupper()):
                    gramaticaASerDerivada = gramaticaASerDerivada.replace(letter, derivacao[letter][random.randint(0, len(derivacao[letter])-1)] , 1)
                    self.textBoxDerivacao.insert(END,"{} = {} \n".format(self.inputNaoTerminalInicial.get(), gramaticaASerDerivada))
                    
            
            self.textBoxDerivacao.insert(END,"{} = {} \n".format(self.inputNaoTerminalInicial.get(), gramaticaASerDerivada))
            
            if (gramaticaASerDerivada.islower()):
                break
            if self.stop_threads: 
                #print("Loop Terminado")
                break


    def stop(self):
        self.stop_threads = True

    
    def inputGramatica(self):
        #self.textBoxGramatica.config(state = 'normal')
        self.textBoxGramatica.insert(END,"{}{}".format(self.inputGramaticaText.get(), '\n') )
        #self.textBoxGramatica.config(state = 'disabled')
        
        # Faz o split para dividir o terminal do nao terminal 
        inputDeGramatica = self.inputGramaticaText.get().split('=')

        # cria as variaveis nao terminal e faz stip para tirar os espacos
        naoTerminal = inputDeGramatica[0].strip()

        # faz o split pra criar os terminais
        terminais = inputDeGramatica[1].split('|')

        # tira os espacos dos terminais caso haja
        for x in range (len(terminais)):
            terminais[x] = terminais[x].strip()

        # Adciona os valores do array
        derivacao[naoTerminal] = terminais 

        #print(derivacao)

        self.inputGramaticaText.delete(0,END)


    def Exemplo1(self):
        self.textBoxGramatica.delete('1.0',END)
        self.textBoxDerivacao.delete('1.0',END)
        global derivacao    
        derivacao.clear()
        derivacao = {'S': ['aCb'], 'C': ['ab']}
        self.textBoxGramatica.insert(END,"S = aCb\nC = ab")
        self.inputNaoTerminalInicial.delete(0,END)
        self.inputNaoTerminalInicial.insert(END,'S')
    
    def Exemplo2(self):
        self.textBoxGramatica.delete('1.0',END)
        self.textBoxDerivacao.delete('1.0',END)
        global derivacao    
        derivacao.clear()
        derivacao = {'S': ['Cde', 'deA'], 'A': ['Ea', 'D', 'S'], 'C': ['ded'], 'D': ['deA', 'S'], 'E': ['ead']}
        self.textBoxGramatica.insert(END,"S = Cde|deA\nA = Ea|D|S\nC = ded\nD = deA|S\nE = ead")
        self.inputNaoTerminalInicial.delete(0,END)
        self.inputNaoTerminalInicial.insert(END,'S')

    def Exemplo3(self):
        self.textBoxGramatica.delete('1.0',END)
        self.textBoxDerivacao.delete('1.0',END)
        global derivacao    
        derivacao.clear()
        derivacao = {'S': ['ABC'], 'C': ['BaB', 'c'], 'B': ['b', 'bb'], 'A': ['a']}
        self.textBoxGramatica.insert(END,"S = ABC\nC = BaB|c\nB = b|bb\nA = a")
        self.inputNaoTerminalInicial.delete(0,END)
        self.inputNaoTerminalInicial.insert(END,'S')
        


Application()