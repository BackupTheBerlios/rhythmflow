'''

@author: Helios GILLES
'''
import cluttergtk
import clutter
import gtk
import os
import cover
import fx_default
import scrollbar
import control

WIDTH = 1000
HEIGHT = 600
BLACK_BG = clutter.Color(0,0,0,255)

class rhythmflow(cluttergtk.Embed):
    def __init__(self):
        cluttergtk.Embed.__init__(self)
        
    def rf(self):
        self.stage = self.get_stage()
        self.stage.set_size(WIDTH,HEIGHT)
        self.stage.set_color(BLACK_BG) 
        self.stage.connect('key-press-event', self.parseKeyPress)
        self.index_cover_selected = 2
        self.cover = cover.cover(self)
        self.fx = fx_default.fx(self)
        self.fx.init_fx(self, self.get_covers(), self.get_index_cover_selected())
        self.scrollbar = scrollbar.scrollbar(self)
        self.scrollbar.init_scrollbar(self, self.get_index_cover_selected(), self.get_size_covers())
        self.control = control.control(self)
        self.show()
        
    def parseKeyPress(self,actor,event):
        if event.keyval == clutter.keysyms.Left:
            self.anim_left()
        if event.keyval == clutter.keysyms.Right:
            self.anim_right()
        if event.keyval == clutter.keysyms.q:
            exit(0)
            
    def click_scrollbar_left(self,actor,event):
        self.anim_left()
        
    def click_scrollbar_right(self,actor,event):
        self.anim_right()
        
    def click_cover(self,actor,event):
        self.anim_dbl_click(actor)
            
    def anim_left(self):
        self.fx.anim_left(self,self.get_covers(),self.get_index_cover_selected())
        self.scrollbar.anim_left(self,self.get_index_cover_selected(),self.get_size_covers())
        
    def anim_right(self):
        self.fx.anim_right(self,self.get_covers(),self.get_index_cover_selected())
        self.scrollbar.anim_right(self,self.get_index_cover_selected(),self.get_size_covers())    
            
    def anim_dbl_click(self,actor):
        self.fx.anim_dbl_click(actor)
    
    def show(self):
        self.stage.remove_all()
        self.stage.add(self.scrollbar.scrollbars)
        self.stage.add(self.control.controls)
        self.stage.add(self.fx.get_view())
        self.stage.show_all()
        
    def get_width(self):
        return self.stage.get_width()
    
    def get_height(self):
        return self.stage.get_height()
    
    def get_index_cover_selected(self):
        return self.index_cover_selected
    
    def inc_index_cover_selected(self):
        self.index_cover_selected = self.index_cover_selected + 1
    
    def dec_index_cover_selected(self):
        self.index_cover_selected = self.index_cover_selected - 1
        
    def get_size_covers(self):
        return len(self.cover.covers)
    
    def get_covers(self):
        return self.cover.covers
    
    def set_covers(self,covers):
        self.cover.covers = covers
    
    def get_list_covers(self):
        return self.cover.list_covers
    
    def set_list_covers(self,list_covers):
        self.cover.list_covers = list_covers
        
    def get_scrollbars(self):
        return self.scrollbar.scrollbars
    
    def set_scrollbars(self,scrollbars):
        self.scrollbar.scrollbars = scrollbars
    
    def get_controls(self):
        return self.control.controls
    
    def set_controls(self,controls):
        self.control.controls = controls
    
    def get_fx(self):
        return self.fx
    
if __name__=="__main__":
    window = gtk.Window()
    window.connect('destroy', gtk.main_quit)
    window.set_title('Rhythmflow 0.1')
    vbox = gtk.VBox(False, 1)
    window.add(vbox)
    rf = rhythmflow()
    vbox.pack_start(rf, True, True, 0)
    rf.set_size_request(1000, 600)
    rf.realize()
    rf.rf()
    window.set_position(gtk.WIN_POS_CENTER)
    window.show_all()

    gtk.main()