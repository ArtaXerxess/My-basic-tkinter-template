# Basic tkinter template
import  tkinter  as  tk
from  tkinter  import  ttk
from  tkinter.messagebox  import  showinfo


class  ArtaXerxes(tk.Tk):
        def  __init__(self):
            super().__init__()

            #  configure  the  root  window
            self.title('My  Awesome  GUI Template')
            self.geometry('370x90')
            self.minsize(300,50)

            # label
            self.label  =  ttk.Label(self,  text='Hello,  ArtaXerxes')
            self.label.pack()

            # Buttons

            # Click Me
            self.button  =  ttk.Button(self,  text='Click  Me')
            self.button['command']  =  self.button_clicked
            self.button.pack()
            # hieeee
            self.button2 = ttk.Button(self,text='hiee')
            self.button2['command'] = self.button_clicked2
            self.button2.pack()

        def button_clicked2(self):
            print('you clicked the \'hiee\' button')

        def  button_clicked(self):
            showinfo(title='Information',message='Hello,  Tkinter!')


if __name__=="__main__":
    app =  ArtaXerxes()
    app.mainloop()