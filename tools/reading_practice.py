'''
Shows characters to a user, allowing them to practice reading.
Currently the characters are chosen randomly, so the sentence generally won't
make sense.

To get characters from pinyin:
https://www.chinese-tools.com/tools/ime.html
To get Unicode from characters:
https://www.chinese-tools.com/tools/converter-unicode.html
'''
import tkinter
import random

root = tkinter.Tk()
root.title('Character Practice')
tcl = tkinter.Tcl()

characters = []
with open('characters.txt') as c:
    for ch in c:
        characters.append(chr(int(ch)))


def update_text():
    new_chars = ''.join(random.choices(characters, k=random.randint(1, 5)))
    # print('New characters:', new_chars)
    text.configure(text=new_chars)


def key(event):
    update_text()


root.state('zoomed')  # set window full screen
text = tkinter.Label(root, height=3, width=8, font=("SimSun", 200))
text.pack(fill='both', expand=True)
text.bind("<Key>", key)  # event for when any key is pressed
text.focus_set()
tcl.after(0, update_text)

root.mainloop()
