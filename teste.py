import tkinter  as Tk
from PIL import Image,ImageTk
janela = Tk.Tk()
janela.state('zoomed')
janela.title("Teste Principal")
janela.grid_columnconfigure(0,minsize=250)
janela.grid_rowconfigure(0, minsize=50)
titulo = Tk.Label (text= "El teste com o titulo de 'Loja coveniente'",fg="white",bg="#400289",width=100,height =5)
titulo.grid(row=0,column=0,columnspan=2)






tkimage = ImageTk.PhotoImage(Image.open("teste image.jpg"))
tkimage2 = ImageTk.PhotoImage(Image.open("teste image.jpg"))
Tk.Label(janela, image=tkimage).grid(row=1, column=0)
Tk.Label(janela, image=tkimage2).grid(row=1, column=1)
mensagem =Tk.Label (text = "EL Sherek Mexicano",fg="green",bg="#990000")
mensagem.grid(row=2, column=0)
custo =Tk.Label (text="R$ 100,00")
custo.grid(row=3,column=0)
mensagem2 = Tk.Label (text="El impostor",fg="red",bg = "#009900")
mensagem2.grid(row=2, column=1)
custo2 =Tk.Label (text="R$ 1,00")
custo2.grid(row=3,column=1)
janela.mainloop()