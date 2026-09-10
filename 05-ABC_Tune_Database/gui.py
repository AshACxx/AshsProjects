import tkinter as tk
from tkinter import scrolledtext
from analysis import get_tunes_by_book, get_tune, search

#tkinter menu
def launch_gui(df):

    #main window
    my_w = tk.Tk()
    my_w.title("ABC Tune Database")

    my_w.geometry("750x600")
    #adding a text and scroll widget to the main box (my_W) -> acts as the root
    output = scrolledtext.ScrolledText(my_w, width=90, height=25)
    #pady is padding for the main window, moves it away from the top of the titlebar
    output.pack(pady=10)

    def show(df):
        #clears text box (1.0 is line1 char 0 tk.END _> to the end)
        output.delete(1.0, tk.END)

        if df.empty:
            #if the df has no rows/ data it displays no (#note for future tk.END is used to place no results at the end of widget)
            output.insert(tk.END, "No results found.\n")
            #returning no result to df
            return

        for i, row in df.iterrows():
            #outputting (printing) the rows in the main window
            #insert -> tk.END = appending the text to the end of the text box
            output.insert(tk.END, f"Title: {row['title']}\n")

            output.insert(tk.END, f"Type: {row['type']}\n")

            output.insert(tk.END, f"Key: {row['key']}\n")

            output.insert(tk.END, f"Book: {row['book_number']}\n")

            #adding lines to seperate 
            output.insert(tk.END, "-"*50 + "\n")


    #search by book number
    #.pack is used to horiztonally or vertically place the widgets after another 
    #.pack() lets me stack the name and asearch bar on top of eachother

    tk.Label(my_w, text="Search by Book Number:", font=("Arial",10)).pack()

    #entry creates an input box 
    book_entry = tk.Entry(my_w)
    book_entry.pack()

    #creating a button, using lambda to create a mini function name (tkinter cant take calls) inserting the dataframe and using .get() to return the specified key
    #FOR FUTURE: user types into entry > when u click the button mini funcyion runs > returns number > get_tunes_by_book filters dataframe to book (1)or(2)

    tk.Button(my_w, text="Search", command=lambda:show(get_tunes_by_book(df, int(book_entry.get())))).pack()

    #search by tune type
    tk.Label(my_w, text="\nSearch by Type:").pack()
    type_entry = tk.Entry(my_w)

    type_entry.pack()
    tk.Button(my_w, text="Search", command=lambda: show(get_tune(df, type_entry.get()))).pack()

    # Search by title
    tk.Label(my_w, text="\nSearch by Title:").pack()
    title_entry = tk.Entry(my_w)
    title_entry.pack()
    tk.Button(my_w, text="Search", command=lambda: show(search(df, title_entry.get()))).pack()

    my_w.mainloop()
