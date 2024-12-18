#
#
# VERSÃO 0.4.1
#
#
#
import tkinter  as Tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk

janela = Tk.Tk()
janela.state('zoomed')
janela.title("Teste Principal")

janela.grid_columnconfigure(1,minsize=2)
janela.grid_rowconfigure(0,minsize=100)
titulo = Tk.Label(text="LOJA DE CONVÊNIENCIA NAUM",font=100,fg="white",bg="#000000",width=180,height=5)
titulo.grid(row=0,column=0,columnspan=4)
#COMIDA
def comida():
    comidas = Tk.Toplevel()
    comidas.state('zoomed')
    comidas.title("COMIDA")
    lettera = [
        ('Pedaço de Bolo',10.50,25),
        ('Chips',9.00,26),
        ('Coxinha',4.00,27),
        ('Pão de Queijo',2.00,28)
        ]
    letterb = [
        ("Pingo D' Ouro",7.00,29),
        ("Pizza Congelada",15.00,30),
        ("Sanduiche",5.50,31),
        ("Sorvete",20.00,32)
        ]
    for i,letter in enumerate(lettera):
        linha1 = Tk.Button(comidas,text="ADICIONAR CARRINHO",command= lambda l=letter:adicionar( l[0],l[1],l[2]),background="green",fg="white")
        linha1.grid(column=i,row=4)
    #
    for i,letter in enumerate(letterb):
        linha1 = Tk.Button(comidas,text="ADICIONAR CARRINHO",command= lambda l=letter:adicionar(l[0],l[1],l[2]),background="green",fg="white")
        linha1.grid(column=i,row=8)                               
        #
    titulo = Tk.Label (comidas,text="ALIMENTOS",fg="black",bg="#FFFF00",font=100,width=180,height=5).grid(row=0,column=0,columnspan=4)
    tkimagemc0 = ImageTk.PhotoImage(Image.open("imagem/bolo.jpg"))
    # ,ipady=10
    Tk.Label(comidas,image=tkimagemc0).grid(row=1,column=0,pady=10)
    nomec1 = Tk.Label(comidas,text="Pedaço de Bolo")
    nomec1.grid(row=2,column=0)
    nomec1bc = None
    precoc1 = Tk.Label(comidas,text="R$ 10.50")
    precoc1.grid(row=3,column=0)
    #
    tkimagemc1 = ImageTk.PhotoImage(Image.open("imagem/chips.jpg"))
    Tk.Label(comidas,image=tkimagemc1).grid(row=1,column=1)
    nomec2 = Tk.Label(comidas,text="Chips")
    nomec2.grid(row=2,column=1)
    precoc2 = Tk.Label(comidas,text="R$ 9.00")
    precoc2.grid(row=3,column=1)
    #
    tkimagemc2 = ImageTk.PhotoImage(Image.open("imagem/coxinha.jpg"))
    Tk.Label(comidas,image=tkimagemc2).grid(row=1,column=2)
    nomec3 = Tk.Label(comidas,text="Coxinha")
    nomec3.grid(row=2,column=2)
    precoc3 = Tk.Label(comidas,text="R$ 4.00")
    precoc3.grid(row=3,column=2)
    #
    tkimagemc3 = ImageTk.PhotoImage(Image.open("imagem/paoque.jpg"))
    Tk.Label(comidas,image=tkimagemc3).grid(row=1,column=3)
    nomec4 = Tk.Label(comidas,text="Pão de Queijo")
    nomec4.grid(row=2,column=3)
    precoc4 = Tk.Label(comidas,text="R$ 2.00")
    precoc4.grid(row=3,column=3)
    #
    tkimagemc4 = ImageTk.PhotoImage(Image.open("imagem/pingo.jpg"))
    Tk.Label(comidas,image=tkimagemc4).grid(row=5,column=0)
    nomec5 = Tk.Label(comidas,text="Pingo D' Ouro")
    nomec5.grid(row=6,column=0)
    precoc5 = Tk.Label(comidas,text="R$ 7.00")
    precoc5.grid(row=7,column=0)
    #
    tkimagemc5 = ImageTk.PhotoImage(Image.open("imagem/pizza.jpg"))
    Tk.Label(comidas,image=tkimagemc5).grid(row=5,column=1)
    nomec6 = Tk.Label(comidas,text="Pizza Congelada")
    nomec6.grid(row=6,column=1)
    precoc6 = Tk.Label(comidas,text="R$ 15.00")
    precoc6.grid(row=7,column=1)
    #
    tkimagemc6 = ImageTk.PhotoImage(Image.open("imagem/sanduiche.jpg"))
    Tk.Label(comidas,image=tkimagemc6).grid(row=5,column=2)
    nomec7 = Tk.Label(comidas,text="Sanduiche")
    nomec7.grid(row=6,column=2)
    precoc7 = Tk.Label(comidas,text="R$ 5.50")
    precoc7.grid(row=7,column=2)
    #
    tkimagemc7 = ImageTk.PhotoImage(Image.open("imagem/sorvete.jpg"))
    Tk.Label(comidas,image=tkimagemc7).grid(row=5,column=3)
    nomec8 = Tk.Label(comidas,text="Sorvete 2L")
    nomec8.grid(row=6,column=3)
    precoc8 = Tk.Label(comidas,text="R$ 20.00")
    precoc8.grid(row=7,column=3)

    botao_fechar =Tk.Button(comidas,text="VOLTAR",command=comidas.destroy,height=2,width=10).grid(row=0,column=0)
    comidas.mainloop()
