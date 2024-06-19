import tkinter as tk

janela = tk.Tk()

janela.title('Pizzaria')
janela.geometry('300x350')

tamanhos = {'Pequena': 15, 'Média': 22, 'Grande': 28}
ingredientes = {"Queijo Extra": 2.00, "Pepperoni": 3.00, "Bacon": 4.00}
ingredientes_lista = ["Queijo Extra", 'Pepperoni', 'Bacon']
valor_total = 0
tamanho_selecionado = ''
ingrediente_selecionado = []


variavel = tk.StringVar()#? para que serve e porque usar
variavel.set('Grande')

def escolha(var):
    global tamanho_selecionado
    label_escolha['text'] = var
    tamanho_selecionado = var

def calcular():

    tamanho = variavel.get()
    qtd = int(input.get())
    
    # if tamanho == 'Pequena':
    #     preco_un = 15
    # elif tamanho == 'Média':
    #     preco_un = 22
    # else:
    #     preco_un = 28
    
    ingredientes_marcados = []
    print(15*'=')
    for nome, estado in enumerate(lista_checks):
        print('-')
        estado_selecionado = estado.get()
        print(f'Estado selecionado: {estado_selecionado}')
        print(ingredientes_lista[nome])
        
        if estado_selecionado == 1:
            ingredientes_marcados.append(ingredientes_lista[nome])
        
    preco_un = tamanhos[tamanho]
    
    total_ingredientes = 0
    for i in ingredientes_marcados:
        total_ingredientes += ingredientes[i]
    
    total_unidade = preco_un * qtd
    
    valor_total = total_unidade + total_ingredientes
    
    label_resultado.config(text=f'Tamanho: {tamanho} - R${total_unidade:.2f} \n Ingredientes: \n {ingredientes_marcados} - R${total_ingredientes:.2f} \n Valor total: R${valor_total:.2f} ')


teste = tk.Frame(janela, border='5', background='blue')
teste.grid(row=0, column=0, padx=5, pady=5)

teste2 = tk.Frame(janela, background='lightcoral')
teste2.grid(padx=5, pady=5)

teste3 = tk.Frame(janela, bg='lightblue')
teste3.grid()


lista_checks = [] #?  salva os estados 
for ingrediente in ingredientes.items():
    variavel_check = tk.IntVar()
    inupt_check = tk.Checkbutton(teste3, text=ingrediente[0], variable=variavel_check)
    inupt_check.grid()
    variavel_check.set(0)
    lista_checks.append(variavel_check)
    

label_inicio = tk.Label(teste, text='Escolha o tamanho da pizza: ')

option = tk.OptionMenu(teste, variavel, *tamanhos, command=escolha)

label_escolha = tk.Label(teste, text='')

label_qtd = tk.Label(teste2, text='Quantidade: ', bg='red', background='lightblue')

input = tk.Entry(teste2, width=10)

label_resultado = tk.Label(teste2, text='--', bg='lightgreen')

btn = tk.Button(janela, text='enviar', command=calcular, width=20)

label_escolha.grid(pady=20)
label_inicio.grid(pady=0,)
option.grid(padx=10, row=1, column=1)
label_escolha.grid(pady=0, row=2, columnspan=3)

label_qtd.grid(pady=10, row=3, column=0)
input.grid(pady=10, padx=10, row=3, column=1)

btn.grid(pady=0, columnspan=3)
label_resultado.grid(pady=10)

janela.mainloop()