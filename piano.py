from tkinter import *
import time;
import datetime
import pygame
from pygame.locals import *
from variables import path

pygame.init()
root = Tk()
root.title("Piano")
root.geometry('1352x700+0+0')
root.configure(background = 'white')

ABC =Frame(root, bg="powder blue", bd=20, relief=RIDGE)
ABC.grid()
ABC1 =Frame(ABC, bg="powder blue", bd=20, relief=RIDGE)
ABC1.grid()
ABC2 =Frame(ABC, bg="powder blue", relief=RIDGE)
ABC2.grid()
ABC3 =Frame(ABC, bg="powder blue", relief=RIDGE)
ABC3.grid()

str1 = StringVar()
str1.set("Just like Music")
Date1=StringVar()
Time1=StringVar()

Date1.set(time.strftime("%d/%m/%Y"))
Time1.set(time.strftime("%H/%M/%S"))
#!-----------------------------SOSTENIDOS-------------------------------------------------------------------------------------------------
def value_DOs():
  str1.set("DO#")
  sound = pygame.mixer.Sound(path+"DO#.wav")
  sound.play()
def value_REs():
  str1.set("RE#")
  sound = pygame.mixer.Sound(path+"RE#.wav")
  sound.play()
def value_MIs():
  str1.set("MI#")
  sound = pygame.mixer.Sound(path+"MI#.wav")
  sound.play()
def value_FAs():
  str1.set("FA#")
  sound = pygame.mixer.Sound(path+"FA#.wav")
  sound.play()
def value_SOLs():
  str1.set("SOL#")
  sound = pygame.mixer.Sound(path+"SOL#.wav")
  sound.play()
def value_LAs():
  str1.set("LA#")
  sound = pygame.mixer.Sound(path+"LA#.wav")
  sound.play()
def value_SIs():
  str1.set("SI#")
  sound = pygame.mixer.Sound(path+"SI#.wav")
  sound.play()
#!-----------------------------NOTAS---------------------------------------------------------------------------
# for numero in [0, 1, 2, 3]:
#     def numero():
#       str1.set("DO")
#       sound = pygame.mixer.Sound(path+"DO.wav")
#       sound.play()


def value_DO():
  str1.set("DO")
  sound = pygame.mixer.Sound(path+"DO.wav")
  sound.play()
def value_RE():
  str1.set("RE")
  sound = pygame.mixer.Sound(path+"RE.wav")
  sound.play()
def value_MI():
  str1.set("MI")
  sound = pygame.mixer.Sound(path+"MI.wav")
  sound.play()
def value_FA():
  str1.set("FA")
  sound = pygame.mixer.Sound(path+"FA.wav")
  sound.play()
def value_SOL():
  str1.set("SOL")
  sound = pygame.mixer.Sound(path+"SOL.wav")
  sound.play()
def value_LA():
  str1.set("LA")
  sound = pygame.mixer.Sound(path+"LA.wav")
  sound.play()
def value_SI():
  str1.set("SI")
  sound = pygame.mixer.Sound(path+"SI.wav")
  sound.play()
def value_DO8():
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
btnDoSo=Button(ABC2, height = 6, width = 6, bd=4, text="DO#", font=('arial',18,'bold'), bg="black",fg="white", command = value_DOs)
btnDoSo.grid(row=0,column=0, padx=5, pady=5)
btnREs=Button(ABC2, height = 6, width = 6, bd=4, text="RE#", font=('arial',18,'bold'), bg="black",fg="white", command = value_REs)
btnREs.grid(row=0,column=2, padx=5, pady=5)

btnSpace2=Button(ABC2, state=DISABLED, height = 6, width = 2, font=('arial',18,'bold'), bg="powder blue",relief=FLAT)
btnSpace2.grid(row=0,column=3, padx=0, pady=0)

