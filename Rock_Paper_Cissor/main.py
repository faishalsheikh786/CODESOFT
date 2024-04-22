import random
from tkinter import *
from PIL import Image, ImageTk


user_score = 0
computer_score = 0


root = Tk()
frame = Frame(root)
frame.grid(padx=20, pady=20)
root.title("Rock Paper Scissor Game")


def disable_btn():
    rock_btn.config(state="disable")
    paper_btn.config(state="disable")
    scissor_btn.config(state="disable")


def enable_btn():
    rock_btn.config(state="normal")
    paper_btn.config(state="normal")
    scissor_btn.config(state="normal")


def play_again():
    user_label.config(image=user_img)
    computer_label.config(image=robot_img)
    display_label.config(text="")
    enable_btn()


def reset():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_label.config(image=user_img)
    computer_label.config(image=robot_img)
    computer_score_label.config(text="Score")
    user_score_label.config(text="Score")
    display_label.config(text="")
    enable_btn()


def select_rock_image():
    if computer_score_label["text"]=="Score":
        computer_score_label.config(text=0)
    if user_score_label["text"]=="Score":
        user_score_label.config(text=0)
    images_list = [rock_img, paper_img, scissor_img]
    computer_image = random.choice(images_list)
    global user_score, computer_score
    disable_btn()
    user_label.config(image=rock_img)
    computer_label.config(image=computer_image)
    if computer_image==rock_img:
        display_label.config(text="Tie")
    elif computer_image==paper_img:
        display_label.config(text="You Lose")
        computer_score+=1
        computer_score_label.config(text=computer_score)
    elif computer_image==scissor_img:
        display_label.config(text="You Win")
        user_score+=1
        user_score_label.config(text=user_score)
    
    print(f"User Score : {user_score}    Computer Score : {computer_score}")

def select_paper_image():
    if computer_score_label["text"]=="Score":
        computer_score_label.config(text=0)
    if user_score_label["text"]=="Score":
        user_score_label.config(text=0)
    images_list = [rock_img, paper_img, scissor_img]
    computer_image = random.choice(images_list)
    global user_score, computer_score
    disable_btn()
    user_label.config(image=paper_img)
    computer_label.config(image=computer_image)
    if computer_image==rock_img:
        print("You Win")
        display_label.config(text="You Win")
        user_score+=1
        user_score_label.config(text=user_score)
    elif computer_image==paper_img:
        display_label.config(text="Tie")
    elif computer_image==scissor_img:
        display_label.config(text="You Lose")
        computer_score+=1
        computer_score_label.config(text=computer_score)
    print(f"User Score : {user_score}    Computer Score : {computer_score}")

def select_scissor_image():
    if computer_score_label["text"]=="Score":
        computer_score_label.config(text=0)
    if user_score_label["text"]=="Score":
        user_score_label.config(text=0)
    images_list = [rock_img, paper_img, scissor_img]
    computer_image = random.choice(images_list)
    global user_score, computer_score
    disable_btn()
    user_label.config(image=scissor_img)
    computer_label.config(image=computer_image)
    if computer_image==rock_img:
        display_label.config(text="You Lose")
        computer_score+=1
        computer_score_label.config(text=computer_score)
    elif computer_image==paper_img:
        display_label.config(text="You Win")
        user_score+=1
        user_score_label.config(text=user_score)
    elif computer_image==scissor_img:
        display_label.config(text="Tie")
    print(f"User Score : {user_score}    Computer Score : {computer_score}")


robot_img = ImageTk.PhotoImage(Image.open("robot_avatar.png").resize((300,300)))
user_img = ImageTk.PhotoImage(Image.open("user_avatar.png").resize((300,300)))
rock_img = ImageTk.PhotoImage(Image.open("Rock.png").resize((300,300)))
paper_img = ImageTk.PhotoImage(Image.open("Paper.png").resize((300,300)))
scissor_img = ImageTk.PhotoImage(Image.open("Scissor.png").resize((300,300)))


label1 = Label(frame, text="Computer", font=("Arial",25,"bold")).grid(row=0, column=1, pady=10)
label2 = Label(frame, text="Player", font=("Arial",25,"bold")).grid(row=0, column=5, pady=10)

computer_label = Label(frame, image=robot_img)
computer_label.grid(row=1, column=1, padx=10)


user_label = Label(frame, image=user_img)
user_label.grid(row=1, column=5, padx=10) 

display_label = Label(frame, text="", font=("Arial",20,"bold"))
display_label.grid(row=1, column=3)

computer_score_label = Label(frame, text="Score", font=("Arial",20,"bold"))
computer_score_label.grid(row=2, column=1, pady=5)
user_score_label = Label(frame, text="Score", font=("Arial",20,"bold"))
user_score_label.grid(row=2, column=5, pady=5)


rock_btn = Button(frame, width=20, height=2, text="Rock", font=("Arial",10,"bold"), bd=3, command=select_rock_image)
paper_btn = Button(frame, width=20, height=2, text="Paper", font=("Arial",10,"bold"), bd=3, command=select_paper_image)
scissor_btn = Button(frame, width=20, height=2, text="Scissor", font=("Arial",10,"bold"), bd=3, command=select_scissor_image)
play_again_btn = Button(frame, width=63, height=2, text="Play Again", font=("Arial",10,"bold"), bd=3, command=play_again)
reset_btn = Button(frame, width=63, height=2, text="Reset All", font=("Arial",10,"bold"), bd=3, command=reset)


rock_btn.grid(row=3, column=2)
paper_btn.grid(row=3, column=3)
scissor_btn.grid(row=3, column=4)
play_again_btn.grid(row=4, column=2, columnspan=3, pady=5)
reset_btn.grid(row=5, column=2, columnspan=3, pady=5)


root.mainloop()

