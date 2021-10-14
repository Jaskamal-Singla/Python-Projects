from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import Text
from tkinter import colorchooser
import webbrowser as wb
from tkinter import messagebox
import sys
# from PIL import Image, ImageGrab

# hot features : shortcut keys flexible menu bar

window=Tk()
winWidth=2560
winHeight=1600


window.title("Jas' Text Editor Program")

window.geometry("2560x1600")
menubar=Menu(window)
window.config(menu=menubar)

def saveFile(event=""):
    file=filedialog.asksaveasfile(initialdir=r"/Users/dirname/Desktop/python",
                                    defaultextension=".txt", #*the default extension will be .txt
                                  filetypes=[('Text files','.txt'),
                                             ('HTML files','.html'),
                                             ('All files','.*')]
                                  )
    
    
    if file is None:
        return
    fileText=str(text.get(1.0,END))
    file.write(fileText)
    print(fileText)
    file.close()

def openFile(event=""):
    file=filedialog.askopenfile(filetypes=(('Text files','*.txt'),('HTML','*.html')))
    if not file:
        return
    try:
        opened=open(file,'r')
        file.write(opened.read())
    except Exception:
        messagebox.showinfo(title="Something went wrong", message="The system was not able to read the contents of the file")
    file.close()

def ChooseColor():
    color=colorchooser.askcolor()
    
def openWebsite():
    try:
        wb.open(r"https://code.visualstudio.com/")  #it will open the site of visual studio 
    except Exception:
        messagebox.showerror(title="Network Connection Error",message='''Connection Error\n Unable to connect to the server''') 

def ChooseBg():
    color=colorchooser.askcolor()
    colorHex=color[1]
    text.config(bg=colorHex)  

def ChooseFg():
    color=colorchooser.askcolor()
    colorHex=color[1]
    text.config(fg=colorHex)

def makeBold(event):
    text.config(font=('Helvetica',35,'bold'))

def makeItalic(event):
    text.config(font=('Helvetica',35,'italic'))

def makeUnderline(event):
    text.config(font=('Helvetica',35,'underline'))

def selectAll(event):
    text.get(1.0,END) 

def ChooseDarkMode():
    text.config(bg='black',fg='white',insertbackground='white') #insert background changes cursor color

def ChooseWhiteMode():
    text.config(bg='white',fg='black',insertbackground='black')

def chooseCursor():
    color=colorchooser.askcolor()
    colorHex=color[1]
    text.config(insertbackground=colorHex)

def takeScreenshot():
    # image=ImageGrab.grab()
    # image.show()  
    pass  
    


    

fileMenu=Menu(menubar,tearoff=0)
fileMenu.add_command(label='Open',command=openFile)
fileMenu.add_command(label='Save',command=saveFile)
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit)

menubar.add_cascade(label='File',menu=fileMenu)

editMenu=Menu(menubar,tearoff=0)
editMenu.add_command(label='Pick color',command=ChooseColor) # ?I have used it so that the user can get the desired color hex value from the editor itself instead of going to google
editMenu.add_command(label="Choose BgColor",command=ChooseBg)
editMenu.add_command(label="Choose FontColor",command=ChooseFg)
editMenu.add_command(label="Cursor Color",command=chooseCursor)
editMenu.add_separator()
editMenu.add_command(label="Dark Mode" ,command=ChooseDarkMode)
editMenu.add_command(label="Light Mode",command=ChooseWhiteMode)

editMenu.add_separator()

editMenu.add_command(label="Take Screenshot",command=takeScreenshot)


menubar.add_cascade(label='Edit',menu=editMenu)


helpMenu=Menu(menubar,tearoff=0)
helpMenu.add_command(label="About",command=openWebsite)

menubar.add_cascade(label="Help",menu=helpMenu)

 


#setting scroll bar to the text area
scrollbar=Scrollbar(window)
scrollbar.pack(fill=Y,side=RIGHT) #I WILL BE ADDED TO RIGHT SIDE OF THE SCREEN LIKE IN VS CODE 

text=Text(window,font=('Helvetica',35),width=500,undo=True,yscrollcommand=scrollbar.set) 
scrollbar.config(command=text.yview) 
text.pack()




#shortcut keys for mac users
if (sys.platform=='darwin'):
    window.bind("<Command-s>",saveFile)
    window.bind("<Command-o>",openFile)
    window.bind("<Command-b>",makeBold)
    window.bind("<Command-i>",makeItalic)
    window.bind("<Command-u>",makeUnderline)
    window.bind("<Command-z>",text.edit_undo)
    window.bind("<Command-a>",selectAll)
else:
    window.bind("<Control-s>",saveFile)
    window.bind("<Control-o>",openFile)
    window.bind("<Control-b>",makeBold)
    window.bind("<Control-i>",makeItalic)
    window.bind("<Control-u>",makeUnderline)
    window.bind("<Control-z>",text.edit_undo)
    window.bind("<Control-a>",selectAll)






window.mainloop()
