from cProfile import label
from cgitb import text
from email.mime import image
from logging import root
from msilib.schema import File
from tkinter import Entry, StringVar, image_names, messagebox, PhotoImage, Frame,Label, Tk, Button, Image, Canvas, Toplevel
import qrcode
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
 
def No():
    messagebox.showinfo(title="😤😕😑", message=(" Te dije que esta no (•̀o•́)ง"))    

def mensaje1():

    imagen_entry = StringVar()
    nombre_imagen = StringVar()
    
    
    def convertir():
        imagen = qrcode.make(imagen_entry.get())
        archivo_imagen = open(nombre_imagen.get()+ ".png", 'wb' ) 
        imagen.save(archivo_imagen)
        archivo_imagen.close()
        
    def MostrarQR():
        def DestruirQR():
            ventana_nueva2.destroy()
        ventana_nueva2 = Toplevel()
        ventana_nueva2.geometry("800x800")
        ventana_nueva2.title("QR")
        ventana_nueva2.iconbitmap("icono.ico")
        ventana_nueva2.resizable(True,True)
        canvaQR = Canvas(ventana_nueva2, width=800, height=700)
        canvaQR.place(x=100, y=100)
        canvaQR.config(bg="gray86", bd=0)
        
        boton3 = Button(ventana_nueva2, text="    Cerrar QR    ", bg="lime green", command=DestruirQR).place(x=390,y=50)
        
        global my_image
        root.filename = filedialog.askopenfilename(initialdir="Users\joalv\Desktop\Generador-de-QR-Proyecto-final" , title="Carpeta de archivos" , 
                                                   filetypes=(("Archivos png", "*.png") , ("Todos los archivos","*.*") ))
        my_label = Label(canvaQR, text=root.filename).pack() 
        my_image = ImageTk.PhotoImage(Image.open(root.filename))
        my_image_label = Label(canvaQR, image=my_image).pack()
        
     
        
    ventana_nueva1 = Toplevel()
    ventana_nueva1.geometry("500x300")
    ventana_nueva1.title("URL A QR")
    ventana_nueva1.iconbitmap("icono.ico")
    ventana_nueva1.resizable(False,False)
    
    converaqr = Label(ventana_nueva1, text="ingrese la URL: ", fg="black", bd=5, relief="groove").place(x=20,y=102)
    
    entrada1 = Entry(ventana_nueva1, bg="gray", width=50, textvariable= imagen_entry, bd=5,highlightthickness=2, highlightcolor="red").place(x=150,y=100)

    nomber_label= Label(ventana_nueva1, text="Nombre del QR: ", fg="black", bd=5, relief="groove").place(x=20,y=152)
    
    entrada2 = Entry(ventana_nueva1, bg="gray", width=50, textvariable= nombre_imagen, bd=5,highlightthickness=2, highlightcolor="red")
    entrada2.place(x=150,y=150)
    
    boton1 = Button(ventana_nueva1, text="    CONVERTIR    ", bg="orange", command=convertir).place(x=150,y=200)
    boton2 = Button(ventana_nueva1, text="     MOSTRAR CARPETA    ", bg="lime green", command=MostrarQR).place(x=270,y=200)
    