def objeto():
    obj = Tk.Toplevel()
    obj.state('zoomed')
    obj.title("OBJETO")
    titulo = Tk.Label (obj,text="OBJETO",fg="white",bg="#990000",width=180,font=100,height=5).grid(row=0,column=0,columnspan=4)
    #
    lettera = [
        ('Amoeba',8.00,17),
        ('Boneca Sonho de Mãe',13.00,18),
        ('CD PS2',10.00,19),
        ('Chaveiro',4.00,20)
        ]
    letterb = [
        ("Cubo Mágico",16.00,21),
        ("Dinossauro",15.00,22),
        ("Oculos Escuros",8.00,23),
        ("Xicara",20.00,24)
        ]
    for i,letter in enumerate(lettera):
        linha1 = Tk.Button(obj,text="ADICIONAR CARRINHO",command= lambda l=letter:adicionar( l[0],l[1],l[2]),background="green",fg="white")
        linha1.grid(column=i,row=4)
    #
    for i,letter in enumerate(letterb):
        linha1 = Tk.Button(obj,text="ADICIONAR CARRINHO",command= lambda l=letter:adicionar(l[0],l[1],l[2]),background="green",fg="white")
        linha1.grid(column=i,row=8)                               
        #
    #"
    tkimagemob0 = ImageTk.PhotoImage(Image.open("imagem/bolinha.jpg"))
    Tk.Label(obj,image=tkimagemob0).grid(row=1,column=0,pady=10)
    nomeob0 =Tk.Label(obj,text="Amoeba")
    nomeob0.grid(row=2,column=0)
    precoob0 = Tk.Label(obj,text="R$ 8,00")
    precoob0.grid(row=3,column=0)

    #
    tkimagemob1 = ImageTk.PhotoImage(Image.open("imagem/Boneca.png"))
    Tk.Label(obj,image=tkimagemob1).grid(row=1,column=1)
    nomeob1 = Tk.Label(obj,text="Boneca Sonho de Mãe")
    nomeob1.grid(row=2,column=1)
    precoob1 = Tk.Label(obj,text="R$ 13.00")
    precoob1.grid(row=3,column=1)

    #
    tkimagemob2 = ImageTk.PhotoImage(Image.open("imagem/cd.jpg"))
    Tk.Label(obj,image=tkimagemob2).grid(row=1,column=2)
    nomeob2 = Tk.Label(obj,text="CD PS2 (3 por 1)")
    nomeob2.grid(row=2,column=2)
    precoob2 = Tk.Label(obj,text="R$ 10.00")
    precoob2.grid(row=3,column=2)

    #
    tkimagemob3 = ImageTk.PhotoImage(Image.open("imagem/chaveiro.jpg"))
    Tk.Label(obj,image=tkimagemob3).grid(row=1,column=3)
    nomeob3 = Tk.Label(obj,text="Chaveiro")
    nomeob3.grid(row=2,column=3)
    precoob3 = Tk.Label(obj,text="R$ 4.00")
    precoob3.grid(row=3,column=3)

    #
    tkimagemob4 = ImageTk.PhotoImage(Image.open("imagem/cubo.jpg"))
    Tk.Label(obj,image=tkimagemob4).grid(row=5,column=0)
    nomeob4 = Tk.Label(obj,text="Cubo Mágico")
    nomeob4.grid(row=6,column=0)
    precoob4 = Tk.Label(obj,text="R$ 16.00")
    precoob4.grid(row=7,column=0)

    #
    tkimagemob5 = ImageTk.PhotoImage(Image.open("imagem/dino.jpg"))
    Tk.Label(obj,image=tkimagemob5).grid(row=5,column=1)
    nomeob5 = Tk.Label(obj,text="Dinossauro")
    nomeob5.grid(row=6,column=1)
    precoob5 = Tk.Label(obj,text="R$ 15.00")
    precoob5.grid(row=7,column=1)

    #
    tkimagemob6 = ImageTk.PhotoImage(Image.open("imagem/oculos.jpg"))
    Tk.Label(obj,image=tkimagemob6).grid(row=5,column=2)
    nomeob6 = Tk.Label(obj,text="Óculos Escuros (1 unidade)")
    nomeob6.grid(row=6,column=2)
    precoob6 = Tk.Label(obj,text="R$ 8.00")
    precoob6.grid(row=7,column=2)

    #
    tkimagemob7= ImageTk.PhotoImage(Image.open("imagem/xicara.jpg"))
    Tk.Label(obj,image=tkimagemob7).grid(row=5,column=3)
    nomeob7 = Tk.Label(obj,text="Xicara (1 unidade)")
    nomeob7.grid(row=6,column=3)
    precoob7 = Tk.Label(obj,text="R$ 14.00")
    precoob7.grid(row=7,column=3)


    botao_fechar =Tk.Button(obj,text="VOLTAR",width=10,command=obj.destroy,height=2).grid(row=0,column=0)
    obj.mainloop()
