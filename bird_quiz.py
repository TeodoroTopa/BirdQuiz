# Python program to create a simple GUI
# Simple Quiz using Tkinter

import pandas as pd
import numpy as np 
import random
import json


#import everything from tkinter
from tkinter import *

# and import messagebox as mb from tkinter
from tkinter import messagebox as mb

#import json to use json file for data
import json

from PIL import Image, ImageTk

#class to define the components of the GUI
class Quiz:
    # This is the first method which is called when a
    # new object of the class is initialized. This method
    # sets the question count to 0. and initialize all the
    # other methoods to display the content and make all the
    # functionalities available
    def __init__(self):

        # set question number to 0
        self.q_no= 0

        #bird image
        self.bird_image = Image.open(image[str(self.q_no)])
        self.final_bird_image = ImageTk.PhotoImage(self.bird_image)
        
        # assigns ques to the display_question function to update later.
        self.display_title()
        self.display_question()
        
        # opt_selected holds an integer value which is used for
        # selected option in a question.
        self.opt_selected=IntVar()
        
        # displaying radio button for the current question and used to
        # display options for the current question
        self.opts=self.radio_buttons()
        
        # display options for the current question
        self.display_options()
        
        # displays the button for next and exit.
        self.buttons()

        #entry = Entry(gui, width= 40)
        #entry.focus_set()
        #entry.pack()
        
        # no of questions
        self.data_size=len(question)
        #self.data_size = entry.get()
        
        # keep a counter of correct answers
        self.correct=0


    # This method is used to display the result
    # It counts the number of correct and wrong answers
    # and then display them at the end as a message Box
    def display_result(self):
        
        # calculates the wrong count
        wrong_count = self.data_size - self.correct
        correct = f"Correct: {self.correct}"
        wrong = f"Wrong: {wrong_count}"
        
        # calcultaes the percentage of correct answers
        score = int(self.correct / self.data_size * 100)
        result = f"Score: {score}%"
        
        # Shows a message box to display the result
        mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):
        
        # checks for if the selected option is correct
        if self.opt_selected.get() == answer[str(q_no)]:
            # if the option is correct it return true
            return True
        else:
            mb.showinfo("INCORRECT", "Incorrect! That was a" + species[str(q_no)])
            return False

    # This method is used to check the answer of the
    # current question by calling the check_ans and question no.
    # if the question is correct it increases the count by 1
    # and then increase the question number by 1. If it is last
    # question then it calls display result to show the message box.
    # otherwise shows next question.
    def next_btn(self):
        
        # Check if the answer is correct
        if self.check_ans(self.q_no):
            
            # if the answer is correct it increments the correct by 1
            self.correct += 1
        
        # Moves to next Question by incrementing the q_no counter
        self.q_no += 1
        
        # checks if the q_no size is equal to the data size
        if self.q_no==self.data_size:
            
            # if it is correct then it displays the score
            self.display_result()
            
            # destroys the GUI
            gui.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()


    # This method shows the two buttons on the screen.
    # The first one is the next_button which moves to next question
    # It has properties like what text it shows the functionality,
    # size, color, and property of text displayed on button. Then it
    # mentions where to place the button on the screen. The second
    # button is the exit button which is used to close the GUI without
    # completing the quiz.
    def buttons(self):
        
        # The first button is the Next button to move to the
        # next Question
        next_button = Button(gui, text="Next",command=self.next_btn,
        width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
        
        # placing the button on the screen
        next_button.place(x=350,y=380)
        
        # This is the second button which is used to Quit the GUI
        quit_button = Button(gui, text="Quit", command=gui.destroy,
        width=5,bg="black", fg="white",font=("ariel",16," bold"))
        
        # placing the Quit button on the screen
        quit_button.place(x=700,y=50)


    # This method deselect the radio button on the screen
    # Then it is used to display the options available for the current
    # question which we obtain through the question number and Updates
    # each of the options for the current question of the radio button.
    def display_options(self):
        val=0
        
        # deselecting the options
        self.opt_selected.set(0)
        
        # looping over the options to be displayed for the
        # text of the radio buttons.
        for option in options[str(self.q_no)]:
            self.opts[val]['text']=option
            val+=1


    # This method shows the current Question on the screen
    def display_question(self):

        filename = image[str(self.q_no)]

        self.bird_image = Image.open(filename)
        self.final_bird_image = ImageTk.PhotoImage(self.bird_image)

       # image_label = Label(gui, image = self.final_bird_image)
        
        # setting the Question properties
        q_no = Label(gui, text=question[str(self.q_no)], width=60,
        font=( 'ariel' ,16, 'bold' ), anchor= 'w')

        #placing the option on the screen
        q_no.place(x=70, y=100)

        
        canvas = Canvas(gui, width=300, height=300)
        canvas.place(relx=0.65, rely=0.5, anchor=CENTER)
        bimg = canvas.create_image((100,100), image=self.final_bird_image)




    # This method is used to Display Title
    def display_title(self):
        
        # The title to be shown
        title = Label(gui, text="Kenyan Bird Quiz",
        width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
        
        # place of the title
        title.place(x=0, y=2)


    # This method shows the radio buttons to select the Question
    # on the screen at the specified position. It also returns a
    # list of radio button which are later used to add the options to
    # them.
    def radio_buttons(self):
        
        # initialize the list with an empty list of options
        q_list = []
        
        # position of the first option
        y_pos = 150
        
        # adding the options to the list
        while len(q_list) < 4:
            
            # setting the radio button properties
            radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
            value = len(q_list)+1,font = ("ariel",14))
            
            # adding the button to the list
            q_list.append(radio_btn)
            
            # placing the button
            radio_btn.place(x = 100, y = y_pos)
            
            # incrementing the y-axis position by 40
            y_pos += 40
        
        # return the radio buttons
        return q_list

# Create a GUI Window
gui = Tk()

# set the size of the GUI Window
gui.geometry("800x450")

# set the title of the Window
gui.title("Kenyan Bird Quiz")

# load bird data, shuffle it, add option and question columns.
df = pd.read_csv('bird_data_clean.csv')

df = df[df["image_url"].str.contains("www.inaturalist")==False]
df.reset_index(inplace=True, drop=True)

options = []

for i in range(len(df)):
    
    temp = list(df['species'])
    
    if i < (len(df)-1):
        ans = temp.pop(i)
    else: 
        ans = temp.pop()
    
    choices = random.choices( temp, k=3 )
    
    choices.append(ans)
    
    random.shuffle(choices)
    
    options.append(choices)
    
df['options'] = options

df['answer'] = [ (df['options'][i].index(df['species'][i])) + 1 for i in range(len(df)) ]
df['question'] = ['What bird is this?' for i in range(len(df))]
df['image_filename'] = 'bird_pics\\full\\' + df['image_filename'].astype(str)

df2 = df.sample(frac=0.03)
df2.reset_index(inplace=True, drop=True)

df2.to_json('json_questions.json', orient='columns')

# get the data from the json file
with open('json_questions.json') as f:
    data = json.load(f)

# set the question, options, and answer
question = (data['question'])
image = (data['image_filename'])
options = (data['options'])
answer = (data[ 'answer'])
species = (data['species'])

# create an object of the Quiz Class.
quiz = Quiz()

# Start the GUI
gui.mainloop()

# END OF THE PROGRAM
