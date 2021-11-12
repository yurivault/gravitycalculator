from tkinter import *



# Interface do usuário(intefacen)

janelainterface = Tk()
janelainterface.geometry("1024x768")
janelainterface.title("Quanto será que eu peso em outro planeta? ")
janelainterface.iconbitmap("planet.ico")

res = DoubleVar()
planeta = StringVar()
peso = DoubleVar()


# Definindo a imagem de fundo da interface
intefacen = PhotoImage(file="interface.png")
intefacenplace = Label(janelainterface, image=intefacen)
intefacenplace.place(x=0, y=0, relwidth=1, relheight=1)


# Definindo a função que vai calcular o peso através da fórmula P = m.g, onde P = Peso, m = Massa, g = Aceleração da gravidade

def calculo():
    
    inputdoplaneta = (planeta.get())

    lua = (peso.get()*(1.62))/9.8
    jupiter = (peso.get()*(24.79))/9.8
    saturno = (peso.get()*(10.74))/9.8
    mercurio = (peso.get()*(3.70))/9.8
    venus = (peso.get()*(8.87))/9.8
    marte = (peso.get()*3.7)/9.8
    Europa_lua = (peso.get()*(1.31))/9.8
    netuno = (peso.get()*(11.15))/9.8
    urano = (peso.get()*(8.87))/9.8
    
           
# Definindo o resultado com base na escolha de planeta do usuário. Eu incluí algumas exceções com diferentes maneiras de escrever o mesmo planeta.
    
    if "Marte" in inputdoplaneta:
        res.set((marte))
    elif "marte" in inputdoplaneta:
        res.set((marte))
    elif "MARTE" in inputdoplaneta:
        res.set((marte))
    elif "Lua" in inputdoplaneta:
        res.set(( lua))
    elif "lua" in inputdoplaneta:
        res.set(( lua))
    elif "LUA" in inputdoplaneta:
        res.set(( lua))    
    elif "jupiter" in inputdoplaneta:
        res.set((jupiter))
    elif "júpiter" in inputdoplaneta:
        res.set((jupiter))
    elif "JÚPITER" in inputdoplaneta:
        res.set((jupiter))
    elif "Júpiter" in inputdoplaneta:
        res.set((jupiter))
    elif "Jupiter" in inputdoplaneta:
        res.set((jupiter))
    elif "JUPITER" in inputdoplaneta:
        res.set((jupiter))
    elif "Saturno" in inputdoplaneta:
        res.set((saturno))
    elif "SATURNO" in inputdoplaneta:
        res.set((saturno))
    elif "saturno" in inputdoplaneta:
        res.set((saturno))
    elif "venus" in inputdoplaneta:
        res.set((venus))
    elif "Venus" in inputdoplaneta:
        res.set((venus))
    elif "VENUS" in inputdoplaneta:
        res.set((venus))
    elif "mercurio" in inputdoplaneta:
        res.set((mercurio))
    elif "Mercurio" in inputdoplaneta:
        res.set((mercurio))
    elif "MERCURIO" in inputdoplaneta:
        res.set((mercurio))
    elif "Mercúrio" in inputdoplaneta:
        res.set((mercurio))
    elif "MERCÚRIO" in inputdoplaneta:
        res.set((mercurio))
    elif "mercúrio" in inputdoplaneta:
        res.set((mercurio))
    elif "Urano" in inputdoplaneta:
        res.set((urano))
    elif "urano" in inputdoplaneta:
        res.set((urano))
    elif "URANO" in inputdoplaneta:
        res.set((urano))
    elif "Netuno" in inputdoplaneta:
        res.set((netuno))
    elif "netuno" in inputdoplaneta:
        res.set((netuno))
    elif "NETUNO" in inputdoplaneta:
        res.set((netuno))
    elif "Europa" in inputdoplaneta:
        res.set((Europa_lua))
    elif "europa" in inputdoplaneta:
        res.set((Europa_lua))
    elif "EUROPA" in inputdoplaneta:
        res.set((Europa_lua))
    elif "Europa lua" in inputdoplaneta:
        res.set((Europa_lua))
    elif "EUROPA lua" in inputdoplaneta:
        res.set((Europa_lua))
    elif "europa lua" in inputdoplaneta:
        res.set((Europa_lua))
    elif "Europa lua" in inputdoplaneta:
        res.set((Europa_lua))
    
    else:
        res.set("Escolha um planeta do sistema solar de acordo com a sugestão abaixo!")
    
        

# Resultado das variáveis e definição da fonte

fontedobotao = ("Montserrat", 17, "bold")
fontedoresultado = ("Montserrat", 20, "bold")
fontedoinput = ("Montserrat", 15, "bold")



# Caixa de entrada
pesoentrada = Entry(janelainterface, justify="center", font=(fontedoinput), bd=0,textvariable=peso)
pesoentrada.place(x=450,y=200,width=80, height=35)
pesoentrada.configure(relief="ridge", font = "Arial 18 bold", border=5, background="black", fg ="white")
planeta = Entry(janelainterface,justify="center", font=(fontedoinput), bd=0,textvariable=planeta, fg = "white")
planeta.place(x=385,y=290)
planeta.configure(relief="ridge",  border=5, background="black")

# Label do resultado
textoR = Label(janelainterface,textvariable=res,font=(fontedoresultado), bd=0, bg="alice blue",justify="center", fg="white")
textoR.configure(relief="ridge", border=5, background="black")
textoR.place(x=13,y=515, width=1000, height = 48)


# Botão de calculo
boton = Button(janelainterface,text="Calcular",command=calculo,bg="white",fg="white", bd=0, font=(fontedobotao), background = "black")
boton.configure(relief="ridge", border=5, background="black")
planeta.configure(relief="ridge", border=5, background="black")
boton.place(x=430,y=453)
janelainterface.mainloop()
