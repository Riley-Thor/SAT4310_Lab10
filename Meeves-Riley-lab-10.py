"""

Lab 10: A simple calculator using Tkinter

Course Name : SAT 4310 Advanced Scripting Programming

Semester : Fall 2023

Author : Riley Meeves

Assignment : Lab 10

Date: 11/17/23

"""

# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression in the text entry box
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)
# Function to clear the contents of text entry box
def clear():
	global expression
	expression = ""
	equation.set("")
# Function to evaluate the final expression
def equalpress():
	global expression
	total = str(eval(expression))
	equation.set(total)
	# initialize the expression variable by empty string
	expression = ""

#%% Fill with the Python statements for Questions 1 - 10

# Q1. create a GUI root window

root = Tk()

# Q2. set the background colour of root window as "light gray"

root.configure(bg='light gray')
    
# Q3. set the title of root window as "Simple Calculator"

root.title('Simple Calculator')
   
# Q4. set the configuration of root window to the size of 328x160

root.geometry('328x160')
   
# StringVar() is the variable class
equation = StringVar()
   
# Q5. create the text entry box for showing the expression.
#  1) set textvariable parameter as 'equation' and set the font size to 12.
#  2) return the Entry widget to the variable named 'expression_field',
#such as, expression_field = Entry(....)

expression_field = Entry(root, textvariable=equation, font=12)
   
# use grid method to place the widgets at respective positions
expression_field.grid(columnspan=4, ipadx=73)



   
'''create a Buttons and place at a particular location inside the root window .
# when user press the button, the command or function affiliated to that button is executed.
'''
# Create the first button for the digit '1' in the calculator with following 
#specification: 
    # 1) font size 12, 
    # 2) foreground color: black
    # 3) background color: dark gray
    # 4) command=lambda: press(1)
    # 5) height: 1
    # 6) width: 7
button1 = Button(root, text=' 1 ', font = 12, fg='black', bg='dark gray',
   					command=lambda: press(1), height=1, width=7)
# set the location of button to: row 2 and column 0
button1.grid(row=2, column=0)


# Q6. follow the above example, create Nine different buttons for the digits from '2' - '9' and '0' with following 
#specification: 
    # 1) font size 12, 
    # 2) foreground color: black
    # 3) background color: dark gray
    # 4) command=lambda: press(n), n needs be replaced by the digit 2,3,..,9,0 in the corresponding buttons
    # 5) height: 1
    # 6) width: 7
    # 7) location: row number and column number need to be changed for the in the corresponding buttons.
                   # for example, for the digit 2: row=2, column=1
button2 = Button(root, text=' 2 ', font = 12, fg='black', bg='dark gray',
   					command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)
button3 = Button(root, text=' 3 ', font = 12, fg='black', bg='dark gray',
   					command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)
button4 = Button(root, text=' 4 ', font = 12, fg='black', bg='dark gray',
   					command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)
button5 = Button(root, text=' 5 ', font = 12, fg='black', bg='dark gray',
   					command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)
button6 = Button(root, text=' 6 ', font = 12, fg='black', bg='dark gray',
   					command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)
button7 = Button(root, text=' 7 ', font = 12, fg='black', bg='dark gray',
   					command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)
button8 = Button(root, text=' 8 ', font = 12, fg='black', bg='dark gray',
   					command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)
button9 = Button(root, text=' 9 ', font = 12, fg='black', bg='dark gray',
   					command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)
button0 = Button(root, text=' 0 ', font = 12, fg='black', bg='dark gray',
   					command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)
# Create a button for the symbol '+' in the calculator with following 
#specification: 
    # 1) font size 12, 
    # 2) foreground color: black
    # 3) background color: light green
    # 4) command=lambda: press("+")
    # 5) height: 1
    # 6) width: 7
    # 7) location: row=2, column=3

plus = Button(root, text=' + ', font = 12, fg='black', bg='light green',
				command=lambda: press("+"), height=1, width=7)
plus.grid(row=2, column=3)



# Q7. Create a button for the symbol '-' in the calculator with following 
#specification: 
    # 1) font size 12, 
    # 2) foreground color: black
    # 3) background color: light green
    # 4) command=lambda: press("-")
    # 5) height: 1
    # 6) width: 7
    # 7) location: row=3, column=3

minus = Button(root, text=' - ', font = 12, fg='black', bg='light green',
				command=lambda: press("-"), height=1, width=7)
minus.grid(row=3, column=3)

   
#  Create a button for the symbol '*' in the calculator
multiply = Button(root, text=' * ', font = 12,fg='black', bg='light green',
   					command=lambda: press("*"), height=1, width=7)
multiply.grid(row=4, column=3)
   
#  Create a button for the symbol '/' in the calculator
divide = Button(root, text=' / ', font = 12,fg='black', bg='light green',
   					command=lambda: press("/"), height=1, width=7)
divide.grid(row=5, column=3)
   
# Q8. Create a button for the symbol '=' in the calculator with following 
#specification: 
    # 1) font size 12, 
    # 2) foreground color: black
    # 3) background color: light green
    # 4) command=equalpress 
    # 5) height: 1
    # 6) width: 7
    # 7) location: row=5, column=2
    
equal = Button(root, text=' = ', font = 12, fg='black', bg='light green',
				command=equalpress, height=1, width=7)
equal.grid(row=5, column=2)    
    

   
   
# Q9. Create a button for the 'Clear' in the calculator with following 
#specification: 
    # 1) font size 12, 
    # 2) foreground color: black
    # 3) background color: light green
    # 4) command=clear 
    # 5) height: 1
    # 6) width: 7
    # 7) location: row=5, column=1
clear = Button(root, text='Clear', font = 12,fg='black', bg='light green',
   				command=clear, height=1, width=7)
clear.grid(row=5, column='1')
   

# Q10. set infinite loop for GUI continuous display

root.mainloop()


'''
---

## **Q11. uploading your work**

1. Make sure your exercise python file has the correct name: `<your LastName_FirstName>-lab-9.py`. (You won't get credit for your hard work otherwise.)
2. Open [Canvas](https://mtu.instructure.com/) and log in.
3. Go to the assignment for this week, hit submit, and upload your lab from your computer.

---

Good job, and see you next week.
'''
