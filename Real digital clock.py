#!/usr/bin/env python
# coding: utf-8

# In[25]:


from time import strftime
from tkinter import Label,Tk

#window Config for clock
window=Tk()# we have to call window.mainloop()
window.title("My clock")#title of window
window.geometry("200x200")#geometry of window
window.configure(bg="grey")#configure for the bg color
window.resizable(False,False)#resizable function (false which means no to resize)


#label config
clock_label=Label(window,bg="black",fg="yellow", font=("Times",30,'bold'),relief='solid')
clock_label.place(x=20,y=20)#used to set the position of the window

def updating_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text=current_time)
    clock_label.after(80,updating_label)# updating label after 80 mili sec
    
updating_label()
window.mainloop()


# In[ ]:





# In[ ]:





# In[ ]:




