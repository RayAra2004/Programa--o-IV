#importação do tkinter
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer, text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font= self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificarSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    def verificarSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "raynan" and senha == "raynan":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

root = Tk()
Application(root)
root.mainloop()
'''
#criação da classe Application, aqui se cria os controles exibidos na tela
class Application:
    def __init__(self, master=None):
        #criação do primeiro conteiner, passando como parâmetro o pai(master)
        self.widget1 = Frame(master)
        #informamos que o gerenciador de geometria é o 'pack'
        self.widget1.pack()
        #usando o widget label para imprimir o texto "Primeiro widget"
        self.msg = Label(self.widget1, text="Primeiro widget")
        #alterando "font" do elemento 'msg'
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        #exibindo conteúdo na tela por meio do gerenciador 'pack'
        self.msg.pack()

        #criando botão e adicionando ao 'widget1'
        self.sair = Button(self.widget1)
        #adicionando text "Sair" ao botão
        self.sair["text"] = "Sair"
        #aleterando font do botão
        self.sair["font"] = ("Calibri", "10")
        #definindo tamanho do botão
        self.sair["width"] = 10
        #adicionado comando ao botão
        self.sair["command"] = self.widget1.quit
        #exibindo conteúdo na tela por meio do gerenciador 'pack'
        #e posicionado botão
        self.sair.pack(side=RIGHT)

        self.clique = Button(self.widget1)
        self.clique["text"] = "Clique aqui"
        self.clique["font"] = ("Calibri", "9")
        self.clique["width"] = 10
        #chama a função 'mudarTexto': caso 1
        #self.clique.bind("<Button-1>", self.mudarTexto)
        #ou : caso 2
        self.clique["command"] = self.mudarTexto
        self.clique.pack()

    def mudarTexto(self): #event --> caso 1
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"

        
            Width – Largura do widget;
            Height – Altura do widget;
            Text – Texto a ser exibido no widget;
            Font – Família da fonte do texto;
            Fg – Cor do texto do widget;
            Bg – Cor de fundo do widget;
            Side – Define em que lado o widget se posicionará (Left, Right, Top, Bottom).
        
#instaciação da classe TK pro meio da variável 'root', 
#permite que os widgets sejam utilizados na aplicação
root = Tk()
#passando o 'root' para o construtor da class Application
Application(root)
#evento de loop para exibição da interface
root.mainloop()
'''