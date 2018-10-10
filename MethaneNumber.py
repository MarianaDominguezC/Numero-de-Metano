from tkinter import *

#"Constantes"
root = Tk()
root.title("Methane Number")
root.geometry("500x400")
root["bg"]="#87cefa"
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
CH4 = DoubleVar()
C2H6 = DoubleVar()
C3H8 = DoubleVar()
IC4H10 = DoubleVar()
NC4H10 = DoubleVar()
IC5H12 = DoubleVar()

#Añadir Funciones
def getResultforMN():
        gaslist = [CH4.get(),C2H6.get(),C3H8.get(),IC4H10.get(),NC4H10.get(),IC5H12.get()]
        hcratio = [4,3,8/3,10/4,10/4,12/5]
        hctot = []
        suma = sum(gaslist)
        if 0<suma<=100:
            for i in range(0,len(gaslist)):
                hctot.append((gaslist[i]/100)*hcratio[i])
            if 2<=sum(hctot)<=5:
                mon = 20.17*(sum(hctot) ** 3) - 173.55*(sum(hctot) ** 2) + 508.04*sum(hctot)- 406.14
                mn = 1.445*mon - 103.42
                print("Methane Number = %(first)d" % {"first": mn})
            else:
                print("H/C Ratio is out of Range")
        else:
            print("Off the range, update the mixture! Percentage = %(second)d" %{"second":suma})

#Añadir mas parametros para GUI 
#METANO
Methane = Label(root, text="Methane, CH4".translate(SUB), fg="Black", bg="#87cefa").place(x=10,y=10)
intCH4 = Entry(root, textvariable=CH4).place(x=130,y=10)

#ETANO
Ethane = Label(root, text="Ethane, C2H6".translate(SUB), fg="Black", bg="#87cefa").place(x=10,y=30)
intC2H6 = Entry(root, textvariable=C2H6).place(x=130,y=30)

#PROPANO
Propane = Label(root, text="Propane, C3H8".translate(SUB), fg="Black", bg="#87cefa").place(x=10,y=50)
intC3H8 = Entry(root, textvariable=C3H8).place(x=130,y=50)

#i-BUTANO
iButano = Label(root, text="iButane, i-C4H10".translate(SUB), fg="Black", bg="#87cefa").place(x=10,y=70)
intIC4H10 = Entry(root, textvariable=IC4H10).place(x=130,y=70)

#n-Butano
nButano = Label(root, text="nButane, n-C4H10".translate(SUB), fg="Black", bg="#87cefa").place(x=10,y=90)
intNC4H10 = Entry(root, textvariable=NC4H10).place(x=130,y=90)

#i-Pentano
iPentano = Label(root, text="iPentano, i-C5H12".translate(SUB), fg="Black", bg="#87cefa").place(x=10,y=110)
intIC5H12 = Entry(root, textvariable=IC5H12).place(x=130,y=110)

calculate = Button(root, text="Compute MN!", fg="Blue", command=getResultforMN).place(x=400,y=320)
close = Button(root, text="Exit Program.", fg="Red", command=root.quit).place(x=400,y=350)

root.mainloop()
#Nombre Gas ;   Variable  ; Unit
#Methane    ;   CH4       ; % mole
#Ethane     ;   C2H6      ; % mole
#Propane    ;   C3H8      ; % mole
#i-Butane   ;   IC4H10    ; % mole
#n-Butane   ;   NC4H10    ; % mole
#i-Pentane  ;   IC5H12    ; % mole
#n-Pentane  ;   NC5H12    ; % mole
#n-Hexane   ;   C6H14     ; % mole
#n-Heptane  ;   C7H16     ; % mole
#n-Octane   ;   C8H18     ; % mole
#n-Nonane   ;   C9H20     ; % mole
#n-Decane   ;   C10H22    ; % mole
#Hydrogen H2;   H         ; % mole  -> max: 0,03%
#Sulfuro H2 ;   H2S       ; ppmv    -> max: 6 ppmv
#Monox Carb ;   CO        ; % mole
#Diox Carb  ;   C02       ; % mole
#Nitrogeno  ;   N2        ; % mole
#Oxygeno    ;   O2        ; % mole
#Siloxane   ;   SI        ; % mole  -> max: 0,0003%
#Sulfur     ;   S2        ; % peso  -> max: 0,001% (10ppm weight)

# Como resultado tendriamos tres parametros:
# Lower Heating Value [BTU/lbm] (mas brigido)
# Widgets: Label(root, text, fg), Entry(), Radiobutton(root, text="", value=1, variable= ), Button()
# ej: Button(root, text="BLABLA").grid(row=0,column=0) ó .place(x=0,y=0) ó .pack(side=RIGHT/LEFT)