def bebida():
    bb = Tk.Toplevel()
    bb.state('zoomed')
    bb.title("BEBIDA")
    titulo = Tk.Label (bb,text="BEBIDAS",fg="white",bg="#448811",width=180,font=100,height=5).grid(row=0,column=0,columnspan=4)
    #
    letterc = [
        ('Agua Mineral',5.00,9),
        ('Pacote de Chá',3.00,10),
        ('Coca-Cola Espumante',9.99,11),
        ('Guarana Dolly',9.98,12)
        ]
    letterd = [
        ("Guarana",12.00,13),
        ("Monster",15.00,14),
        ("Pepsi",8.00,15),
        ("Suco de Laranja",20.00,16)
        ]
    for i,letter in enumerate(letterc):
        linha1 = Tk.Button(bb,text="ADICIONAR CARRINHO",command= lambda l=letter:adicionar( l[0],l[1],l[2]),background="green",fg="white")
        linha1.grid(column=i,row=4)
    #
    for i,letter in enumerate(letterd):
        linha1 = Tk.Button(bb,text="ADICIONAR CARRINHO",command= lambda l=letter:adicionar(l[0],l[1],l[2]),background="green",fg="white")
        linha1.grid(column=i,row=8)                               
        #
    #"
    tkimagembe0 = ImageTk.PhotoImage(Image.open("imagem/agua.jpg"))
    Tk.Label(bb,image=tkimagembe0).grid(row=1,column=0,pady=10)
    nomebe1 = Tk.Label(bb,text="Agua mineral")
    nomebe1.grid(row=2,column=0)
    precobe1 = Tk.Label(bb,text="R$ 5.00")
    precobe1.grid(row=3,column=0)

    #
    tkimagembe1 = ImageTk.PhotoImage(Image.open("imagem/cha.jpg"))
    Tk.Label(bb,image=tkimagembe1).grid(row=1,column=1)
    nomebe2 = Tk.Label(bb,text="Pacote de chá")
    nomebe2.grid(row=2,column=1)
    precobe2 = Tk.Label(bb,text="R$ 3.00")
    precobe2.grid(row=3,column=1)

    #
    tkimagembe2 = ImageTk.PhotoImage(Image.open("imagem/coca.jpg"))
    Tk.Label(bb,image=tkimagembe2).grid(row=1,column=2)
    nomebe3 = Tk.Label(bb,text="Coca-Cola Espumante")
    nomebe3.grid(row=2,column=2)
    precobe3 = Tk.Label(bb,text="R$ 9.99")
    precobe3.grid(row=3,column=2)

    #
    tkimagembe3 = ImageTk.PhotoImage(Image.open("imagem/dolly.jpg"))
    Tk.Label(bb,image=tkimagembe3).grid(row=1,column=3)
    nomebe4 = Tk.Label(bb,text="Guarana Dolly")
    nomebe4.grid(row=2,column=3)
    precob4 = Tk.Label(bb,text="R$ 4.00")
    precob4.grid(row=3,column=3)

    #
    tkimagembe4 = ImageTk.PhotoImage(Image.open("imagem/guarana.jpg"))
    Tk.Label(bb,image=tkimagembe4).grid(row=5,column=0)
    nomebe5 = Tk.Label(bb,text="Guarana")
    nomebe5.grid(row=6,column=0)
    precob5 = Tk.Label(bb,text="R$ 9.98")
    precob5.grid(row=7,column=0)

    #
    tkimagembe5 = ImageTk.PhotoImage(Image.open("imagem/monster.jpg"))
    Tk.Label(bb,image=tkimagembe5).grid(row=5,column=1)
    nomebe6 = Tk.Label(bb,text="Monster")
    nomebe6.grid(row=6,column=1)
    precob6 = Tk.Label(bb,text="R$ 12.00")
    precob6.grid(row=7,column=1)

    #
    tkimagembe6 = ImageTk.PhotoImage(Image.open("imagem/pepsi.jpg"))
    Tk.Label(bb,image=tkimagembe6).grid(row=5,column=2)
    nomebe7 = Tk.Label(bb,text="Pepsi")
    nomebe7.grid(row=6,column=2)
    precob7 = Tk.Label(bb,text="R$ 10.00")
    precob7.grid(row=7,column=2)

    #
    tkimagembe7 = ImageTk.PhotoImage(Image.open("imagem/suco.jpg"))
    Tk.Label(bb,image=tkimagembe7).grid(row=5,column=3)
    nomebe8 = Tk.Label(bb,text="Suco de Laranja")
    nomebe8.grid(row=6,column=3)
    precob8 = Tk.Label(bb,text="R$ 13.00")
    precob8.grid(row=7,column=3)


    botao_fechar =Tk.Button(bb,text="VOLTAR",command=bb.destroy,height=2,width=10).grid(row=0,column=0)
    
    bb.mainloop()
