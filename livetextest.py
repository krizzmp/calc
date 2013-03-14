#!/usr/bin/env python
"""An example demonstrating usage of latexmath2png module for embedding math
equations in PyGTK
 
Author: Kamran Riaz Khan <krkhan@inspirated.com>
"""
 
import gtk
import os
import latexmath2png
 
pre = 'gtktex_'
eqs = [
	r'$\alpha_i > \beta_i$',
	r'$\sum_{i=0}^\infty x_i$',
	r'$\left(\frac{5 - \frac{1}{x}}{4}\right)$',
	r'$s(t) = \mathcal{A}\sin(2 \omega t)$',
	r'a_d:=6+\frac{7}{(4+5)}\cdot6=6'
	]
latexmath2png.math2png(eqs, os.getcwd(), prefix = pre)
 
def window_destroy(widget):
	for i in range(0, len(eqs)):
		os.unlink(os.path.join(os.getcwd(), '%s%d.png' % (pre, i + 1)))
	gtk.main_quit()
 
window = gtk.Window()
window.set_border_width(10)
window.set_title('LaTeX Equations in GTK')
window.connect('destroy', window_destroy)
vbox = gtk.VBox(spacing = 10)
window.add(vbox)
 
images = [None] * len(eqs)
for i in range(len(eqs)):
	images[i] = gtk.image_new_from_file('%s%d.png' % (pre, i + 1))
	vbox.pack_start(images[i])
 
window.show_all()
gtk.main()