def mensaje2():

    imagen_entry = StringVar()
    nombre_imagen = StringVar()
    
    
    def convertir():
        imagen = qrcode.make(imagen_entry.get())
        archivo_imagen = open(nombre_imagen.get()+ ".png", 'wb' ) 
        imagen.save(archivo_imagen)
        archivo_imagen.close()
        
    def MostrarQR():
        def DestruirQR():
            ventana_nueva2.destroy()
        ventana_nueva2 = Toplevel()
        ventana_nueva2.geometry("800x800")
        ventana_nueva2.title("QR")
        ventana_nueva2.iconbitmap("icono.ico")
        ventana_nueva2.resizable(True,True)
        canvaQR = Canvas(ventana_nueva2, width=800, height=700)
        canvaQR.place(x=100, y=100)
        canvaQR.config(bg="gray86", bd=0)
        
        boton3 = Button(ventana_nueva2, text="    Cerrar QR    ", bg="lime green", command=DestruirQR).place(x=390,y=50)
        
        global my_image
        root.filename = filedialog.askopenfilename(initialdir="Users\joalv\Downloads\Proyecto Codigos QR" , title="Carpeta de archivos" ,
                                                   filetypes=(("Archivos png", "*.png") , ("Todos los archivos","*.*") ))
        my_label = Label(canvaQR, text=root.filename).pack() 
        my_image = ImageTk.PhotoImage(Image.open(root.filename))
        my_image_label = Label(canvaQR, image=my_image).pack()
        
    ventana_nueva3 = Toplevel()
    ventana_nueva3.geometry("500x300")
    ventana_nueva3.title("Texto A QR")
    ventana_nueva3.iconbitmap("icono.ico")
    ventana_nueva3.resizable(False,False)
    
    converaqr = Label(ventana_nueva3, text="Ingrese el texto: ", fg="black", bd=5, relief="groove").place(x=20,y=102)
    
    entrada1 = Entry(ventana_nueva3, bg="gray", width=50, textvariable= imagen_entry, bd=5,highlightthickness=2, highlightcolor="red").place(x=150,y=100)

    nomber_label= Label(ventana_nueva3, text="Nombre del QR: ", fg="black", bd=5, relief="groove").place(x=20,y=152)
    
    entrada2 = Entry(ventana_nueva3, bg="gray", width=50, textvariable= nombre_imagen, bd=5,highlightthickness=2, highlightcolor="red")
    entrada2.place(x=150,y=150)
    
    boton1 = Button(ventana_nueva3, text="    CONVERTIR    ", bg="orange", command=convertir).place(x=150,y=200)
    boton2 = Button(ventana_nueva3, text="     MOSTRAR CARPETA    ", bg="lime green", command=MostrarQR).place(x=270,y=200)
        
    



def destruir():
    messagebox.showinfo(title="Chau" , message="NOoOoOoOo te vayas 😥")
    ventana.destroy()


ventana = Tk()
ventana.title("Convertidor a QR")
ventana.resizable(False,False)
ventana.iconbitmap("icono.ico")
ventana.geometry("750x500")
ventana.config(bg="gray13")


frame1 = Frame(ventana)
frame1.pack()
frame1.config(bg="black",width= 730, height= 480 )
frame1.place(x= 10, y= 10 )
frame1.config(bd=3)
frame1.config(relief="groove")

c = Canvas(frame1, width=720, height=470)
c.place(x=0, y=0)
c.config(bg="gray86", bd=0)


img1 = PhotoImage(file=r"Recursos\puntero.png")
puntero = c.create_image(400,270, image=img1,anchor="center")

img2 = PhotoImage(file=r"Recursos\uis.png")
puntero = c.create_image(140,400, image=img2,anchor="center")

img3 = PhotoImage(file=r"Recursos\Origen.png")
puntero = c.create_image(110,260, image=img3,anchor="center")


label3=Label(frame1, text="CONVERTIDOR A CODIGO QR", fg="black", font=("Arial", 18), bd=8, relief="groove")
label3.place(x= 160,y= 20)
label3.config(bg="gray86")

label1=Label(frame1, text="Texto y URL", fg="black", font=("Arial", 18), bd=8, relief="groove")
label1.place(x= 270,y= 80)
label1.config(bg="gray86")

label2=Label(frame1, text="-seleccione la opcion que desee: ", fg="black", font=("Arial", 15), bd=5, relief="groove")
label2.place(x= 50,y= 150)
label2.config(bg="gray86")






bt1=Button(frame1, text="    Esta no    ", command=No)
bt1.place(x=200,y=200)

bt3=Button(frame1, text="      URL      ", command=mensaje1)
bt3.place(x=500,y=200)

bt4=Button(frame1, text="    TEXTO    ", command=mensaje2)
bt4.place(x=500,y=270)

bt5=Button(frame1, text="     CERRAR     ", command=destruir)
bt5.place(x=635,y=445)







ventana.mainloop()