def limpeza():
    limpz = Tk.Toplevel()
    limpz.state('zoomed')
    limpz.title("LIMPEZA")
    titulo = Tk.Label (limpz,text="LIMPEZA/HIGIENE",font=100,fg="white",bg="#000099",width=180,height=5).grid(row=0,column=0,columnspan=4)
    #
    lettera = [
        ('Alcool',19.00,1),
        ('Detergente',7.50,2),
        ('Pacote de Esponja',11.00,3),
        ('OMO',17.00,4)
        ]
    letterb = [
        ("Veja Bem",16.00,5),
        ("Shampoo",15.00,6),
        ("Vassoura",7.00,7),
        ("Escova",8.00,8)
        ]
    for i,letter in enumerate(lettera):
        linha1 = Tk.Button(limpz,text="ADICIONAR CARRINHO",command= lambda l=letter:adicionar(l[0],l[1],l[2]),background="green",fg="white")
        linha1.grid(column=i,row=4)
    #
    for i,letter in enumerate(letterb):
        linha1 = Tk.Button(limpz,text="ADICIONAR CARRINHO",command= lambda l=letter:adicionar(l[0],l[1],l[2]),background="green",fg="white")
        linha1.grid(column=i,row=8)                               
        #
    #"
    tkimagemli0 = ImageTk.PhotoImage(Image.open("imagem/alcool.jpg"))
    Tk.Label(limpz,image=tkimagemli0).grid(row=1,column=0,pady=10)
    nomel1 = Tk.Label(limpz,text="Álcool 500ml")
    nomel1.grid(row=2,column=0)
    precol1 = Tk.Label(limpz,text="R$ 19.00")
    precol1.grid(row=3,column=0)

    #
    tkimagemli1 = ImageTk.PhotoImage(Image.open("imagem/detergente.jpg"))
    Tk.Label(limpz,image=tkimagemli1).grid(row=1,column=1)
    nomel2 = Tk.Label(limpz,text="Detergente")
    
    nomel2.grid(row=2,column=1)
    precol2 = Tk.Label(limpz,text="R$ 7.50")
    precol2.grid(row=3,column=1)

    #
    tkimagemli2 = ImageTk.PhotoImage(Image.open("imagem/esponja.jpg"))
    Tk.Label(limpz,image=tkimagemli2).grid(row=1,column=2)
    nomel3 = Tk.Label(limpz,text="Pacote de Esponja")
    nomel3.grid(row=2,column=2)
    precol3 = Tk.Label(limpz,text="R$ 11.00")
    precol3.grid(row=3,column=2)
    #
    tkimagemli3 = ImageTk.PhotoImage(Image.open("imagem/omo.jpg"))
    Tk.Label(limpz,image=tkimagemli3).grid(row=1,column=3)
    nomel4 = Tk.Label(limpz,text="OMO")
    nomel4.grid(row=2,column=3)
    precol4 = Tk.Label(limpz,text="R$ 17.00")
    precol4.grid(row=3,column=3)

    tkimagemli4 = ImageTk.PhotoImage(Image.open("imagem/veja.jpg"))
    Tk.Label(limpz,image=tkimagemli4).grid(row=5,column=0)
    nomel5 = Tk.Label(limpz,text="Veja Bem")
    nomel5.grid(row=6,column=0)
    precol5 = Tk.Label(limpz,text="R$ 16.00")
    precol5.grid(row=7,column=0)
    #
    tkimagemli5 = ImageTk.PhotoImage(Image.open("imagem/xampu.jpg"))
    Tk.Label(limpz,image=tkimagemli5).grid(row=5,column=1)
    nomel6 = Tk.Label(limpz,text="Shampoo 400ml")
    nomel6.grid(row=6,column=1)
    precol6 = Tk.Label(limpz,text="R$ 15.00")
    precol6.grid(row=7,column=1)
    #
    tkimagemli6 = ImageTk.PhotoImage(Image.open("imagem/vass.jpg"))
    Tk.Label(limpz,image=tkimagemli6).grid(row=5,column=2)
    nomeli7 = Tk.Label(limpz,text="Vassoura")
    nomeli7.grid(row=6,column=2)
    precol7 = Tk.Label(limpz,text="R$ 7.00")
    precol7.grid(row=7,column=2)
    #
    tkimagemli7 = ImageTk.PhotoImage(Image.open("imagem/escova.jpg"))
    Tk.Label(limpz,image=tkimagemli7).grid(row=5,column=3)
    nomeli8 = Tk.Label(limpz,text="Escova")
    nomeli8.grid(row=6,column=3)
    precol8 = Tk.Label(limpz,text="R$ 8.00")
    precol8.grid(row=7,column=3)
 
    botao_fechar =Tk.Button(limpz,text="VOLTAR",command=limpz.destroy,height=2,width=10).grid(row=0,column=0)
    limpz.mainloop()
