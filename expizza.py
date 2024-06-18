import tkinter as tk

janela = tk.Tk()

janela.title('Pizzaria')
janela.geometry('300x150')

label_inicio = tk.Label(text='Escolha o tamanho da pizza: ')

tamanhos = ['Pequena', 'Média', 'Grande']
preco_unidade = {'Pequena': 20, 'Média': 30, 'Grande': 40}
valor_total = 0
tamanho_selecionado = ''


variavel = tk.StringVar()
variavel.set(tamanhos[0])

def escolha(var):
    global tamanho_selecionado
    label_escolha['text'] = var
    tamanho_selecionado = var

def calcular():
    global valor_total, preco_unidade
    
    tamanho = variavel.get()
    qtd = int(input.get())
    
    if tamanho == 'Pequena':
        preco_un = 15
    elif tamanho == 'Média':
        preco_un = 22
    else:
        preco_un = 28
    
    valor_total = preco_un * qtd
    
    label_resultado.config(text=f'Valor total: {valor_total} | Tamanho: {tamanho_selecionado}')


option = tk.OptionMenu(janela, variavel, *tamanhos, command=escolha)

label_escolha = tk.Label(janela, text='')

label_qtd = tk.Label(text='Quantidade: ', bg='red', background='lightblue', justify='left')

input = tk.Entry(width=10)

label_resultado = tk.Label(text='')

btn = tk.Button(text='enviar', command=calcular, width=20)



label_escolha.grid(row=1, column=0, pady=20)

label_inicio.grid(pady=0, row=1, column=0)
option.grid(pady=0, row=1, column=1)
label_escolha.grid(pady=0, row=2, columnspan=3)

label_qtd.grid(pady=10, row=3, column=0)
input.grid(pady=0, row=3, column=1)

btn.grid(pady=0, columnspan=3)
label_resultado.grid(pady=0)

janela.mainloop()