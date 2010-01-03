'''

@author: Helios GILLES
'''

import clutter
import rhythmflow 

DEPTH_SCROLLBAR = 1

PATH = "./img/scrollbar/"

class scrollbar:
    def __init__(self,parent):
        self.parent = parent
        self.decal_lr = 12
        self.scrollbars = clutter.Group()
        self.bg = self.bg(self.parent)
        self.left = self.left(self.parent)
        self.right = self.right(self.parent)
        self.button = self.button(self.parent)
        self.timeline = clutter.Timeline(30)
        self.timeline.set_duration(200)
        self.alpha = clutter.Alpha(self.timeline,clutter.EASE_IN_OUT_SINE)      
        self.behaviours = []
        
    def bg(self,parent):
        bg = clutter.Texture()
        bg.set_from_file(PATH+"scrollbar_bg.png")
        bg.set_width(parent.get_width()/1.8)
        bg.set_anchor_point(bg.get_width()/2,bg.get_height()/2)
        bg.set_position(parent.stage.get_width()/2,parent.stage.get_height()/1.2)
        bg.set_depth(DEPTH_SCROLLBAR)
        self.scrollbars.add(bg)
        return bg 
        
    def left(self,parent):
        left = clutter.Texture()
        left.set_from_file(PATH+"scrollbar_left.png")
        left.set_anchor_point(left.get_width()/2,left.get_height()/2)
        left.set_position(self.bg.get_x()-self.bg.get_width()/2-left.get_width()/2+self.decal_lr,self.bg.get_y())
        left.set_depth(DEPTH_SCROLLBAR)
        left.set_reactive(True)
        left.connect("button-press-event", parent.click_scrollbar_left)
        self.scrollbars.add(left)
        return left
    
    def right(self,parent):
        right = clutter.Texture()
        right.set_from_file(PATH+"scrollbar_right.png")
        right.set_anchor_point(right.get_width()/2,right.get_height()/2)
        right.set_position(self.bg.get_x()+self.bg.get_width()/2+right.get_width()/2-self.decal_lr,self.bg.get_y())
        right.set_depth(DEPTH_SCROLLBAR)
        right.set_reactive(True)
        right.connect("button-press-event", parent.click_scrollbar_right)
        self.scrollbars.add(right)
        return right
    
    def button(self,parent):
        button = clutter.Texture()
        button.set_from_file(PATH+"scrollbar_button.png")
        button.set_anchor_point(button.get_width()/2,button.get_height()/2)
        button.set_position(self.bg.get_x()-self.bg.get_width()/2+button.get_width()/2,self.bg.get_y())
        button.set_depth(DEPTH_SCROLLBAR)
        self.scrollbars.add(button)
        return button
    
    def init_scrollbar(self,parent,index_cover_selected,size_covers):
        if index_cover_selected == 0:
            self.button.set_position(self.bg.get_x()-self.bg.get_width()/2+self.button.get_width()/2,self.bg.get_y())
        elif index_cover_selected == size_covers - 1:
            self.button.set_position(self.bg.get_x()+self.bg.get_width()/2-self.button.get_width()/2,self.bg.get_y())
        else:
            self.button.set_position(self.bg.get_x()-self.bg.get_width()/2+self.button.get_width()/2+index_cover_selected*(self.bg.get_width()-self.button.get_width())/(size_covers-1),self.bg.get_y())
    
    def anim_left(self,parent,index_cover_selected,size_covers):
        self.behaviours = []
        if index_cover_selected == 0:
            path = clutter.Path("M "+str(self.button.get_x())+" "+str(self.button.get_y())+" L "+str(self.bg.get_x()-self.bg.get_width()/2+self.button.get_width()/2)+" "+str(self.bg.get_y()))
        elif index_cover_selected == size_covers - 1:
            path = clutter.Path("M "+str(self.button.get_x())+" "+str(self.button.get_y())+" L "+str(self.bg.get_x()+self.bg.get_width()/2-self.button.get_width()/2)+" "+str(self.bg.get_y()))
        else:
            path = clutter.Path("M "+str(self.button.get_x())+" "+str(self.button.get_y())+" L "+str(self.bg.get_x()-self.bg.get_width()/2+self.button.get_width()/2+index_cover_selected*(self.bg.get_width()-self.button.get_width())/(size_covers-1))+" "+str(self.bg.get_y()))
        behavior = clutter.BehaviourPath(self.alpha,path)
        behavior.apply(self.button)
        self.behaviours.append(behavior)  
        self.timeline.start()
        
    def anim_right(self,parent,index_cover_selected,size_covers):
        self.behaviours = []
        if index_cover_selected == 0:
            path = clutter.Path("M "+str(self.button.get_x())+" "+str(self.button.get_y())+" L "+str(self.bg.get_x()-self.bg.get_width()/2+self.button.get_width()/2)+" "+str(self.bg.get_y()))
        elif index_cover_selected == size_covers - 1:
            path = clutter.Path("M "+str(self.button.get_x())+" "+str(self.button.get_y())+" L "+str(self.bg.get_x()+self.bg.get_width()/2-self.button.get_width()/2)+" "+str(self.bg.get_y()))
        else:
            path = clutter.Path("M "+str(self.button.get_x())+" "+str(self.button.get_y())+" L "+str(self.bg.get_x()-self.bg.get_width()/2+self.button.get_width()/2+index_cover_selected*(self.bg.get_width()-self.button.get_width())/(size_covers-1))+" "+str(self.bg.get_y()))
        behavior = clutter.BehaviourPath(self.alpha,path)
        behavior.apply(self.button)
        self.behaviours.append(behavior)  
        self.timeline.start()         
        
if __name__=="__main__":
    rhythmflow.rhythmflow()