#
def mostrar_car():
    car = Tk.Toplevel(janela)
    car.title("Carrinho de Compras")
    cart_label= Tk.Label(car,text="Carrinho",font=("Arial",14))
    cart_label.pack(pady=10)
    tree = ttk.Treeview(car,columns=("Nome","Preço","Quantidade","Total"),show = 'headings')
    tree.heading("Nome",text="Nome")
    tree.heading("Preço",text="Preço")
    tree.heading("Quantidade",text="Quantidade")
    tree.heading("Total",text="Total")
    tree.pack()
    total_car = 0
    for nome,i in arm.items():
        prec_tot = i['price']*i['quantity']
        total_car += prec_tot
        tree.insert("",Tk.END,values=(nome, f"R$ {i['price']:.2f}", i['quantity'], f"R$ {prec_tot:.2f}"))
    #mensagem = Tk.Label(car,text=("EXPERIMENTO")).grid(row=0,column=3)
    total_label = Tk.Label(car, text=f"Total do Carrinho: R$ {total_car:.2f}",font="Arial")
    total_label.pack(pady=10)

    Tk.Button(car, text = "Finalizar Compra", command=lambda: finalize_purchase(car)).pack(pady=10)
    Tk.Button(car,text="Deletar Item", command= lambda: remover()).pack(pady = 20)
    Tk.Button(car,text="Fechar",command = car.destroy).pack(pady=10)
    def remover():
        indice = tree.selection()
        if indice:
            item = tree.item(indice)
            nome_item = item['values'][0]  # Primeiro valor da linha (Nome do item)
            if nome_item in arm:
                del arm[nome_item]  # Remove do carrinho
            tree.delete(indice)  # Remove da árvore
            total_car = sum(i['price'] * i['quantity'] for i in arm.values())  # Atualiza o total
            total_label.config(text=f"Total do Carrinho: R$ {total_car:.2f}")
     
