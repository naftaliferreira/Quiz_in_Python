import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import pandas as pd
import random

# ler arquivo
df = pd.read_excel('questoes.xlsx')
question = df.sample(n=10).values.tolist()

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

# icone
app_icon = PhotoImage(file="icons8-quiz-100.png")
app_label = tk.Label(janela, image=app_icon, bg=background_color)
app_label.pack(pady=10)

# componentes da interface
question_label = tk.Label(janela, text="Pergunta", wraplength=380,
                          bg=background_color, fg=text_color, font=("Arial", 12, "bold"))
question_label.pack(pady=20)


janela.mainloop()
