from tkinter import * # kullanıcı arayüzü grafik erişimi
import time # zaman erişimi
from pynput.keyboard import Key,Controller # otomatik işlem fonksiyonları erişimi
keyboard= Controller() # otomatik işlemlere erişim, (keyboard değişken)
def f1(): # kullanıcıdan sayı alıyoruz işlemin kac saniyede bir olması için
    global var1
    var1 = int(e1.get())
def f3(): # kullanıcıdan kaç kez yazdırmak istedigi bilgisini alıyoruz
    global var3
    var3 = int(e3.get())
def f2(): # var2 yazılacak metnin değişkeni
    global var2
    count = 0
    var2 = str(e2.get())
    while True:
        time.sleep(var1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.type(var2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        count+=1
        if count == var3: #eger count var3 degiskeninin sayisina vardiysa spami durdur
            return False

def storeall():
    f1()
    f3()
    f2()
pencere= Tk()
pencere.geometry("250x230")
pencere.title("Auto Writer")

e1 = Label(pencere,text="Get delay of seconds ",fg="black",bg="lightgray")
e1.pack()
e1=Entry() # yazı yazabilmek icin Entry()'den e1 degiskenine izin aldık
e1.pack()
e2 = Label(pencere,text="Get text",fg="black",bg="lightgray")
e2.pack()
e2 = Entry()
e2.pack()
e3 = Label(pencere,text="Get how many times repeat",fg="black",bg="lightgray")
e3.pack()
e3 = Entry()
e3.pack()

var1 = 0
var2 = "hi"
var3 = 0
statusbar = 1 # not working, if 1 working

status = Label(pencere,text=f"Status={statusbar} \n If status = 1, the program is running\n\n Made by @Wooltzplus",fg="black",bg="lightgray")
status.pack()
buton = Button(pencere,text="Get",command=storeall,height=2,width=5)
buton.pack(side= BOTTOM)


pencere.mainloop() #pencerenin acılmasını saglayan kod
