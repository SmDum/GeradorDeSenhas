#Importação das bibliotecas necessárias
import tkinter as tk
from tkinter import messagebox
import random 
import string 
import pyperclip 

#Função para gerar a senha
def gerar_senha():
    
    try:
        tamanho = int(tamanho_entry.get())
        if tamanho < 4:
            messagebox.showerror("Erro", "O tamanho da senha deve ser pelo menos 4.")
            return
    except:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")
        return
    
    caracteres = ""
    if minusculas.get():
        caracteres += string.ascii_lowercase
        
    if maiusculas.get():
        caracteres += string.ascii_uppercase
        
    if numeros.get():
        caracteres += string.digits
        
    if simbolos.get():
        caracteres += string.punctuation
        
    if not caracteres:
        messagebox.showerror("Erro", "Por favor, selecione pelo menos um tipo de caractere.")
        return
    
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    entry_senha.delete(0, tk.END)
    entry_senha.insert(0, senha)
    

def copiar_senha():
    senha = entry_senha.get()
    if senha:
        pyperclip.copy(senha)
        messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência.")
    else:
        messagebox.showerror("Erro", "Nenhuma senha gerada para copiar.")
    
# Configuração da janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")
janela.geometry("400x300")
janela.resizable(False, False)

# Layout da janela

# Tamanho da senha
tk.Label(janela, text="Tamanho da Senha:").pack(pady=10)
tamanho_entry = tk.Entry(janela)
tamanho_entry.pack(pady=5)


# Definição das opções de caracteres como TRUE por padrão
maiusculas = tk.BooleanVar(value=True)
minusculas = tk.BooleanVar(value=True)
numeros = tk.BooleanVar(value=True)
simbolos = tk.BooleanVar(value=True)

# Checkbuttons para selecionar os tipos de caracteres
tk.Checkbutton(janela, text="Incluir Letras Maiúsculas", variable=maiusculas).pack(anchor=tk.W)
tk.Checkbutton(janela, text="Incluir Letras Minúsculas", variable=minusculas).pack(anchor=tk.W)
tk.Checkbutton(janela, text="Incluir Números", variable=numeros).pack(anchor=tk.W)
tk.Checkbutton(janela, text="Incluir Símbolos", variable=simbolos).pack(anchor=tk.W)

# Botões para gerar e copiar a senha
tk.Button(janela, text="Gerar Senha", command=gerar_senha).pack(pady=10)

entry_senha = tk.Entry(janela, width=40, justify='center')
entry_senha.pack(pady=5)

tk.Button(janela, text="Copiar Senha", command=copiar_senha).pack(pady=10)

janela.mainloop()