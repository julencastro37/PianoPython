from tkinter import *
import time;
import datetime
import pygame
from pygame.locals import *
from variables import path
from variables import notas
# from variables import notasSostenidas

pygame.init()
root = Tk()
root.title("Piano")
root.geometry('1352x700+0+0')
root.configure(background = 'white')



str1 = StringVar()
str1.set("Just like Music")
Date1=StringVar()
Time1=StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H:%M:%S"))
#!-----------------------------SOSTENIDOS------------------------------------------
def value_DOs(event):
  str1.set("DO#")
  sound = pygame.mixer.Sound(path+"DO#.wav")
  sound.play()
  # print ("tecleado", repr(event))

def value_REs(event):
  str1.set("RE#")
  sound = pygame.mixer.Sound(path+"RE#.wav")
  sound.play()

def value_MIs(event):
  str1.set("MI#")
  sound = pygame.mixer.Sound(path+"MI#.wav")
  sound.play()

def value_FAs(event):
  str1.set("FA#")
  sound = pygame.mixer.Sound(path+"FA#.wav")
  sound.play()

def value_SOLs(event):
  str1.set("SOL#")
  sound = pygame.mixer.Sound(path+"SOL#.wav")
  sound.play()

def value_LAs(event):
  str1.set("LA#")
  sound = pygame.mixer.Sound(path+"LA#.wav")
  sound.play()

def value_SIs(event):
  str1.set("SI#")
  sound = pygame.mixer.Sound(path+"SI#.wav")
  sound.play()
#!-----------------------------NOTAS------------------------------------
def value_DO(event):
  str1.set("DO")
  sound = pygame.mixer.Sound(path+"DO.wav")
  sound.play()
def value_RE(event):
  str1.set("RE")
  sound = pygame.mixer.Sound(path+"RE.wav")
  sound.play()
def value_MI(event):
  str1.set("MI")
  sound = pygame.mixer.Sound(path+"MI.wav")
  sound.play()
def value_FA(event):
  str1.set("FA")
  sound = pygame.mixer.Sound(path+"FA.wav")
  sound.play()
def value_SOL(event):
  str1.set("SOL")
  sound = pygame.mixer.Sound(path+"SOL.wav")
  sound.play()
def value_LA(event):
  str1.set("LA")
  sound = pygame.mixer.Sound(path+"LA.wav")
  sound.play()
def value_SI(event):
  str1.set("SI")
  sound = pygame.mixer.Sound(path+"SI.wav")
  sound.play()
def value_DO8(event):
  str1.set("DO 1/8")
  sound = pygame.mixer.Sound(path+"DO2.wav")
  sound.play()
#-----------------------------Canciones-------------------------------
def value_Elise():
  str1.set("Fur elise")
  sound = pygame.mixer.Sound(path+"elise.wav")
  sound.play()
def value_Flute():
  str1.set("Magic Flute")
  sound = pygame.mixer.Sound(path+"flute.wav")
  sound.play()
def value_Valkir():
  str1.set("Valkirias")
  sound = pygame.mixer.Sound(path+"11-cabalgataDeLasValquiriasLaValquiria372.mp3")
  sound.play()
#-----------------------------DECLARATIONS-------------------------------
ABC =Frame(root, bg="powder blue", bd=20, relief=RIDGE)
ABC.grid()
ABC1 =Frame(ABC, bg="powder blue", bd=20, relief=RIDGE)
ABC1.grid()
ABC2 =Frame(ABC, bg="powder blue", relief=RIDGE)
ABC2.bind("a", value_DOs)
ABC2.grid()
ABC3 =Frame(ABC, bg="powder blue", relief=RIDGE)
ABC3.grid()
#-----------------------------Label with title-------------------------------
Label(ABC1, text="Piano Musical Keys", font=('arial',25,'bold'), padx=8, pady=8, bd=4, bg="powder blue",
fg="white",justify=CENTER).grid(row=0,column=0,columnspan=11)
#------------------------------------------------------------
txtDate=Entry(ABC1, textvariable=Date1, font=('arial',18,'bold'), bd=34, bg="powder blue",
fg="black", width=28, justify=CENTER).grid(row=1,column=0,pady=1)

txtDisplay=Entry(ABC1, textvariable=str1, font=('arial',18,'bold'), bd=34, bg="powder blue",
fg="black", width=28, justify=CENTER).grid(row=1,column=1,pady=1)

txtTime=Entry(ABC1, textvariable=Time1, font=('arial',18,'bold'), bd=34, bg="powder blue",
fg="black", width=28, justify=CENTER).grid(row=1,column=2,pady=1)
#----------------------------------SOSTENIDOS--------------------------
# eventos = ['value_DOs']
# for nota in notas:
#     nota=Button(ABC2, height = 6, width = 6, bd=4, text=nota, font=('arial',18,'bold'), bg="black",fg="white", command = value_DOs)
#     nota.grid(row=0,column=0, padx=5, pady=5)
#     root.bind("q", eventos(0))


