import tkinter as tk  # Impordib Tkinteri teegi ja annab sellele lühendi tk


root = tk.Tk()  # Loob programmi põhiakna
root.title("Greeting")  # Määrab akna pealkirjaks "Greeting"
root.geometry("500x300")  # Määrab akna suuruseks 500 x 300 pikslit
root.grid_columnconfigure(0, weight=1)
# Lubab veerul 0 akna suurenedes rohkem ruumi kasutada


def say_hello():
    # Funktsioon käivitub siis, kui kasutaja vajutab nuppu "Click me"

    greeting_lable.config(text="Hello, world!")
    # Muudab Labeli teksti väärtuseks "Hello, world!"


def greet_user():
    # Funktsioon käivitub siis, kui kasutaja vajutab nuppu "Greet me"

    name = name_input.get()
    # Loeb Entry sisestusväljast kasutaja kirjutatud teksti
    # ja salvestab selle muutujasse name

    greeting_lable.config(text=f"Hello, {name}!")
    # Muudab Labeli teksti
    # Näiteks kui kasutaja sisestab "Sander",
    # kuvatakse "Hello, Sander!"


greeting_lable = tk.Label(
    root,
    text="nothing to see here yet"
)
# Loob tekstisildi ehk Labeli
# root tähendab, et Label kuulub põhiaknasse
# text määrab algselt kuvatava teksti

greeting_lable.grid(row=0, column=0, pady=10)
# Paigutab Labeli grid-paigutuses reale 0 ja veergu 0
# pady=10 lisab vertikaalselt veidi tühja ruumi


hello_button = tk.Button(
    root,
    text="Click me",
    command=say_hello
)
# Loob nupu tekstiga "Click me"
# command=say_hello tähendab, et nupule vajutades
# käivitatakse funktsioon say_hello

hello_button.grid(row=1, column=0, pady=10)
# Paigutab nupu reale 1 ja veergu 0


name_input = tk.Entry(root, width=30)
# Loob tekstisisestusvälja
# width=30 määrab välja ligikaudse laiuse

name_input.grid(row=2, column=0, pady=10)
# Paigutab sisestusvälja reale 2 ja veergu 0


greet_button = tk.Button(
    root,
    text="Greet me",
    command=greet_user
)
# Loob teise nupu
# command=greet_user määrab, et nupule vajutamisel
# käivitatakse greet_user funktsioon

greet_button.grid(row=3, column=0, pady=10)
# Paigutab nupu reale 3 ja veergu 0


root.mainloop()
# Käivitab Tkinteri sündmuste tsükli
# Programm jääb ootama kasutaja tegevusi:
# näiteks nupule vajutamist või teksti sisestamist