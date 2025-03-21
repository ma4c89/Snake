from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re

def validar_numeros(input):
    return input.isdigit() or input == ""

def validar_email(valor):
    padrao_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(padrao_email, valor):
        return True
    else:
        messagebox.showerror("Erro", "E-mail inválido. Por favor, insira um e-mail válido.")
        return False

def enviar():
    n = nome.get()
    i = idade.get()
    mae = nome_mae.get()
    pai = nome_pai.get()
    e = estado_civil.get()
    r = rua.get()
    b = bairro.get()
    nc = numero_casa.get()
    em = email.get()
    te = telefone.get()

    selecionado = linguagem.curselection()
    if selecionado:
        l = linguagem.get(selecionado[0])
    else:
        l = "Nenhuma linguagem selecionada"

    if not validar_email(em):
        return

    print(f"Nome: {n} \n Idade: {i} \n Mãe: {mae} \n Pai: {pai} \n Estado Civil: {e}")
    print(f"Rua: {r} \n Bairro: {b} \n Número da Casa: {nc} \n Email: {em} \n Telefone: {te}")
    print(f"Linguagem Favorita: {l}\n\n")

    resetar_campos()

def resetar_campos():
    nome.delete(0, END)
    idade.delete(0, END)
    nome_mae.delete(0, END)
    nome_pai.delete(0, END)
    estado_civil.set("")
    linguagem.selection_clear(0, END)
    rua.delete(0, END)
    bairro.delete(0, END)
    numero_casa.delete(0, END)
    email.delete(0, END)
    telefone.delete(0, END)

# Código da interface gráfica
janela = Tk()
janela.title("Tela")
janela.geometry("500x500")
janela.configure(bg="lightblue")

janela.grid_columnconfigure(0, weight=1)
janela.grid_columnconfigure(1, weight=1)

label = Label(janela, text="Seja bem-vindo", font=("Arial", 12, "bold"), fg="black", bg="lightblue")
label.grid(row=0, column=0, columnspan=2, pady=10, sticky="ew")

label_nome = Label(janela, text="Digite seu nome:", fg="black", bg="lightblue")
label_nome.grid(row=1, column=0, sticky="e", padx=5, pady=5)
nome = Entry(janela, width=25)
nome.grid(row=1, column=1, padx=5, pady=5, sticky="w")

vc = janela.register(validar_numeros)

label_idade = Label(janela, text="Idade:", fg="black", bg="lightblue")
label_idade.grid(row=2, column=0, sticky="e", padx=5, pady=5)
idade = Entry(janela, width=25, validate="key", validatecommand=(vc, "%P"))
idade.grid(row=2, column=1, padx=5, pady=5, sticky="w")

label_nome_mae = Label(janela, text="Nome da mãe:", fg="black", bg="lightblue")
label_nome_mae.grid(row=3, column=0, sticky="e", padx=5, pady=5)
nome_mae = Entry(janela, width=25)
nome_mae.grid(row=3, column=1, padx=5, pady=5, sticky="w")

label_nome_pai = Label(janela, text="Nome do pai:", fg="black", bg="lightblue")
label_nome_pai.grid(row=4, column=0, sticky="e", padx=5, pady=5)
nome_pai = Entry(janela, width=25)
nome_pai.grid(row=4, column=1, padx=5, pady=5, sticky="w")

label_rua = Label(janela, text="Rua:", fg="black", bg="lightblue")
label_rua.grid(row=5, column=0, sticky="e", padx=5, pady=5)
rua = Entry(janela, width=25)
rua.grid(row=5, column=1, padx=5, pady=5, sticky="w")

label_bairro = Label(janela, text="Bairro:", fg="black", bg="lightblue")
label_bairro.grid(row=6, column=0, sticky="e", padx=5, pady=5)
bairro = Entry(janela, width=25)
bairro.grid(row=6, column=1, padx=5, pady=5, sticky="w")

label_numero_casa = Label(janela, text="Número da casa:", fg="black", bg="lightblue")
label_numero_casa.grid(row=7, column=0, sticky="e", padx=5, pady=5)
numero_casa = Entry(janela, width=25, validate="key", validatecommand=(vc, "%P"))
numero_casa.grid(row=7, column=1, padx=5, pady=5, sticky="w")

label_email = Label(janela, text="E-mail:", fg="black", bg="lightblue")
label_email.grid(row=8, column=0, sticky="e", padx=5, pady=5)
email = Entry(janela, width=25)
email.grid(row=8, column=1, padx=5, pady=5, sticky="w")

label_telefone = Label(janela, text="Número de telefone:", fg="black", bg="lightblue")
label_telefone.grid(row=9, column=0, sticky="e", padx=5, pady=5)
telefone = Entry(janela, width=25, validate="key", validatecommand=(vc, "%P"))
telefone.grid(row=9, column=1, padx=5, pady=5, sticky="w")

style = ttk.Style()
style.configure("TCombobox", fieldbackground="lightgrey", background="lightgrey")

label_estado_civil = Label(janela, text="Estado Civil:", fg="black", bg="lightblue")
label_estado_civil.grid(row=10, column=0, sticky="e", padx=5, pady=5)
estado_civil = ttk.Combobox(janela, values=["Solteiro(a)", "Casado(a)"], width=22, style="TCombobox")
estado_civil.grid(row=10, column=1, padx=5, pady=5, sticky="w")

label_linguagem = Label(janela, text="Linguagem Favorita:", fg="black", bg="lightblue")
label_linguagem.grid(row=11, column=0, sticky="e", padx=5, pady=5)

linguagem = Listbox(janela, height=5, bg="lightgrey")
linguagem.grid(row=11, column=1, padx=5, pady=5, sticky="w")
linguagem.insert(END, "Java")
linguagem.insert(END, "C++")
linguagem.insert(END, "JavaScript")
linguagem.insert(END, "Python")
linguagem.insert(END, "C#")

b = Button(janela, text="Enviar", font=("Arial", 10), bg="blue", fg="white", width=8, command=enviar)
b.grid(row=12, column=0, columnspan=2, pady=10)

janela.mainloop()