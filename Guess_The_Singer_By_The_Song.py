import tkinter as tk
import random

root = tk.Tk()

root.title("Guess The Singer By The Song")

song_dict = {'I Gotta Feeling': 'the black eyed peas',
             "Rockstar": "post malone",
             "Old Town Road": "lil nas x",
             "Truth Hurts": "lizzo",
             "One Dance": "drake",
             "Super Base": "nicki minaj",
             'Fake Love': 'bts',
             'Photoshop': 'tita',
             "Panini": "lil nas x",
             "Lover": "taylor swift",
             "Wow": "post malone",
             "Make It Right": "bts",
             "Bad guy": "Bilie eilish",
             "circles": "post malone",
             "24k magic": "bruno mars",
             "liar": "camila cabello",
             "In my feelings": "drake",
             "Sweet but psycho": "ava max",
             "Kill this love": "blackpink",
             "Antilopa": "tita",
             "Not Today": "bts"}

dictsongvar = tk.StringVar()
guesssongvar = tk.StringVar()
resultvar = tk.StringVar()

# transforming to readable format
dictword = dictsongvar.get()
dictword = random.choice(list(song_dict.keys()))
dictsongvar.set(dictword)
failures = []
answer = False

def counter():
    failures.append(1)

def check():
    guessword = guesssongvar.get()
    guessword = guessword.lower()
    result = resultvar.get()
    if song_dict[dictword] == guessword:
        global answer
        answer = True
        result = ('That\'s right!')
        failures.clear()
    elif song_dict[dictword] != guessword:
        counter()
        result = ('You didn\'t guess the singer! The attempt #' + str(sum(failures)) + '\nTry again')

    resultvar.set(result)

def newsong():
    global dictword
    global answer
    failures.clear()
    guesssongvar.set("")
    resultvar.set("")
    dictword = random.choice(list(song_dict.keys()))
    dictsongvar.set(dictword)
    guesssongvar.set("")
    resultvar.set("")


def quit():
    root.destroy()

frame = tk.Frame(root,bg='light goldenrod yellow')
frame.pack()
songlabel = tk.Label(frame, width=70, textvariable=dictsongvar, bg='light goldenrod yellow')
songlabel.pack()
songentry = tk.Entry(frame, width=30, textvariable=guesssongvar)
songentry.pack()
resultlabel = tk.Label(frame, textvariable=resultvar, bg='light goldenrod yellow')
resultlabel.pack()
tk.Button(frame, text='Check', width=20, font='arial 10', bg='light goldenrod yellow', command=check).pack()
tk.Button(frame, text='New song', width=20, font='arial 10', bg='light goldenrod yellow', command=newsong).pack()
tk.Button(frame, text='Quit', width=20, font='arial 10', bg='light goldenrod yellow', command=quit).pack()
root.mainloop()
