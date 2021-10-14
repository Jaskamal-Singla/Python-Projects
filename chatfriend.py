from tkinter import *

#gui chatfriend made in tkinter
window=Tk()
window.geometry("500x500")
window.title("ChatBot")


window.config(bg="red")
def Reply(event=""):
    enter=entry.get().lower()
    if len(enter)==5 and enter=="hello":
        label.config(text="Hello I am your chatting friend")
    elif enter=="idiot" or enter=="stupid":
        label.config(text="Hmm...Why are you so angry on me")
    elif enter=='hi' or enter=='hi ':
        label.config(text="Hi, I am your chatting assisstant") 
    else:
        label.config(text="Huh..i did Not understand anything")
    
def delete():
    entry.delete(0,END)  
    

entry=Entry(window,font=("Impact",30,'bold'),bg="black",fg="#3ae809")
entry.grid(row=0,column=0)
label=Label(window,font=("Arial",30,'italic'))
label.grid(row=1,column=0)
button=Button(window,text="Want reply?",command=Reply).grid(row=2,column=0)

window.bind("<Return>",Reply)



window.mainloop()