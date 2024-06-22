import tkinter as tk
from tkinter import messagebox
import mysql.connector
from datetime import datetime

#inicia conexao com banco
connector = mysql.connector.connect(
    host='127.0.0.1', user='root', password='', database='pizzaria'
)

#funçao para salvar os dados
def salvar_pedido(tamanho, quantidade, valor_total):
    cr = connector.cursor()
    cr.execute('INSERT INTO pedidos (data_pedido, tamanho, quantidade, valor_total) VALUES (%s, %s, %s, %s)', (datetime.now(), tamanho, quantidade, valor_total))
    connector.commit()

#funcao que salva o cliente
def salvar_cliente(nome, telefone, email):
    cr = connector.cursor()
    cr.execute('INSERT INTO clientes (nome, telefone, email) VALUES (%s, %s, %s)', (nome, telefone, email))
    connector.commit()


def tela_cliente():
    ## cadastro de cliente ##

    janela_cadastro_cliente = tk.Tk()
    janela_cadastro_cliente.title('Cadastro de clientes')
    
    
    framejanela_cadastro_cliente = tk.Frame(janela_cadastro_cliente, border='5', background='blue')
    framejanela_cadastro_cliente.grid(row=0, column=0, padx=5, pady=5)
    #nome
    label_cliente_nome = tk.Label(framejanela_cadastro_cliente,text='Nome: ')
    input_cliente_nome = tk.Entry(framejanela_cadastro_cliente)
    label_cliente_nome.grid()
    input_cliente_nome.grid()

    #telefone
    label_cliente_telefone = tk.Label(framejanela_cadastro_cliente,text='Telefone: ')
    input_cliente_telefone = tk.Entry(framejanela_cadastro_cliente)
    label_cliente_telefone.grid()
    input_cliente_telefone.grid()

    #email
    label_cliente_email = tk.Label(framejanela_cadastro_cliente,text='E-mail: ')
    input_cliente_email = tk.Entry(framejanela_cadastro_cliente)
    label_cliente_email.grid()
    input_cliente_email.grid()
    

    #desmarca os entrys do cliente apos responder a caixa de dialogo
    def desmarcar_cliente():
        input_cliente_nome.delete(0, 'end')
        input_cliente_telefone.delete(0, 'end')
        input_cliente_email.delete(0, 'end')
        
    #caixa de dialogo para salvar ou nao o cliente
    def confirmar_cliente():
        resposta = messagebox.askquestion(message=f"Deseja adicionar o novo cliente?")
        if resposta == 'yes':
            salvar_cliente(input_cliente_nome.get(), input_cliente_telefone.get(), input_cliente_email.get())
            print('SALVOU NO BANCO')
            desmarcar_cliente()
        else:
            desmarcar_cliente()
            print('nao salvou nada')
    
    #botao para cadastrar o cliente
    btn_cliente_enviar = tk.Button(text='Cadastrar', command=confirmar_cliente)
    btn_cliente_enviar.grid()

    ## fim cadastro de cliente ##

    ## INICIO PEDIDO ##
