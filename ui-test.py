#!/usr/bin/env python
"""An example demonstrating usage of latexmath2png module for embedding math
equations in PyGTK
 
Author: Kamran Riaz Khan <krkhan@inspirated.com>
"""
 
import gtk

 
def window_destroy(widget):
	gtk.main_quit()

def add_eq(self):
	something=gtk.Button("I'm new!")
	something.show()
	vbox.remove(self)
	something.connect('clicked', add_eq)
	vbox.pack_start(something)
window = gtk.Window()
window.set_border_width(10)
window.set_title('LaTeX Equations in GTK')
window.connect('destroy', window_destroy)
vbox = gtk.VBox(spacing = 10)
window.add(vbox)

btn_add_eq=gtk.Button('new equation')
btn_add_eq.connect('clicked', add_eq)
vbox.pack_start(btn_add_eq)

 
window.show_all()
gtk.main()