#!/usr/bin/env python
"""an attempt to create the interface for calc
Author: Kristoffer Petersen <krizzmp@gmail.com>
"""
 
from gi.repository import Gtk
import os
import latexmath2png

class mathline(Gtk.EventBox):
	"""docstring for mathline"""
	def __init__(self):
		super(mathline, self).__init__()
		self.connect("enter-notify-event", self.enter)
		
		self.line=Gtk.HBox()
		self.btn=Gtk.Image.new_from_file("none")
		self.line.add(self.btn)
		self.edit=Gtk.Entry()
		self.edit.connect("focus-out-event", self.updateimg)
		self.line.add(self.edit)
		self.btn.hide()
		self.add(self.line)
		self.line.show()
		self.edit.show()
		self.show()


	def enter(self,g,h):
		for x in test:
			if x!=self and not x.edit.is_focus():
				x.edit.hide()
				x.btn.show()
		self.edit.show()
		self.btn.hide()
	
	def updateimg(self,g,h):
		if self.edit.get_text():
			latexmath2png.math2png([self.edit.get_text()], os.getcwd(), prefix = "pre")
			self.btn.set_from_file('pre1.png')
		self.btn.show()
		self.edit.hide()


 
def window_destroy(widget):
	try:
		os.unlink(os.path.join(os.getcwd(), 'pre1.png' ))
	except:
		print "boo"
	Gtk.main_quit()


window = Gtk.Window()
window.set_border_width(10)
window.set_title('LaTeX Equations in GTK')
window.connect('destroy', window_destroy)

def teste(self):
	test[0].createimg()

test=[]
test.append(mathline())
test.append(mathline())
thing=Gtk.VBox()
thing.add(test[0])
thing.add(test[1])
btnimg=Gtk.Button('create img')
btnimg.connect('clicked',teste)
btnimg.show()
thing.add(btnimg)
thing.show()
window.add(thing)

 
window.show()
Gtk.main()