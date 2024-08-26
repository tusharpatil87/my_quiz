from tkinter import *
import requests
import os


CWD = os.getcwd()
# print(f"CWD is:\n{CWD}")
background_img_name = "background.png"
bg_img_path = os.path.join(CWD,background_img_name)
photo_img = "kanye.webp"
photo_img_path = os.path.join(CWD,photo_img)

def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()["quote"]
    print(f"{data}")
    canvas.itemconfig(quote_text, text=data)


    #Write your code here.



window = Tk()
window.title("Harsh Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file=bg_img_path)
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Harsh's Quote Goes HERE", width=250, font=("Arial", 20, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file=photo_img_path, height= 350,width= 340)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()