try:  # Python 2
    from Tkinter import *  # noqa
except ImportError:  # Python 3
    from tkinter import *  # noqa

from rectbutton import RectButton


class LockScreen(Frame):
    passcode = "8888"

    def __init__(self, master, succ_screen):
        self.entered_code = ""
        self.success_screen = succ_screen
        super(LockScreen, self).__init__(master)

        self.lbl = Label(self, text="Enter Passcode: ", font="Helvetica 24")
        numbtns = {}
        for i in range(10):
            numbtns[i] = RectButton(self, text="%d" % i, width=40, height=40, command=lambda x=i:self.handle_button_num(x))
        delbtn = RectButton(self, text="\u232b", width=40, height=40, command=self.handle_button_del)
        backbtn = RectButton(self, text="\u23ce", width=120, command=self.handle_button_back)
        self.lbl.grid(column=1, row=1, columnspan=4, padx=10, pady=10, sticky=N+W)
        for x in range(3):
            for y in range(3):
                numbtns[x+y*3+1].grid(column=x+1, row=y+2, padx=10, pady=10)
        numbtns[0].grid(column=2, row=5, padx=10, pady=10)
        delbtn.grid(column=3, row=5, padx=10, pady=10)
        backbtn.grid(column=3, row=9, columnspan=2, padx=10, pady=10, sticky=S+E)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(4, weight=1)
        self.rowconfigure(0, minsize=10)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, minsize=10)
        self.update_label()

    def update_label(self):
        self.lbl.config(text="Enter Passcode: %s" % ("*" * len(self.entered_code)))
        self.update()

    def handle_button_num(self, btnnum):
        self.entered_code += str(btnnum)
        if len(self.entered_code) == len(self.passcode):
            if self.entered_code == self.passcode:
                self.master.screen_pop()
                self.master.screen_push(self.success_screen)
            else:
                self.lbl.config(foreground="#f00")
                self.update_label()
                self.after(2000)
                self.entered_code = ""
                self.lbl.config(foreground="black")
        self.update_label()

    def handle_button_del(self):
        self.entered_code = self.entered_code[:-1]
        self.update_label()

    def handle_button_back(self):
        self.master.screen_pop()

