import numpy as np
import tkinter as tk  # gives tk namespace

  
def get_list(event):
    """
    function to read the listbox selection
    and put the result in an entry widget
    """
    # get selected line index
    index = listbox1.curselection()[0]
    # get the line's text
    seltext = listbox1.get(index)
    # delete previous text in enter1
    enter1.delete(0, 50)
    # now display the selected text
    enter1.insert(0, seltext)
    filter_list.append(float(seltext))
    context=0.
    for i in range(len(filter_list)):
        context=context+2.**(filter_list[i]-1)
        print("Filter and context ",i+1,filter_list[i],int(context))
        

def set_list(event):
    """
    insert an edited line from the entry widget
    back into the listbox
    """
    try:
        index = listbox1.curselection()[0]
        # delete old listbox line
        listbox1.delete(index)
    except IndexError:
        index = tk.END
    # insert edited item back into listbox1 at index
    listbox1.insert(index, enter1.get())
    

def printer(event):
    print("Alccolselect=",listbox1.get(listbox1.curselection()))
 
# create the sample data file
filt_list = []
for i in range(50):
   filt_list.append(str(i+1))

filter_list=[]

root = tk.Tk()
root.title("Listbox Operations")
# create the listbox (note that size is in characters)
listbox1 = tk.Listbox(root, width=100, height=60)
listbox1.grid(row=0, column=0)
   
# create a vertical scrollbar to the right of the listbox
yscroll = tk.Scrollbar(command=listbox1.yview, orient=tk.VERTICAL)
yscroll.grid(row=0, column=1, sticky=tk.N+tk.S)
listbox1.configure(yscrollcommand=yscroll.set)
listbox1.bind("<<ListboxSelect>>", printer)

# use entry widget to display/edit selection
enter1 = tk.Entry(root, width=50, bg='yellow')
enter1.insert(0, 'Click on an item in the listbox')
enter1.grid(row=1, column=0)
# pressing the return key will update edited line
enter1.bind('<Return>', set_list)
# or double click left mouse button to update line
enter1.bind('<Double-1>', set_list)
# load the listbox with data
for item in filt_list:
    listbox1.insert(tk.END, item)
   
# left mouse click on a list item to display selection
listbox1.bind('<ButtonRelease-1>', get_list)


root.mainloop()