def adicionar(nome,preco,id):
    teste.append((nome,preco,id))
    if nome in arm:
        arm[nome]['quantity']+=1
    else:
        arm[nome] = {'price': preco, 'quantity':1}
    messagebox.showinfo("TRABALHO",f"Você adicicionou o produto {nome} com o valor de {preco}")
def finalize_purchase(car):
    if not arm:
        messagebox.showerror("Erro", "O carrinho está vazio. Adicione itens antes de finalizar a compra.")
        return

    # Criação da janela para escolher a forma de pagamento
    payment_window = Tk.Toplevel()
    payment_window.title("Escolha a Forma de Pagamento")

    # Lista de opções de pagamento
    payment_options = ["Crédito", "Débito", "Pix"]
    
    # Combobox para selecionar a forma de pagamento
    payment_combobox = ttk.Combobox(payment_window, values=payment_options, state="readonly")  # Texto padrão
    payment_combobox.pack(pady=20)

    # Função para exibir a mensagem de confirmação após a seleção
    def confirm_payment():
        selected_payment = payment_combobox.get()
        if selected_payment:
            messagebox.showinfo("Compra Finalizada", f"Compra finalizada com pagamento no {selected_payment}!")
            arm.clear()  # Limpar o carrinho após a compra
            car.destroy()  # Fechar a janela do carrinho
            payment_window.destroy()  # Fechar a janela de pagamento


        else:
            messagebox.showerror("Erro", "Escolha uma forma de pagamento válida.")
    
    # Botão para confirmar o pagamento
    Tk.Button(payment_window, text="Confirmar", command=confirm_payment).pack(pady=10)
    
    # Botão para fechar a janela de pagamento
    Tk.Button(payment_window, text="Fechar", command=payment_window.destroy).pack(pady=10)

teste = []
arm = {}
lettera = [
    ('Pizza Congelada',15.00,30),
    ('Boneca Sonho de Mãe',13.00,18),
    ('Guarana',9.98,13),
    ('Dinossauro',15.00,22)
]
letterb = [
    ('Vassoura',7.00,7),
    ('OMO',17.00,4),
    ('Sorvete',20.00,32),
    ('Veja Bem',16.00,5)
]

    #
for i,letter in enumerate(lettera):
    linha1 = Tk.Button(janela,text="ADICIONAR CARRINHO",command= lambda l=letter:adicionar( l[0],l[1],l[2]),background="green",fg="white")
    linha1.grid(column=i,row=5)
#
for i,letter in enumerate(letterb):
    linha1 = Tk.Button(janela,text="ADICIONAR CARRINHO",command= lambda l=letter:adicionar(l[0],l[1],l[2]),background="green",fg="white")
    linha1.grid(column=i,row=9)                               
    #