btnDoSo=Button(ABC2, height = 6, width = 6, bd=4, text="DO#", font=('arial',18,'bold'), bg="black",fg="white", command = value_DOs)
btnDoSo.grid(row=0,column=0, padx=5, pady=5)
root.bind("q", value_DOs)

btnREs=Button(ABC2, height = 6, width = 6, bd=4, text="RE#", font=('arial',18,'bold'), bg="black",fg="white", command = value_REs)
btnREs.grid(row=0,column=2, padx=5, pady=5)
root.bind("w", value_REs)
btnSpace2=Button(ABC2, state=DISABLED, height = 6, width = 2, font=('arial',18,'bold'), bg="powder blue",relief=FLAT)
btnSpace2.grid(row=0,column=3, padx=0, pady=0)

btnMIs=Button(ABC2, height = 6, width = 6, bd=4, text="MI#", font=('arial',18,'bold'), bg="black",fg="white", command = value_MIs)
btnMIs.grid(row=0,column=4, padx=5, pady=5)
root.bind("e", value_MIs)
btnFAs=Button(ABC2, height = 6, width = 6, bd=4, text="FA#", font=('arial',18,'bold'), bg="black",fg="white", command = value_FAs)
btnFAs.grid(row=0,column=6, padx=5, pady=5)
root.bind("r", value_FAs)
btnSOLs=Button(ABC2, height = 6, width = 6, bd=4, text="SOL#", font=('arial',18,'bold'), bg="black",fg="white", command = value_SOLs)
btnSOLs.grid(row=0,column=8, padx=5, pady=5)
root.bind("t", value_SOLs)

btnSpace5=Button(ABC2, state=DISABLED, height = 6, width = 2, font=('arial',18,'bold'), bg="powder blue",relief=FLAT)
btnSpace5.grid(row=0,column=9, padx=0, pady=0)

btnLAs=Button(ABC2, height = 6, width = 6, bd=4, text="LA#", font=('arial',18,'bold'), bg="black",fg="white", command = value_LAs)
btnLAs.grid(row=0,column=10, padx=5, pady=5)
root.bind("y", value_LAs)
btnSIs=Button(ABC2, height = 6, width = 6, bd=4, text="SI#", font=('arial',18,'bold'), bg="black",fg="white", command = value_SIs)
btnSIs.grid(row=0,column=12, padx=5, pady=5)
root.bind("u", value_SIs)
#------------------------------------------------------------
btnDo=Button(ABC3, height = 8, width = 6, bd=4, text="DO", font=('arial',18,'bold'), bg="white",fg="black", command = value_DO)
btnDo.grid(row=0,column=0, padx=5, pady=5)
root.bind("a", value_DO)
btnRe=Button(ABC3, height = 8, width = 6, bd=4, text="RE", font=('arial',18,'bold'), bg="white",fg="black", command = value_RE)
btnRe.grid(row=0,column=1, padx=5, pady=5)
root.bind("s", value_RE)
btnMi=Button(ABC3, height = 8, width = 6, bd=4, text="MI", font=('arial',18,'bold'), bg="white",fg="black", command = value_MI)
btnMi.grid(row=0,column=2, padx=5, pady=5)
root.bind("d", value_MI)
btnFa=Button(ABC3, height = 8, width = 6, bd=4, text="FA", font=('arial',18,'bold'), bg="white",fg="black", command = value_FA)
btnFa.grid(row=0,column=3, padx=5, pady=5)
root.bind("f", value_FA)
btnSol=Button(ABC3, height = 8, width = 6, bd=4, text="SOL", font=('arial',18,'bold'), bg="white",fg="black", command = value_SOL)
btnSol.grid(row=0,column=4, padx=5, pady=5)
root.bind("g", value_SOL)
btnLa=Button(ABC3, height = 8, width = 6, bd=4, text="LA", font=('arial',18,'bold'), bg="white",fg="black", command = value_LA)
btnLa.grid(row=0,column=5, padx=5, pady=5)
btnSi=Button(ABC3, height = 8, width = 6, bd=4, text="SI", font=('arial',18,'bold'), bg="white",fg="black", command = value_SI)
btnSi.grid(row=0,column=6, padx=5, pady=5)
root.bind("h", value_SI)
btnDo2=Button(ABC3, height = 8, width = 6, bd=4, text="DO", font=('arial',18,'bold'), bg="white",fg="black", command = value_DO8)
btnDo2.grid(row=0,column=7, padx=5, pady=5)
root.bind("j", value_DO8)
btnD1=Button(ABC3, height = 8, width = 6, bd=4, text="D1", font=('arial',18,'bold'), bg="white",fg="black", command = value_Elise)
btnD1.grid(row=0,column=8, padx=5, pady=5)
btnE1=Button(ABC3, height = 8, width = 6, bd=4, text="E1", font=('arial',18,'bold'), bg="white",fg="black", command = value_Flute)
btnE1.grid(row=0,column=9, padx=5, pady=5)
btnF1=Button(ABC3, height = 8, width = 6, bd=4, text="F1", font=('arial',18,'bold'), bg="white",fg="black", command = value_Valkir)
btnF1.grid(row=0,column=10, padx=5, pady=5)
#------------------------------------------------------------
root.mainloop()