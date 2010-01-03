'''

@author: Helios GILLES
'''
import cluttergtk
import clutter
import gtk
import os

BLACK_BG = clutter.Color(0,0,0,255)
GREEN_BG = clutter.Color(0,255,0,255)

class test(cluttergtk.Embed):
    def __init__(self):
        cluttergtk.Embed.__init__(self)
        self.connect('size-request', self.size_request)
        
    def rf(self):
        self.stage = self.get_stage()
        self.stage.set_color(BLACK_BG) 
        self.stage.connect('key-press-event', self.parseKeyPress)
        
        self.rect = clutter.Rectangle()
        self.rect.set_size(100,100)
        self.rect.set_color(GREEN_BG)
        self.rect.set_reactive(True)
        self.rect.connect("button-press-event", self.left)
        self.stage.add(self.rect)
        
    def parseKeyPress(self,actor,event):
        if event.keyval == clutter.keysyms.q:
            print "cdfgdfgdfgfgdfgdfgdfgdfg"
            
    def left(self,actor,event):
        print "gjhgjhg"
            
    def size_request (self, widget, requisition):
        requisition.width, requisition.height = -1, 250
        self.rect.set_position(500,50)
        