tkimagem = ImageTk.PhotoImage(Image.open("imagem/pizza.jpg"))
Tk.Label(janela,image=tkimagem,).grid(row=2,column=0)
nome_produto1 = Tk.Label(janela,text="Pizza Congelada").grid(row=3,column=0)
prec_produto1 = Tk.Label(janela,text='R$ 15.00').grid(row=4,column=0)
#
tkimagem2 = ImageTk.PhotoImage(Image.open("imagem/Boneca.png"))
Tk.Label(janela,image=tkimagem2).grid(row=2,column=1)
nome_produto2 = Tk.Label(janela,text="Boneca Sonho de Mãe").grid(row=3,column=1)
prec_produto2 = Tk.Label(janela,text='R$ 13.00').grid(row=4,column=1)
#
tkimagem3 = ImageTk.PhotoImage(Image.open("imagem/guarana.jpg"))
Tk.Label(janela,image=tkimagem3).grid(row=2,column=2)
nome_produto3 = Tk.Label(janela,text="Guarana").grid(row=3,column=2)
prec_produto3 = Tk.Label(janela,text='R$ 9.98').grid(row=4,column=2)
#
tkimagem4 = ImageTk.PhotoImage(Image.open("imagem/dino.jpg"))
Tk.Label(janela,image=tkimagem4).grid(row=2,column=3)
nome_produto4 = Tk.Label(janela,text="Dinossauro").grid(row=3,column=3)
prec_produto4 = Tk.Label(janela,text='R$ 15.00').grid(row=4,column=3)
#
tkimagemp = ImageTk.PhotoImage(Image.open("imagem/vass.jpg"))
Tk.Label(janela,image=tkimagemp).grid(row=6,column=0)
nome_produto5 = Tk.Label(janela,text="Vassoura").grid(row=7,column=0)
prec_produto5 = Tk.Label(janela,text='R$ 7.00').grid(row=8,column=0)
#
tkimagemp1 = ImageTk.PhotoImage(Image.open("imagem/omo.jpg"))
Tk.Label(janela,image=tkimagemp1).grid(row=6,column=1)
nome_produto6 = Tk.Label(janela,text="OMO").grid(row=7,column=1)
prec_produto6 = Tk.Label(janela,text='R$ 17.00').grid(row=8,column=1)
#
tkimagemp2 = ImageTk.PhotoImage(Image.open("imagem/sorvete.jpg"))
Tk.Label(janela,image=tkimagemp2).grid(row=6,column=2)
nome_produto7 = Tk.Label(janela,text="Sorvete").grid(row=7,column=2)
prec_produto7 = Tk.Label(janela,text='R$ 20.00').grid(row=8,column=2)
#
tkimagemp3= ImageTk.PhotoImage(Image.open("imagem/veja.jpg"))
Tk.Label(janela,image=tkimagemp3).grid(row=6,column=3)
nome_produto8 = Tk.Label(janela,text="Veja Bem").grid(row=7,column=3)
prec_produto8 = Tk.Label(janela,text='R$ 16.00').grid(row=8,column=3)

