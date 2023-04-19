
from tkinter import *

def calculo():
 global total
 resposta_usuario = resposta.get()
 n_inteiro = int(resposta_usuario)
 if n_inteiro < 12:
    total = n_inteiro * 1.30
 else:
    total = n_inteiro*1.00

 janela1.config(text=f'PREÇO TOTAL: R${total}')


janela = Tk()
janela.title('VALOR DA COMPRA')
texto = Label(janela, text='Digite o número de maçãs compradas: ').pack()

resposta = Entry(janela)
resposta.pack()
total = 0

Button(janela,text="Calcular",command=calculo).pack()
janela1 = Label(janela, text='')
janela1.pack()
janela.mainloop()
