from tkinter import *
import random
import time
from tkinter import filedialog,messagebox

def salidaPrincipal():
    ventana.destroy()

Title = ("arial black", 25)
Subtitle = ("Cambria", 12)

ventana = Tk()
ventana.geometry("800x700")
ventana.title("Ruloneta")
ventana.resizable(0,0)
ventana.config(bg="#0081CB")

marcoPrincipal = Frame(ventana, bd="10", relief=RIDGE, bg="#FF9933")
marcoPrincipal.pack(side=TOP)

tituloPrincipal = Label(marcoPrincipal, text="La Ruloneta", font=Title, fg="#202020", bg="#FF9933")
tituloPrincipal.pack()

subPrincipal = Label(marcoPrincipal, bd=5, text="BIENVENIDOS", font=Subtitle, fg="#202020", bg="#FF9933")
subPrincipal.pack()


def menu():
    ventanaProductos = Toplevel()
    ventanaProductos.config(bg="#202020")
    ventanaProductos.title("Productos")
    ventanaProductos.resizable(0,0)
    ventanaProductos.geometry("1100x650")

    def texto():
        textoText.delete(1.0, END)
        x = random.randint(1, 10000)
        noText = "No" + str(x)
        fecha = time.strftime("%d-%m-%y")
        textoText.insert(END, "Ayuda.." + noText + "\t\t\t\t Fecha:" + fecha + "\n")
        textoText.insert(END, "********************************************************\n")
        textoText.insert(END, " Buenas, esperamos solucionar sus inconvenientes\n")
        textoText.insert(END, " "+ "\n")
        textoText.insert(END, "Para seleccionar su articulo, presione en la casilla donde  "+"\n" +
                         "se encuentre, luego añada la cantidad deseada                   ")
        textoText.insert(END, "********************************************************\n\n")
        textoText.insert(END, "Si tiene algún reclamo, contactenos a:\t\t\t"+ "\n")
        textoText.insert(END, "                     LaRuloneta@support.com \t\t\t \n")

    def guardar():
        url=filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        datos_recibo=textoText.get(1.0, END)
        url.write(datos_recibo)
        url.close()
        messagebox.showinfo("Informacion", message="Instrucciones almacenada con exito")

    def borrar():
        textoText.delete(1.0, END)
        txtCamiseta.set("0")
        txtPantalon.set("0")
        txtCampera.set("0")
        txtShorts.set("0")
        txtCalzas.set("0")
        txtMedias.set("0")
        txtCamperones.set("0")
        txtRetro.set("0")
        txtOriginal.set("0")


        txtGuantes.set("0")
        txtPelotas.set("0")
        txtCanilleras.set("0")
        txtBotinero.set("0")
        txtBotines.set("0")
        txtVendas.set("0")
        txtVinchas.set("0")
        txtMuñequeras.set("0")
        txtCintas.set("0")

        
        textCamiseta.config(state=DISABLED)
        textPantalon.config(state=DISABLED)
        textCampera.config(state=DISABLED)
        textShorts.config(state=DISABLED)
        textCalzas.config(state=DISABLED)
        textMedias.config(state=DISABLED)
        textCamperones.config(state=DISABLED)
        textRetro.config(state=DISABLED)
        textOriginal.config(state=DISABLED)

    
        textGuantes.config(state=DISABLED)
        textPelotas.config(state=DISABLED)
        textCanilleras.config(state=DISABLED)
        textBotinero.config(state=DISABLED)
        textBotines.config(state=DISABLED)
        textVendas.config(state=DISABLED)
        textVinchas.config(state=DISABLED)
        textMuñequeras.config(state=DISABLED)
        textCintas.config(state=DISABLED)


        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)

        global costoderopa, costodeaccesorios, total
        costoderopa=0
        costodeaccesorios=0
        total=0

        entryCostoRopa.config(state=NORMAL)
        entryCostoRopa.delete(0, END)
        entryCostoRopa.insert(0, costoderopa)
        entryCostoRopa.config(state=DISABLED)

        entryCostoAccesorios.config(state=NORMAL)
        entryCostoAccesorios.delete(0, END)
        entryCostoAccesorios.insert(0, costodeaccesorios)
        entryCostoAccesorios.config(state=DISABLED)

        entryTotal.config(state=NORMAL)
        entryTotal.delete(0, END)
        entryTotal.insert(0, total)
        entryTotal.config(state=DISABLED)

    def salirMenu():
        ventanaProductos.destroy()

    def totalFinal():
        global costoderopa, costodeaccesorios, total
        t_camiseta = int(textCamiseta.get()) 
        t_pantalon = int(textPantalon.get())
        t_campera = int(textCampera.get())
        t_shorts = int(textShorts.get())
        t_calzas = int(textCalzas.get())
        t_medias = int(textMedias.get())
        t_camperones = int(textCamperones.get())
        t_retro = int(textRetro.get())
        t_original = int(textOriginal.get())
        costoderopa = (t_camiseta * 1000) + (t_pantalon * 700) + (t_campera * 500) + (t_shorts * 750) + (t_calzas * 1500) + (t_medias * 800) + (t_camperones * 1100) + (t_retro * 6000) + (t_original * 5000)
        entryCostoRopa.config(state=NORMAL)
        entryCostoRopa.delete(0, END)
        entryCostoRopa.insert(0, costoderopa)
        entryCostoRopa.config(state=DISABLED)

        t_guantes = int(textGuantes.get())
        t_pelotas = int(textPelotas.get())
        t_canilleras = int(textCanilleras.get())
        t_botinero = int(textBotinero.get())
        t_botines = int(textBotines.get())
        t_vendas = int(textVendas.get())
        t_vinchas = int(textVinchas.get())
        t_muñequeras = int(textMuñequeras.get())
        t_cintas = int(textCintas.get())
        costodeaccesorios = (t_guantes * 600) + (t_pelotas * 600) + (t_canilleras * 600) + (t_botinero * 600) + (t_botines * 500) + (
                    t_vendas * 500) + (t_vinchas * 800) + (t_muñequeras * 800) + (t_cintas * 800)
        entryCostoAccesorios.config(state=NORMAL)
        entryCostoAccesorios.delete(0, END)
        entryCostoAccesorios.insert(0, costodeaccesorios)
        entryCostoAccesorios.config(state=DISABLED)

        total = costoderopa + costodeaccesorios
        entryTotal.config(state=NORMAL)
        entryTotal.delete(0, END)
        entryTotal.insert(0, total)
        entryTotal.config(state=DISABLED)

    def Camiseta(): 
        if var1.get() == 1:
            textCamiseta.config(state=NORMAL)
            textCamiseta.delete(0, END)
            textCamiseta.focus()
        else: 
            textCamiseta.config(state=DISABLED)
            txtCamiseta.set("0")

    def Pantalon():
        if var2.get() == 1:
            textPantalon.config(state=NORMAL)
            textPantalon.delete(0, END)
            textPantalon.focus()
        else:
            textPantalon.config(state=DISABLED)
            txtPantalon.set("0")

    def Campera():
        if var3.get() == 1:
            textCampera.config(state=NORMAL)
            textCampera.delete(0, END)
            textCampera.focus()
        else:
            textCampera.config(state=DISABLED)
            txtCampera.set("0")

    def Shorts():
        if var4.get() == 1:
            textShorts.config(state=NORMAL)
            textShorts.delete(0, END)
            textShorts.focus()
        else:
            textShorts.config(state=DISABLED)
            txtShorts.set("0")

    def Calzas():
        if var5.get() == 1:
            textCalzas.config(state=NORMAL)
            textCalzas.delete(0, END)
            textCalzas.focus()
        else:
            textCalzas.config(state=DISABLED)
            txtCalzas.set("0")

    def Medias():
        if var6.get() == 1:
            textMedias.config(state=NORMAL)
            textMedias.delete(0, END)
            textMedias.focus()
        else:
            textMedias.config(state=DISABLED)
            txtMedias.set("0")

    def Camperones():
        if var7.get() == 1:
            textCamperones.config(state=NORMAL)
            textCamperones.delete(0, END)
            textCamperones.focus()
        else:
            textCamperones.config(state=DISABLED)
            txtCamperones.set("0")

    def Retro():
        if var8.get() == 1:
            textRetro.config(state=NORMAL)
            textRetro.delete(0, END)
            textRetro.focus()
        else:
            textRetro.config(state=DISABLED)
            txtRetro            .set("0")

    def Original():
        if var9.get() == 1:
            textOriginal.config(state=NORMAL)
            textOriginal.delete(0, END)
            textOriginal.focus()
        else:
            textOriginal.config(state=DISABLED)
            txtOriginal.set("0")


    def Guantes():
        if var10.get() == 1:
            textGuantes.config(state=NORMAL)
            textGuantes.delete(0, END)
            textGuantes.focus()
        else:
            textGuantes.config(state=DISABLED)
            txtGuantes.set("0")

    def Pelotas():
        if var11.get() == 1:
            textPelotas.config(state=NORMAL)
            textPelotas.delete(0, END)
            textPelotas.focus()
        else:
            textPelotas.config(state=DISABLED)
            txtPelotas.set("0")

    def Canilleras():
        if var12.get() == 1:
            textCanilleras.config(state=NORMAL)
            textCanilleras.delete(0, END)
            textCanilleras.focus()
        else:
            textCanilleras.config(state=DISABLED)
            txtCanilleras.set("0")

    def Botinero():
        if var13.get() == 1:
            textBotinero.config(state=NORMAL)
            textBotinero.delete(0, END)
            textBotinero.focus()
        else:
            textBotinero.config(state=DISABLED)
            txtBotinero.set("0")

    def Botines():
        if var14.get() == 1:
            textBotines.config(state=NORMAL)
            textBotines.delete(0, END)
            textBotines.focus()
        else:
            textBotines.config(state=DISABLED)
            txtBotines.set("0")

    def Vendas():
        if var15.get() == 1:
            textVendas.config(state=NORMAL)
            textVendas.delete(0, END)
            textVendas.focus()
        else:
            textVendas.config(state=DISABLED)
            txtVendas.set("0")

    def Vinchas():
        if var16.get() == 1:
            textVinchas.config(state=NORMAL)
            textVinchas.delete(0, END)
            textVinchas.focus()
        else:
            textVinchas.config(state=DISABLED)
            txtVinchas.set("0")

    def Muñequeras():
        if var17.get() == 1:
            textMuñequeras.config(state=NORMAL)
            textMuñequeras.delete(0, END)
            textMuñequeras.focus()
        else:
            textMuñequeras.config(state=DISABLED)
            txtMuñequeras.set("0")

    def Cintas():
        if var18.get() == 1:
            textCintas.config(state=NORMAL)
            textCintas.delete(0, END)
            textCintas.focus()
        else:
         textCintas.config(state=DISABLED)
         txtCintas.set("0")
         textCintas.focus()


    marcoSuperior = Frame(ventanaProductos, bd=5, relief=RIDGE, bg="#FF9933")
    marcoSuperior.pack(side=TOP)

    tituloProductos = Label(marcoSuperior, text="LA RULONETA              ", font=Title, fg="white", bg="#FF8000", width=53)
    tituloProductos.grid(row=0, column=0)


    marcoProductos = Frame(ventanaProductos, bd=10, relief=RIDGE, bg="#FF8000")
    marcoProductos.pack(side=LEFT)

    marcoCosto = Frame(marcoProductos, bd=2, relief=RIDGE, bg="#FF8000")
    marcoCosto.pack(side=BOTTOM)

    marcoRopa = LabelFrame(marcoProductos, text="Ropa", bd=5, font=Subtitle, fg="white", relief=RIDGE, bg="#202020")
    marcoRopa.pack(side=LEFT)

    marcoAccesorios = LabelFrame(marcoProductos, text="Accesorios", bd=5, font=Subtitle, fg="white", relief=RIDGE, bg="#202020")
    marcoAccesorios.pack(side=LEFT)


    ladoDerecho = Frame(marcoProductos, bd=5, relief=RIDGE, bg="#202020")
    ladoDerecho.pack(side=RIGHT)
    marcoTexto = Frame(ladoDerecho, bd=5, relief=RIDGE, bg="#202020")
    marcoTexto.pack()
    marcoBoton = Frame(ladoDerecho, bd=5, relief=RIDGE, bg="#202020")
    marcoBoton.pack()


    var1 = IntVar()
    var2 = IntVar()
    var3 = IntVar()
    var4 = IntVar()
    var5 = IntVar()
    var6 = IntVar()
    var7 = IntVar()
    var8 = IntVar()
    var9 = IntVar()
    
    var10 = IntVar()
    var11 = IntVar()
    var12 = IntVar()
    var13 = IntVar()
    var14 = IntVar()
    var15 = IntVar()
    var16 = IntVar()
    var17 = IntVar()
    var18 = IntVar()


    txtCamiseta = StringVar()
    txtCamiseta.set("0")
    txtPantalon = StringVar()
    txtPantalon.set("0")
    txtCampera = StringVar()
    txtCampera.set("0")
    txtShorts = StringVar()
    txtShorts.set("0")
    txtCalzas = StringVar()
    txtCalzas.set("0")
    txtMedias = StringVar()
    txtMedias.set("0")
    txtCamperones = StringVar()
    txtCamperones.set("0")
    txtRetro             = StringVar()
    txtRetro            .set("0")
    txtOriginal = StringVar()
    txtOriginal.set("0")


    txtGuantes = StringVar()
    txtGuantes.set("0")
    txtPelotas = StringVar()
    txtPelotas.set("0")
    txtCanilleras = StringVar()
    txtCanilleras.set("0")
    txtBotinero = StringVar()
    txtBotinero.set("0")
    txtBotines = StringVar()
    txtBotines.set("0")
    txtVendas = StringVar()
    txtVendas.set("0")
    txtVinchas = StringVar()
    txtVinchas.set("0")
    txtMuñequeras = StringVar()
    txtMuñequeras.set("0")
    txtCintas = StringVar()
    txtCintas.set("0")


    costoderopa = StringVar()

    Camiseta = Checkbutton(marcoRopa, text="Camiseta----------  $1000", font=Subtitle, onvalue=1, offvalue=0, variable=var1,
                        command=Camiseta)
    Camiseta.grid(row=0, column=0, sticky=W)
    Pantalon = Checkbutton(marcoRopa, text="Pantalon------------  $700", font=Subtitle, onvalue=1, offvalue=0, variable=var2,
                           command=Pantalon)
    Pantalon.grid(row=1, column=0, sticky=W)
    Campera = Checkbutton(marcoRopa, text="Campera------------  $500", font=Subtitle, onvalue=1, offvalue=0, variable=var3,
                       command=Campera)
    Campera.grid(row=2, column=0, sticky=W)
    Shorts = Checkbutton(marcoRopa, text="Shorts---------------  $750", font=Subtitle, onvalue=1, offvalue=0, variable=var4,
                           command=Shorts)
    Shorts.grid(row=3, column=0, sticky=W)
    Calzas = Checkbutton(marcoRopa, text="Calzas--------------  $1500", font=Subtitle, onvalue=1, offvalue=0,
                              variable=var5, command=Calzas)
    Calzas.grid(row=4, column=0, sticky=W)
    Medias = Checkbutton(marcoRopa, text="Medias--------------- $800", font=Subtitle, onvalue=1, offvalue=0, variable=var6,
                        command=Medias)
    Medias.grid(row=5, column=0, sticky=W)
    Camperones = Checkbutton(marcoRopa, text="Camperones-----  $1100", font=Subtitle, onvalue=1, offvalue=0, variable=var7,
                         command=Camperones)
    Camperones.grid(row=6, column=0, sticky=W)
    Retro = Checkbutton(marcoRopa, text="Retro--------------- $6000", font=Subtitle, onvalue=1, offvalue=0, variable=var8,
                        command=Retro)
    Retro.grid(row=7, column=0, sticky=W)
    Original = Checkbutton(marcoRopa, text="Original------------ $5000", font=Subtitle, onvalue=1, offvalue=0, variable=var9,
                        command=Original)
    Original.grid(row=8, column=0, sticky=W)

    textCamiseta = Entry(marcoRopa, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtCamiseta)
    textCamiseta.grid(row=0, column=1)
    textPantalon = Entry(marcoRopa, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtPantalon)
    textPantalon.grid(row=1, column=1)
    textCampera = Entry(marcoRopa, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtCampera)
    textCampera.grid(row=2, column=1)
    textShorts = Entry(marcoRopa, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtShorts)
    textShorts.grid(row=3, column=1)
    textCalzas = Entry(marcoRopa, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtCalzas)
    textCalzas.grid(row=4, column=1)
    textMedias = Entry(marcoRopa, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtMedias)
    textMedias.grid(row=5, column=1)
    textCamperones = Entry(marcoRopa, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtCamperones)
    textCamperones.grid(row=6, column=1)
    textRetro = Entry(marcoRopa, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtRetro          )
    textRetro.grid(row=7, column=1)
    textOriginal = Entry(marcoRopa, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtOriginal)
    textOriginal.grid(row=8, column=1)


    Guantes = Checkbutton(marcoAccesorios, text="Guantes---------------  $600", font=Subtitle, onvalue=1, offvalue=0, variable=var10,
                        command=Guantes)
    Guantes.grid(row=0, column=0, sticky=W)
    Pelotas = Checkbutton(marcoAccesorios, text="Pelotas----------------  $600", font=Subtitle, onvalue=1, offvalue=0, variable=var11,
                           command=Pelotas)
    Pelotas.grid(row=1, column=0, sticky=W)
    Canilleras = Checkbutton(marcoAccesorios, text="Canilleras------------- $600", font=Subtitle, onvalue=1, offvalue=0, variable=var12,
                        command=Canilleras)
    Canilleras.grid(row=2, column=0, sticky=W)
    Botinero = Checkbutton(marcoAccesorios, text="Botinero--------------  $600", font=Subtitle, onvalue=1, offvalue=0, variable=var13,
                         command=Botinero)
    Botinero.grid(row=3, column=0, sticky=W)
    Botines = Checkbutton(marcoAccesorios, text="Botines----------------  $500", font=Subtitle, onvalue=1, offvalue=0,
                        variable=var14, command=Botines)
    Botines.grid(row=4, column=0, sticky=W)
    Vendas = Checkbutton(marcoAccesorios, text="Vendas----------------- $500", font=Subtitle, onvalue=1, offvalue=0, variable=var15,
                       command=Vendas)
    Vendas.grid(row=5, column=0, sticky=W)
    Vinchas = Checkbutton(marcoAccesorios, text="Vinchas---------------- $800", font=Subtitle, onvalue=1, offvalue=0, variable=var16,
                        command=Vinchas)
    Vinchas.grid(row=6, column=0, sticky=W)
    Muñequeras = Checkbutton(marcoAccesorios, text="Muñequeras----------$800", font=Subtitle, onvalue=1, offvalue=0, variable=var17,
                          command=Muñequeras)
    Muñequeras.grid(row=7, column=0, sticky=W)
    Cintas = Checkbutton(marcoAccesorios, text="Cintas-------------------$800", font=Subtitle, onvalue=1, offvalue=0, variable=var18,
                       command=Cintas)
    Cintas.grid(row=8, column=0, sticky=W)

    textGuantes = Entry(marcoAccesorios, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtGuantes)
    textGuantes.grid(row=0, column=1)
    textPelotas = Entry(marcoAccesorios, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtPelotas)
    textPelotas.grid(row=1, column=1)
    textCanilleras = Entry(marcoAccesorios, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtCanilleras)
    textCanilleras.grid(row=2, column=1)
    textBotinero = Entry(marcoAccesorios, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtBotinero)
    textBotinero.grid(row=3, column=1)
    textBotines = Entry(marcoAccesorios, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtBotines)
    textBotines.grid(row=4, column=1)
    textVendas = Entry(marcoAccesorios, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtVendas)
    textVendas.grid(row=5, column=1)
    textVinchas = Entry(marcoAccesorios, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtVinchas)
    textVinchas.grid(row=6, column=1)
    textMuñequeras = Entry(marcoAccesorios, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtMuñequeras)
    textMuñequeras.grid(row=7, column=1)
    textCintas = Entry(marcoAccesorios, font=Subtitle, bd=7, width=8, state=DISABLED, textvariable=txtCintas)
    textCintas.grid(row=8, column=1)


    costoRopa = Label(marcoCosto, text="Total de Ropa $", font=Subtitle, bd=10, bg="#FF9933", fg="white")
    costoRopa.grid(row=0, column=0)
    entryCostoRopa = Entry(marcoCosto, font=Subtitle, bd=5, width=14, state="readonly")
    entryCostoRopa.grid(row=0, column=1, padx=5)

    costoAccesorios = Label(marcoCosto, text="Total Accesorios $", font=Subtitle, bd=10, bg="#FF9933", fg="white")
    costoAccesorios.grid(row=1, column=0)
    entryCostoAccesorios = Entry(marcoCosto, font=Subtitle, bd=5, width=14, state="readonly")
    entryCostoAccesorios.grid(row=1, column=1, padx=5)

    costoTotal = Label(marcoCosto, text="Total $", font=Subtitle, bd=10, bg="#FF9933", fg="white")
    costoTotal.grid(row=2, column=0)
    entryTotal = Entry(marcoCosto, font=Subtitle, bd=5, width=14, state="readonly")
    entryTotal.grid(row=2, column=1, padx=5)


    textoText = Text(marcoTexto, font=("arial", 12, "bold"), bd=3, width=48, height=12)
    textoText.grid(row=0, column=0)

    botonTotal = Button(marcoBoton, text="Total", font=Subtitle, fg="white", bg="#202020", bd=4, padx=5, command=totalFinal)
    botonTotal.grid(row=0,column=0)

    botonTexto = Button(marcoBoton, text="Guia", font=Subtitle, fg="white", bg="#202020", bd=4, padx=5, command=texto)
    botonTexto.grid(row=0, column=1)


    botonBorrar = Button(marcoBoton, text="Borrar", font=Subtitle, fg="white", bg="#202020", bd=4, padx=5, command=borrar)
    botonBorrar.grid(row=0, column=3)

    botonSalida = Button(marcoBoton, text="Salir", font=Subtitle, fg="white", bg="#202020", bd=4, padx=5, command=salirMenu)
    botonSalida.grid(row=0, column=4)

menuBoton = Button(ventana, font=Subtitle, text="Comprar", command=menu, height="2", width="20")
menuBoton.config(bd=2, bg="#202020", fg="white")
menuBoton.pack()
menuBoton.place(x=300, y=300)


salir = Button(ventana, font=Subtitle, text="Salir", command=salidaPrincipal, width="20", height="2")
salir.config(bd=2, bg="#202020", fg="white")
salir.pack()
salir.place(x=300, y=400)

ventana.mainloop()