#
def login():
    import tkinter as tk
    from tkinter import messagebox
    usuarios = {}

    # Criação de Conta
    def CriarConta_Info():
        nome_2 = Usuario2.get()
        email_2 = Email.get()
        senha01_2 = Senha1.get()
        senha02_2 = Senha2.get()

        if not nome_2 or not email_2 or not senha01_2 or not senha02_2:
            messagebox.showerror("ERRO", "Todos os campos devem ser preenchidos!")
            return
        if senha01_2 != senha02_2:
            messagebox.showerror("ERRO", "As senhas não coincidem!")
            return
        if email_2 in usuarios:
            messagebox.showerror("ERRO", "Email já cadastrado!")
            return

        usuarios[email_2] = {"nome": nome_2, "senha": senha01_2}
        messagebox.showinfo("Sucesso", "Conta criada com sucesso!")

    # Validar Login
    def Validar_Login():
        email_1 = Usuario1.get()
        senha_1 = Senha3.get()

        if email_1 in usuarios and usuarios[email_1]["senha"] == senha_1:
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos!")

    # Janela 02 - Criar Conta
    def CriarConta_Janela():
        janela2 = tk.Toplevel()
        janela2.title("Criar Conta")
        janela2.resizable(False, False)

        TextoConta = tk.Label(janela2, text="Criar Conta", font=("Arial", 16), bg="#C0C0C0", height=2)
        TextoConta.grid(row=0, columnspan=2, sticky="NSEW")

        # Entrada Usuário
        global Usuario2
        Usuario2 = tk.Entry(janela2, width=30)
        Usuario2.grid(row=1, column=1, sticky="E")
        TextoUser2 = tk.Label(janela2, text="Nome:")
        TextoUser2.grid(row=1, column=0, sticky="E")

        # Entrada Email
        global Email
        Email = tk.Entry(janela2, width=30)
        Email.grid(row=2, column=1)
        TextoEmail = tk.Label(janela2, text="Email:")
        TextoEmail.grid(row=2, column=0, sticky="E")

        # Entrada Senhas
        global Senha1
        Senha1 = tk.Entry(janela2, width=30)
        Senha1.grid(row=3, column=1)
        TextoSe1 = tk.Label(janela2, text="Senha:")
        TextoSe1.grid(row=3, column=0, sticky="E")

        global Senha2
        Senha2 = tk.Entry(janela2, show="*", width=30)
        Senha2.grid(row=4, column=1, sticky="E")
        TextoSe2 = tk.Label(janela2, text="Confirmar Senha:")
        TextoSe2.grid(row=4, column=0)

        # Botão 02 - Confirmar Criação Conta
        Botao2 = tk.Button(janela2, text="Confirmar", command=CriarConta_Info)
        Botao2.grid(row=5, columnspan=2, pady=10)

    # Janela 01 - Login
    janela = tk.Tk()
    janela.title("Login")
    janela.resizable(False, False)

    # Texto Login
    TextoLogin = tk.Label(janela, text="LOGIN", font=("Arial", 16), bg="#C0C0C0", height=2)
    TextoLogin.grid(row=0, columnspan=2, sticky="NSEW")

    # Entrada Usuario (Email)
    global Usuario1
    Usuario1 = tk.Entry(janela, width=30)
    Usuario1.grid(row=1, column=1)
    TextoUser1 = tk.Label(janela, text="Usuário (Email):")
    TextoUser1.grid(row=1, column=0, sticky="E")

    # Entrada Senha
    global Senha3
    Senha3 = tk.Entry(janela, show="*", width=30)
    Senha3.grid(row=2, column=1)
    TextoSe3 = tk.Label(janela, text="Senha:")
    TextoSe3.grid(row=2, column=0, sticky="E")

    # Botão 03 - Janela Criar Conta
    Botao3 = tk.Button(janela, text="Criar Conta", command=CriarConta_Janela)
    Botao3.grid(row=4, columnspan=2)

    # Cor - Janela
    Cor = tk.Label(janela, bg="#C0C0C0", height=1)
    Cor.grid(row=5, columnspan=2, sticky="NSEW")

    # Botão 01 - Confirmar Login
    Botao1 = tk.Button(janela, text="Confirmar Login", command=Validar_Login)
    Botao1.grid(row=3, columnspan=2, pady=10)

    janela.mainloop()
    # Função para finalizar a compra

botao_comida =Tk.Button(janela,text="ALIMENTOS",width=10,height=2,border=3,activebackground="yellow",command=comida).grid(row=1,column=0)
botao_obj =Tk.Button(janela,text="OBJETO",width=10,height=2,border=3,activebackground="red",activeforeground="white",command=objeto).grid(row=1,column=1)
botao_bb =Tk.Button(janela,text="BEBIDA",width=10,height=2,border=3,activebackground="green",activeforeground="white",command=bebida).grid(row=1,column=2)
botao_limpz =Tk.Button(janela,text="LIMPEZA/HIGIENE",width=15,height=2,border=3,activebackground="blue",activeforeground="white",command=limpeza).grid(row=1,column=3)
botao_login =Tk.Button(janela,text="LOGIN",width=10,height=2,border=3,activebackground="white",command=login).grid(row=0,column=3)
botao_carro =Tk.Button(janela,text="CARRINHO",width=15,height=2,border=3,command=mostrar_car)
botao_carro.grid(row=0,column=2)

janela.mainloop()
