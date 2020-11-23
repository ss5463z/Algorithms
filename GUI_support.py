import sys

10
11
try:
    12
    import Tkinter as tk
13 except ImportError:
14
import tkinter as tk

15
16
try:
    17
    import ttk
18
py3 = False
19 except ImportError:
20
import tkinter.ttk as ttk

21
py3 = True
22
23


def set_Tk_var():
    24
    global TFL
    LINES


25
TFL
LINES = tk.StringVar()
26
global Station
A
27
Station
A = tk.StringVar()
28
global STATION
B
29
STATION
B = tk.StringVar()
30
global TFL
LINES
31
TFL
LINES = tk.StringVar()
32
global Station
A
33
Station
A = tk.StringVar()
34
global STATION
B
35
STATION
B = tk.StringVar()
36
37


def init(top, gui, *args, **kwargs):
    38
    global w, top_level, root


39
w = gui
40
top_level = top
41
root = top
42
43


def destroy_window():
    44  # Function which closes the window.


45
global top_level
46
top_level.destroy()
47
top_level = None
48
49
if __name__ == '__main__':
    50
    import GUI
51
GUI.vp_start_gui()