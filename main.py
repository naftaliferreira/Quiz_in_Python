import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# ler arquivo
df = pd.read_excel('questoes.xlsx')
questoes = df.sample(n=10).values.tolist()

# interface gráfica

janela = tk.Tk()
janela.title('Quiz')
janela.geometry("400x450")

# definição de cores

background_color = "#ECECEC"
text_color = "#333333"
button_color = "#4CAF50"

janela.config(bg=background_color)
janela.option_add('*Font', 'Arial') 

janela.mainloop()