btnMIs=Button(ABC2, height = 6, width = 6, bd=4, text="MI#", font=('arial',18,'bold'), bg="black",fg="white", command = value_MIs)
btnMIs.grid(row=0,column=4, padx=5, pady=5)
btnFAs=Button(ABC2, height = 6, width = 6, bd=4, text="FA#", font=('arial',18,'bold'), bg="black",fg="white", command = value_FAs)
btnFAs.grid(row=0,column=6, padx=5, pady=5)
btnSOLs=Button(ABC2, height = 6, width = 6, bd=4, text="SOL#", font=('arial',18,'bold'), bg="black",fg="white", command = value_SOLs)
btnSOLs.grid(row=0,column=8, padx=5, pady=5)

btnSpace5=Button(ABC2, state=DISABLED, height = 6, width = 2, font=('arial',18,'bold'), bg="powder blue",relief=FLAT)
btnSpace5.grid(row=0,column=9, padx=0, pady=0)

btnLAs=Button(ABC2, height = 6, width = 6, bd=4, text="LA#", font=('arial',18,'bold'), bg="black",fg="white", command = value_LAs)
btnLAs.grid(row=0,column=10, padx=5, pady=5)
btnSIs=Button(ABC2, height = 6, width = 6, bd=4, text="SI#", font=('arial',18,'bold'), bg="black",fg="white", command = value_SIs)
btnSIs.grid(row=0,column=12, padx=5, pady=5)
#------------------------------------------------------------
btnDo=Button(ABC3, height = 8, width = 6, bd=4, text="DO", font=('arial',18,'bold'), bg="white",fg="black", command = value_DO)
btnDo.grid(row=0,column=0, padx=5, pady=5)
btnRe=Button(ABC3, height = 8, width = 6, bd=4, text="RE", font=('arial',18,'bold'), bg="white",fg="black", command = value_RE)
btnRe.grid(row=0,column=1, padx=5, pady=5)
btnMi=Button(ABC3, height = 8, width = 6, bd=4, text="MI", font=('arial',18,'bold'), bg="white",fg="black", command = value_MI)
btnMi.grid(row=0,column=2, padx=5, pady=5)
btnFa=Button(ABC3, height = 8, width = 6, bd=4, text="FA", font=('arial',18,'bold'), bg="white",fg="black", command = value_FA)
btnFa.grid(row=0,column=3, padx=5, pady=5)

btnSol=Button(ABC3, height = 8, width = 6, bd=4, text="SOL", font=('arial',18,'bold'), bg="white",fg="black", command = value_SOL)
btnSol.grid(row=0,column=4, padx=5, pady=5)
btnLa=Button(ABC3, height = 8, width = 6, bd=4, text="LA", font=('arial',18,'bold'), bg="white",fg="black", command = value_LA)
btnLa.grid(row=0,column=5, padx=5, pady=5)
btnSi=Button(ABC3, height = 8, width = 6, bd=4, text="SI", font=('arial',18,'bold'), bg="white",fg="black", command = value_SI)
btnSi.grid(row=0,column=6, padx=5, pady=5)
btnDo2=Button(ABC3, height = 8, width = 6, bd=4, text="DO", font=('arial',18,'bold'), bg="white",fg="black", command = value_DO8)
btnDo2.grid(row=0,column=7, padx=5, pady=5)

btnD1=Button(ABC3, height = 8, width = 6, bd=4, text="D1", font=('arial',18,'bold'), bg="white",fg="black", command = value_Elise)
btnD1.grid(row=0,column=8, padx=5, pady=5)
btnE1=Button(ABC3, height = 8, width = 6, bd=4, text="E1", font=('arial',18,'bold'), bg="white",fg="black", command = value_Flute)
btnE1.grid(row=0,column=9, padx=5, pady=5)
btnF1=Button(ABC3, height = 8, width = 6, bd=4, text="F1", font=('arial',18,'bold'), bg="white",fg="black", command = value_Valkir)
btnF1.grid(row=0,column=10, padx=5, pady=5)
#------------------------------------------------------------
root.mainloop()