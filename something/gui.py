import tkinter
top = tkinter.Tk()
top.title("Moje pierwsze gui")
label = tkinter.Label( top, text = "Witaj Świecie programowania\nCo swym urokiem nas zabawia\nCo otwiera nowe możliwości\nZ binarnych liczb złożoności" )
label.pack() # podpinanie kontrolki pod okno
top.mainloop()