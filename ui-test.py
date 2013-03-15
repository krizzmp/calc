#!/usr/bin/env python
"""An example demonstrating usage of latexmath2png module for embedding math
equations in PyGTK
 
Author: Kamran Riaz Khan <krkhan@inspirated.com>
"""
 
from gi.repository import Gtk

class mathline(Gtk.EventBox):
	"""docstring for mathline"""
	editbox=None
	editimg=None
	resultimg=None
	button=None
	def __init__(self):
		super(mathline, self).__init__()
		self.connect("enter-notify-event", self.enter)
		self.connect("leave-notify-event", self.leave)
		self.editbox=Gtk.Entry()
		#self.editbox.connect("leave-notify-event", self.leave)
		self.button = Gtk.Button("Hello World")
		self.button2 = Gtk.Button("Hello World")
		#self.button2.connect("enter-notify-event", self.enter)

		self.line=Gtk.HBox()
		self.line.pack_start(self.button2,True,True,0)
		self.line.pack_end(self.button,True,True,0)
		self.add(self.line)
		self.editbox.show()

	def enter(self,g,h):
		print "foo"
		self.line.remove(self.button2)
		self.line.pack_start(self.editbox,True,True,0)
		

	def leave(self,g,h):
		print "left"
		if self.editbox.has
		self.line.remove(self.editbox)
		self.line.pack_start(self.button2,True,True,0)

 
def window_destroy(widget):
	Gtk.main_quit()


window = Gtk.Window()
window.set_border_width(10)
window.set_title('LaTeX Equations in GTK')
window.connect('destroy', window_destroy)

# grid = Gtk.Grid()
# window.add(grid)

# k=['1','2','3','4']

# for i, string in enumerate(k):
# 	button1 = Gtk.Button(label=string)
# 	button2 = Gtk.Button(label=string+'2')
# 	button1.set_hexpand ( True)
# 	grid.attach(button1, 1, i, 1, 1)
# 	grid.attach(button2, 2, i, 1, 1)
def testing(self):
	print 2
test=mathline()
test2=mathline()
thing=Gtk.VBox()
thing.add(test)
thing.add(test2)
thing.connect('destroy',testing)
window.add(thing)

 
window.show_all()
Gtk.main()