def tela_pedido():
    janela_pedidos = tk.Tk()
    janela_pedidos.title('Pedidos')
    janela_pedidos.geometry('300x350')
    #variaveis utilizadas
    tamanhos = {'Pequena': 15, 'Média': 22, 'Grande': 28}
    ingredientes = {"Queijo Extra": 2.00, "Pepperoni": 3.00, "Bacon": 4.00}
    ingredientes_lista = ["Queijo Extra", 'Pepperoni', 'Bacon']
    tamanho_selecionado = ''
    ingrediente_selecionado = []
    variavel = tk.StringVar()
    variavel.set('Grande')

    #calcula os valores das pizzas e ingredientes
    def calcular():
        global qtd, valor_total
        tamanho = variavel.get()
        qtd = int(input.get())

        #pega os ingredientes marcados
        ingredientes_marcados = []
        for nome, estado in enumerate(lista_checks):
            estado_selecionado = estado.get()
            if estado_selecionado == 1:#se for 1 esta marcado
                ingredientes_marcados.append(ingredientes_lista[nome])
            
        preco_un = tamanhos[tamanho]
        
        #pega todos os valores dos ingredientes marcados
        total_ingredientes = 0
        for i in ingredientes_marcados:
            total_ingredientes += ingredientes[i]
        
        total_unidade = preco_un * qtd
        valor_total = total_unidade + total_ingredientes
        
        label_resultado.config(text=f'Tamanho: {tamanho} - R${total_unidade:.2f} \n Ingredientes: \n {ingredientes_marcados} - R${total_ingredientes:.2f} \n Valor total: R${valor_total:.2f} ')

    #função para desmarcar as informações nos messageboxes
    def desmarcar(a, b):
        a.delete(0, 'end')
        b.config(text='--')
        for i in (lista_checks):
            if i.get() == 1:
                i.set(0)

    #caixa de dialogo
    def confirmar():
        calcular()
        #chama o messagebox
        resposta = messagebox.askquestion(message=f"Pedido com valor final de R${valor_total:.2f}.\n Deseja confirmar o pedido?")
        if resposta == 'yes':
            salvar_pedido(variavel.get(), qtd, valor_total)
            desmarcar(input, label_resultado)
        else:
            desmarcar(input, label_resultado)

    frame = tk.Frame(janela_pedidos, border='5', background='blue')
    frame.grid(row=0, column=0, padx=5, pady=5)

    frame2 = tk.Frame(janela_pedidos, background='lightcoral')
    frame2.grid(padx=5, pady=5)

    frame3 = tk.Frame(janela_pedidos, bg='lightblue')
    frame3.grid()

    label_inicio = tk.Label(frame, text='Escolha o tamanho da pizza: ')
    option = tk.OptionMenu(frame, variavel, *tamanhos)

    label_escolha = tk.Label(frame, text='')
    label_qtd = tk.Label(frame2, text='Quantidade: ', bg='red', background='lightblue')

    input = tk.Entry(frame2, width=10)
    label_resultado = tk.Label(frame2, text='--', bg='lightgreen')

    btn = tk.Button(janela_pedidos, text='enviar', command=confirmar, width=20)

    #cria checkbuttons
    lista_checks = []
    for ingrediente in ingredientes.items():
        variavel_check = tk.IntVar()
        inupt_check = tk.Checkbutton(frame3, text=ingrediente[0], variable=variavel_check)
        inupt_check.grid()
        variavel_check.set(0)
        lista_checks.append(variavel_check)

    label_escolha.grid(pady=20)
    label_inicio.grid(pady=0,)
    option.grid(padx=10, row=1, column=1)
    label_escolha.grid(pady=0, row=2, columnspan=3)

    label_qtd.grid(pady=10, row=3, column=0)
    input.grid(pady=10, padx=10, row=3, column=1)

    btn.grid(pady=0, columnspan=3)
    label_resultado.grid(pady=10)

## FIM PEDIDOS ##

## criando menus ##
#JANELA INICIAL
janela_inicio = tk.Tk()
janela_inicio.title('Pizzaria início')
janela_inicio.geometry('300x200')

#barra de menu
barra_menu = tk.Menu(janela_inicio)
#instancia do menu de pedidos
menu_pedido = tk.Menu(barra_menu)
#instancia do menu de clientes
menu_cliente = tk.Menu(barra_menu)
#adiciona o menu de pedidos e cadastro de clientes a barra de menu
barra_menu.add_cascade(label='Pedidos', menu=menu_pedido)
barra_menu.add_cascade(label='Clientes', menu=menu_cliente)
#adiciona opcoes ao menu pedidos e cadastro de clientes
menu_pedido.add_command(label='Realizar pedido', command=tela_pedido)
menu_cliente.add_command(label='Cadastrar cliente', command=tela_cliente)
janela_inicio.config(menu=barra_menu)

## FIM MENUS ##

janela_inicio.mainloop()