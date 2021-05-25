import tkinter as tk
import time

BASE_BACKGROUND = '#292929'
HEADER_BASE_COLOR = '#F5F5F5'
HEADER_BASE_COLOR = '#F5F5F5'
HEADER_COLOR_PRIMARY = '#1c1c1c'
HEADER_COLOR_SECONDARY = '#8ec63e'

def Header_Menu_Animation(app):
	
	Header_Frame = tk.Frame(app, background = HEADER_BASE_COLOR)
	Header_Frame.place(relx=0.0 , rely= 0.0 , relheight= 0.2 ,relwidth= 1 )
	n = 0.0
	while True:
		n += 0.08
		time.sleep(0.04)
		Header_Frame.place(relx=0.0 , rely= 0.0 , relheight= n ,relwidth= 1 )
		Header_Frame.update()
		if n >= 1.0:
			return Header_Frame
			break