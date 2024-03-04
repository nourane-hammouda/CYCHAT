import sqlite3
import tkinter as tk
import thinker.messagebox as msgbox
conn = sqlite3.connect('chatapp.database')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY,
            name TEXT, 
            firstname TEXT,
            email, TEXT))''')

def insert_data(name, firstname, email): 
    with conn:
        c.execute("INSERT INTO users (name, firstname , email), VALUES (?, ?, ?)", (name, firstname, email))
root = tk.Tk() 
root.title("Base de donnée Chatify") 
root.config(bg='Cornsilk', borderwidth=20)
#nom_label
name_label = tk.Label(root, text="NOM", bg='Cornsilk', fg='black', borderwidth=15, font=('ds-digit', 15, 'bold')) 
name_label.grid(row=0, column=0)

#prenom_label
firstname_label = tk.Label(root, text="PRENOM", bg='Cornsilk', fg='black', borderwidth=15, font=('ds-digit', 15, 'bold'))
#prenom_entry

#prenom_entry 
firstname_entry = tk.Entry(root, font=('ds-digit', 15, 'bold'), borderwidth=5) 
firstname_entry.grid(row=1, column=1)

def submit_data():
    name = name_entry.get()
    firstname = firstname_entry.get()
    email = email_entry.get()

    if name == "" or firstname == "" or email == "":
        msgbox.showerror("Erreur", "Veuillez remplir tous les champs demandés.")
    else : 
        msgbox.showinfo("Information", "L'utilisateier a été enregistré.")
    insert_data(name, firstname, email)
    name_entry.delete(0, tk.END)
    firstname_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

submit_button = tk.Button(root, text="REGISTER", bg='Cornsilk', fg='black', borderwidth=5, font=('ds-digit', 15, 'bold'), command=submit_data)
submit_button.grid(row=6, column=1)

display_text=tk.Text(root, font=('ds-digit', 110, 'bold'))
display_text.grid(row=7, columnspan=2)

def show_data():
    with conn:
        c.execute("SELECT * FROM users")
        data = c.fetchall()
        display_text.delete("1.0", tk.END)
        for row in data:
            display_text.insert(tk.END, f"({row[0]} {row[1]} {row[2]} {row[3]}\n")
show_button = tk.Button(root, text="AFFICHER LES DONNEES", bg='Cornsilk', fg='black', borderwidth=5, font=('ds-digit', 15, 'bold'),command=show_data)
show_button.grid(row=8, columnspan=2)
#demarrer boucle principale
root.mainloop()



    
# Fermer la connexion
conn.close()
