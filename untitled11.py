from tkinter import*
import random

root.Tk()
root.title("List")
root.geometry("550x300")

label_list=Label(root)
label_item=Label(root)

list_items=["Bottle", "Tiffin", "ID card", "chocolate", "Chips", "Hanky", "Ticket"]

label_list["text"]="Listed items: "+str(list_items)

def bag_the_items():
    random_item=random.sample(range(1, 7),1)
    label_item["text"]="put item no. "+str(random_item)+" in the bag"
    
label_list.place(relx=0.5,rely=0.4,anchor=CENTER)

btn=Button(root, text="Which item to put in the bag?", command=bag_the_items)

btn.place(relx=0.5,rely=0.5,anchor=CENTER)

label_item.place(relx=0.5,rley=0.6,anchor=CENTER)

root.mainloop()