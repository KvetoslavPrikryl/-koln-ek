from tkinter import *

window = Tk()
window.title("Úkolníček")
window.minsize(400,400)
window.iconbitmap("Tick-OK.ico")
window.resizable(False, False)

# Fonty a barvy
main_font = ("Times new Roman", 12)
main_color = "green"
button_coler = "#e2cff4"
window.config(bg=main_color)

# Funkce
def add_text():
    # přidání textu
    list_box.insert(END, user_input.get())
    user_input.delete(0, END)

def remove_text_item():
    list_box.delete(ANCHOR)

def clear_all_list():
    list_box.delete(0, END)

def save_tasks():
    with open("tasks.txt", "w") as file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                file.write(f"{one_task}")
            else:
                file.write(f"{one_task}\n")

def open_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for one_line in file:
                list_box.insert(END, one_line)
    except:
        print("Chyba! Zkontruljte funkci open_tasks, nebo soubor tasks.txt není založen!")

# Framy
imput_frame = Frame(window, bg=main_color)
text_frame = Frame(window, bg="white")
button_frame = Frame(window, bg=main_color)
imput_frame.pack()
text_frame.pack()
button_frame.pack()

# Imput frame obsah
user_input = Entry(imput_frame, width=35, borderwidth=3, font=main_font)
add_button = Button(imput_frame, text="Přidat", borderwidth=2, font=main_font, bg=button_coler, command=add_text)
user_input.grid(row=0, column=0, padx=5, pady=5, ipadx=10)
add_button.grid(row=0, column=1, padx=5, pady=5)

# scroolbar
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky=N+S)

# Text frame obsah
list_box = Listbox(text_frame, height=15, width=45, borderwidth=3, font=main_font, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)

# Propojení listboxu se scrollem
text_scrollbar.config(command=list_box.yview)

# Button frame obsah
remove_button = Button(button_frame, text="Odebrat položku", borderwidth=2, font=main_font, bg=button_coler, command=remove_text_item)
clear_button = Button(button_frame, text="Smazat seznam", borderwidth=2, font=main_font, bg=button_coler, command=clear_all_list)
save_button = Button(button_frame, text="Uložit", borderwidth=2, font=main_font, bg=button_coler, command=save_tasks)
quit_button = Button(button_frame, text="Zavřít", borderwidth=2, font=main_font, bg=button_coler, command=window.destroy)

remove_button.grid(row=0, column=0, padx=2, pady=10)
clear_button.grid(row=0, column=1,padx=2, pady=10)
save_button.grid(row=0, column=2, padx=2, pady=10, ipadx=8)
quit_button.grid(row=0, column=3, padx=2, pady=10, ipadx=8)

#Hlavní cyklus
open_tasks()
window.mainloop()