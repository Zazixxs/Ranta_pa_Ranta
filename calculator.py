import tkinter
import customtkinter

def calculate_and_display():
    try:
        savings = int(entryMonth.get())
        years = int(entryYear.get())
        interest = int(entryProcent.get())
    except ValueError:
        outputTextbox.delete("1.0", tkinter.END)
        outputTextbox.insert(tkinter.END, "Felaktig inmatning. Ange numeriska värden.")
        return

    total = 0
    for i in range(years * 12):  # Assume that savings occur monthly
        total *= 1 + interest / 100 / 12  # Compound interest calculated monthly
        total += savings  # Add monthly savings
    outputTextbox.delete("1.0", tkinter.END)
    outputTextbox.insert(tkinter.END, f"Ditt totala sparande att vara: {total} kr")





app = tkinter.Tk()
app.geometry("600x600")
app.title("Ränta på Ränta")


#Month
labelMonth = customtkinter.CTkLabel(master=app,
                               text="Månads sparande",
                               width=120,
                               height=25,
                               corner_radius=8)
labelMonth.place(relx=0, rely=0, anchor=tkinter.NW)

entryMonth = customtkinter.CTkEntry(master=app,
                               width=120,
                               height=25,
                               corner_radius=10)
entryMonth.place(relx=0, rely=0.05, anchor=tkinter.NW)

#Year
labelYear = customtkinter.CTkLabel(master=app,
                               text="Antal År",
                               width=120,
                               height=25,
                               corner_radius=8)
labelYear.place(relx=0, rely=0.1, anchor=tkinter.NW)

entryYear = customtkinter.CTkEntry(master=app,
                               width=120,
                               height=25,
                               corner_radius=10)
entryYear.place(relx=0, rely=0.15, anchor=tkinter.NW)

#Interest
labelProcent = customtkinter.CTkLabel(master=app,
                               text="Procent per år",
                               width=120,
                               height=25,
                               corner_radius=8)
labelProcent.place(relx=0, rely=0.2, anchor=tkinter.NW)

entryProcent = customtkinter.CTkEntry(master=app,
                               width=120,
                               height=25,
                               corner_radius=10)
entryProcent.place(relx=0, rely=0.25, anchor=tkinter.NW)

#Calculate button
calculateButton = tkinter.Button(app, text="Beräkna", command=calculate_and_display)
calculateButton.place(relx=0, rely=0.3, anchor=tkinter.NW)

#Output textbox
#Output textbox
outputTextbox = tkinter.Text(app)
outputTextbox.place(relx=0, rely=0.35, anchor=tkinter.NW)


app.mainloop()
