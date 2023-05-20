import tkinter as tk
from tkinter import messagebox
import random
import time

def check_input():
    global count, icount, idx, ln, start, end, words, word, new_str, i
    a = entry.get().split()[-1]
    b = words[word].split()[i]

    if a == b:
        count += 1
        new_str = new_str + b + ' '
        c = new_str + ' '.join(words[word].split()[i+1:])

        idx = words[word].index(b, idx+ln)
        ln = len(str(b))

        entry.delete(0, tk.END)
        entry.insert(tk.END, c)

        entry.tag_add("start", "1."+str(idx), "1."+str(idx+ln))
        entry.tag_config("start", foreground="green")

        # Move to the next word
        i += 1
        if i >= len(words[word].split()):
            i = 0
            word = random.randint(0, len(words)-1)
            label.config(text=words[word])
            entry.tag_config("start", foreground="black")

    else:
        icount += 1
        new_str = new_str + b + ' '
        c = new_str + ' '.join(words[word].split()[i+1:])

        idx = words[word].index(b, idx+ln)
        ln = len(str(b))

        entry.delete(0, tk.END)
        entry.insert(tk.END, c)

        entry.tag_add("start", "1."+str(idx), "1."+str(idx+ln))
        entry.tag_config("start", foreground="red")

def start_test():
    global words, word, count, icount, idx, ln, start, new_str, i
    words = [
        "The quick brown fox jumps over the lazy dog.",
        "Sphinx of black quartz, judge my vow.",
        "Pack my box with five dozen liquor jugs.",
        "How quickly daft jumping zebras vex.",
        "The five boxing wizards jump quickly."
    ]
    word = random.randint(0, len(words)-1)
    count = 0
    icount = 0
    idx = 0
    ln = 0
    start = time.time()
    new_str = ""
    i = 0

    label.config(text=words[word])
    entry.tag_config("start", foreground="black")

def finish_test():
    global end
    end = time.time()

    typed_entries = len(' '.join(entry.get().split()))
    time_in_min = (end - start) / 60
    result = int((typed_entries / 5) / time_in_min)

    # Display result in messagebox
    messagebox.showinfo('Result', "Your Typing Speed= "+str(result)+" wpm")

# creating window using gui
window = tk.Tk()
window.title('Typing Speed')
window.resizable(0, 0)

# define size of window
window.geometry("470x200")

x1 = tk.Label(window, text="Let's check your typing speed....", font="Arial 20")
x1.place(x=10, y=50)

label = tk.Label(window, text="", font="Arial 12", wraplength=400)
label.place(x=10, y=100)

entry = tk.Entry(window, width=50)
entry.place(x=10, y=140)
entry.focus()  # Set focus to the entry widget

b1 = tk.Button(window, text="Start", width=12, bg='white', fg="tomato", font="Algerian,10", command=start_test)
b1.place(x=200, y=170)

b2 = tk.Button(window, text="Finish", width=12, bg='white', fg="tomato", font="Algerian,10", command=finish_test)
b2.place(x=300, y=170)

window.protocol("WM_DELETE_WINDOW", finish_test)
window.mainloop()
