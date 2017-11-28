import tkinter as tk
from tkinter.filedialog import askdirectory
import tkinter.messagebox
import unzip as uz
import base64, os

# Crear favicon
icon = \
"""
AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAABILAAASCwAAAAAAAAAAAAD////////////////////////////////+/v7//////+vr6//Jycn/w8PD/9LS0v/5+fn////////////////////////////////////////////9/f3//////8TExP96enr/YGBg/1NTU/9xcXH/kpKS//Hx8f///////v7+//////////////////////////////////Pz8/99fX3/PT09/zo6Ov9YWFj/JCQk/11dXf+hoaH///////z8/P/////////////////////////////////39/f/dnZ2/3Fxcf+IiIj/kpKS/2tra/8rKyv/lpaW//z8/P/////////////////+/v7//Pz8//39/f/8/Pz//////+jo6P+Ghob/iYmJ/5CQkP8fHx//SkpK/5CQkP///////v7+///////+/v7//v7+/////////////f39///////ExMT/gICA/0pKSv8aGhr/W1tb/4CAgP/Dw8P///////39/f/+/v7//////+zs7P+2trb/pKSk/6SkpP/FxcX/kJCQ/0ZGRv8vLy//j4+P/319ff+goKD//////////////////////+3t7f93d3f/VFRU/zw8PP8/Pz//Z2dn/3Fxcf88PDz/dXV1/4ODg/94eHj/bm5u/7Kysv///////Pz8//////+5ubn/Y2Nj/zc3N/9ycnL/Wlpa/yUlJf91dXX/ZmZm/zAwMP9LS0v/KSkp/2FhYf+qqqr///////z8/P//////19fX/3d3d/+JiYn/hISE/6Wlpf8uLi7/XV1d/3l5ef+CgoL/YWFh/3x8fP+cnJz/9PT0///////+/v7//f39///////BwcH/fn5+/4uLi/83Nzf/KCgo/25ubv/Nzc3/9fX1/97e3v/q6ur//v7+///////////////////////z8/P/gICA/1lZWf8WFhb/WFhY/4eHh/+qqqr///////7+/v////////////39/f/+/v7/////////////////2NjY/29vb/8mJib/i4uL/4GBgf99fX3/wcHB///////9/f3//f39//7+/v///////////////////////////97e3v9xcXH/NDQ0/3t7e/9sbGz/YGBg/29vb//g4OD///////7+/v////////////////////////////7+/v//////lZWV/11dXf85OTn/Nzc3/0tLS/+AgID/8fHx///////+/v7////////////////////////////+/v7///////Dw8P+np6f/iYmJ/4iIiP+hoaH/39/f///////+/v7/////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==
"""
icondata= base64.b64decode(icon)
tempFile= "icon.ico"
iconfile= open(tempFile,"wb")
## Extract the icon
iconfile.write(icondata)
iconfile.close()

class Descomprimidor:
    #Carga el path de la imagen que se quiere abrir, y lo escribe en el campo entry_1.
    def search_path_in(self):
            fname = askdirectory()
            self.var_1.set(fname)
            if self.var_2.get() == '':
                self.var_2.set(fname)

    def search_path_out(self):
            fname = askdirectory()
            self.var_2.set(fname)

    def descomprimir(self):
        try:
            flag = uz.descomprimir(self.var_1.get(),self.var_2.get())
            if flag == 0:
                tkinter.messagebox.showinfo('Info', 'Archivos descomprimidos exitosamente')
            else:
                tkinter.messagebox.showwarning('Warning', 'No hay archivos .zip ni .Z en el directorio seleccionado')
        except:
            tkinter.messagebox.showerror('Error', 'Algo ha salido mal.')


    def __init__(self, master):
        self.master = master
        master.title("Descompresor de archivos")
        master.minsize(width=910, height=120)
        master.minsize(width=910, height=30)
        master.resizable(width=False, height=False)
        master.iconbitmap(default=tempFile)

        self.label_1 = tk.Label(master, text="Seleccione la carpeta donde están los archivos comprimidos:")
        self.label_1.place(x=5, y= 5)
        self.label_2 = tk.Label(master, text="Seleccione la carpeta donde desea ubicar los archivos después de descomprimirlos:")
        self.label_2.place(x=5, y= 50)

        self.var_1 = tk.StringVar()
        self.var_2 = tk.StringVar()

        self.entry_1 = tk.Entry(master,width=30, textvariable=self.var_1)
        self.entry_1.place(x=5, y=25, width=800, height=22) #width in pixels
        self.entry_2 = tk.Entry(master,width=30, textvariable=self.var_2)
        self.entry_2.place(x=5, y=70, width=800, height=22) #width in pixels

        self.boton_1 = tk.Button(master, text="Browse", command=self.search_path_in, width=10, bg = "white")
        self.boton_1.place(x=820, y=25, width=80, height=22)
        self.boton_2 = tk.Button(master, text="Browse", command=self.search_path_out, width=10, bg = "white")
        self.boton_2.place(x=820, y=70, width=80, height=22)
        self.boton_3 = tk.Button(master, text="Descomprimir", command=self.descomprimir, width=10, bg = "green")
        self.boton_3.place(x=10, y=110, width=100, height=22)

root = tk.Tk()
my_gui = Descomprimidor(root)
os.remove(tempFile)
root.mainloop()
