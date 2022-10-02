#importação do tkinter
from tkinter import *

#criação da classe Application, aqui se cria os controles exibidos na tela
class Application:
    def __init__(self, master=None):
        #criação do primeiro conteiner, passando como parâmetro o pai(master)
        self.widget1 = Frame(master)
        #informamos que o gerenciador de geometria é o 'pack'
        self.widget1.pack()
        #usando o widget label para imprimir o texto "Primeiro widget"
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg.pack()
#instaciação da classe TK pro meio da variável 'root', 
#permite que os widgets sejam utilizados na aplicação
root = Tk()
#passando o 'root' para o construtor da class Application
Application(root)
#evento de loop para exibição da interface
root.mainloop()

'''
def main():

    return 0
if __name__ == "main": main()
'''