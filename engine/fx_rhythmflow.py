'''

@author: Helios GILLES
'''

import clutter
import rhythmflow 
import math

Y_CENTRE = 0.35
SCALE_CENTER = 1.3
X_BIG_SPACE = 0
X_SPACE = 0.6
Y_SPACE = 0.05
OPACITY_OTHER = 80

class fx:
    def __init__(self,parent):
        self.parent = parent
        self.timeline = clutter.Timeline(30)
        self.timeline.set_duration(200)
        self.alpha = clutter.Alpha(self.timeline,clutter.EASE_IN_SINE)   
        self.view = clutter.Group()   
        self.behaviours = []
        self.anim_finished = True
        self.timeline.connect("started", self.event_anim_started)
        self.timeline.connect("completed", self.event_anim_completed)
        
    def event_anim_started(self,event):
        self.anim_finished = False
    
    def event_anim_completed(self,event):
        self.anim_finished = True
                
    def get_view(self):
        return self.view
    
    def init_fx(self,parent,covers,index_cover_selected):
        for (index, cover) in enumerate(covers):
            self.view.add(cover)
            cover.set_reactive(True)
            cover.connect("button-press-event", parent.click_cover)
            if index == index_cover_selected:
                cover.set_scale(SCALE_CENTER,SCALE_CENTER)
                cover.set_position(parent.get_width()/2,parent.get_height()*Y_CENTRE)
                cover.set_depth(0)
            elif index < index_cover_selected:
                if (index_cover_selected - index) % 2 == 1:
                    cover.set_position(parent.get_width()/2-cover.get_width()*X_BIG_SPACE+cover.get_width()*(index-index_cover_selected)*X_SPACE,parent.get_height()/2+parent.get_height()*Y_SPACE)
                else:
                    cover.set_position(parent.get_width()/2-cover.get_width()*X_BIG_SPACE+cover.get_width()*(index-index_cover_selected)*X_SPACE,parent.get_height()/2-parent.get_height()*Y_SPACE)
                cover.set_opacity(OPACITY_OTHER)
                cover.set_depth(index-index_cover_selected)
            else:
                if (index - index_cover_selected) % 2 == 1:
                    cover.set_position(parent.get_width()/2+cover.get_width()*X_BIG_SPACE+cover.get_width()*(index-index_cover_selected)*X_SPACE,parent.get_height()/2+parent.get_height()*Y_SPACE)
                else:
                    cover.set_position(parent.get_width()/2+cover.get_width()*X_BIG_SPACE+cover.get_width()*(index-index_cover_selected)*X_SPACE,parent.get_height()/2-parent.get_height()*Y_SPACE)                
                cover.set_opacity(OPACITY_OTHER)
                cover.set_depth(index_cover_selected-index)
        
    def anim_left(self,parent,covers,index_cover_selected):
        print "left"
        if self.anim_finished :
            if (parent.get_index_cover_selected() > 0):
                self.behaviours = []
                for (index, cover) in enumerate(covers):
                    if index < index_cover_selected - 1:
                        if (index_cover_selected - index) % 2 == 1:
                            path = clutter.Path("M "+str(cover.get_x())+" "+str(cover.get_y())+" L "+str(cover.get_x()+cover.get_width()*X_SPACE)+" "+str(cover.get_y()-2*parent.get_height()*Y_SPACE))
                        else:
                            path = clutter.Path("M "+str(cover.get_x())+" "+str(cover.get_y())+" L "+str(cover.get_x()+cover.get_width()*X_SPACE)+" "+str(cover.get_y()+2*parent.get_height()*Y_SPACE))
                        cover.set_depth(index-index_cover_selected)
                        behavior = clutter.BehaviourPath(self.alpha,path)
                        behavior.apply(cover)
                        self.behaviours.append(behavior)
                        
                covers[index_cover_selected-1].set_depth(0)      
                (cur_scale_x,cur_scale_y) = covers[index_cover_selected-1].get_scale()
                behavior = clutter.BehaviourScale(cur_scale_x,cur_scale_y,SCALE_CENTER,SCALE_CENTER,self.alpha)
                behavior.apply(covers[index_cover_selected-1])
                self.behaviours.append(behavior)
                path = clutter.Path("M "+str(covers[index_cover_selected-1].get_x())+" "+str(covers[index_cover_selected-1].get_y())+" L "+str(parent.get_width()/2)+" "+str(parent.get_height()*Y_CENTRE))
                behavior = clutter.BehaviourPath(self.alpha,path)
                behavior.apply(covers[index_cover_selected-1])
                self.behaviours.append(behavior)
                behavior = clutter.BehaviourOpacity(OPACITY_OTHER,255,self.alpha)
                behavior.apply(covers[index_cover_selected-1])
                self.behaviours.append(behavior)
                
                covers[index_cover_selected].set_depth(-1)
                (cur_scale_x,cur_scale_y) = covers[index_cover_selected].get_scale()
                behavior = clutter.BehaviourScale(cur_scale_x,cur_scale_y,1,1,self.alpha)
                behavior.apply(covers[index_cover_selected])
                self.behaviours.append(behavior)
                path = clutter.Path("M "+str(covers[index_cover_selected].get_x())+" "+str(covers[index_cover_selected].get_y())+" L "+str(parent.get_width()/2+cover.get_width()*X_BIG_SPACE+cover.get_width()*X_SPACE)+" "+str(parent.get_height()/2+parent.get_height()*Y_SPACE))
                behavior = clutter.BehaviourPath(self.alpha,path)
                behavior.apply(covers[index_cover_selected])
                self.behaviours.append(behavior)
                behavior = clutter.BehaviourOpacity(255,OPACITY_OTHER,self.alpha)
                behavior.apply(covers[index_cover_selected])
                self.behaviours.append(behavior)
                
                for (index, cover) in enumerate(covers):
                    if index > index_cover_selected:
                        if (index_cover_selected - index) % 2 == 1:
                            path = clutter.Path("M "+str(cover.get_x())+" "+str(cover.get_y())+" L "+str(cover.get_x()+cover.get_width()*X_SPACE)+" "+str(cover.get_y()-2*parent.get_height()*Y_SPACE))
                        else:
                            path = clutter.Path("M "+str(cover.get_x())+" "+str(cover.get_y())+" L "+str(cover.get_x()+cover.get_width()*X_SPACE)+" "+str(cover.get_y()+2*parent.get_height()*Y_SPACE))
                        cover.set_depth(index_cover_selected-index-2)
                        behavior = clutter.BehaviourPath(self.alpha,path)
                        behavior.apply(cover)
                        self.behaviours.append(behavior)
                      
                self.timeline.start() 
                parent.dec_index_cover_selected()

            
    def anim_right(self,parent,covers,index_cover_selected):
        print "rigth"
        if self.anim_finished :
            if (parent.get_index_cover_selected() < len(covers)-1):
                self.behaviours = []
                for (index, cover) in enumerate(covers):
                    if index < index_cover_selected :
                        if (index_cover_selected - index) % 2 == 1:
                            path = clutter.Path("M "+str(cover.get_x())+" "+str(cover.get_y())+" L "+str(cover.get_x()-cover.get_width()*X_SPACE)+" "+str(cover.get_y()-2*parent.get_height()*Y_SPACE))
                        else:
                            path = clutter.Path("M "+str(cover.get_x())+" "+str(cover.get_y())+" L "+str(cover.get_x()-cover.get_width()*X_SPACE)+" "+str(cover.get_y()+2*parent.get_height()*Y_SPACE))
                        cover.set_depth(index-index_cover_selected)
                        behavior = clutter.BehaviourPath(self.alpha,path)
                        behavior.apply(cover)
                        self.behaviours.append(behavior)
                        
                                
                covers[index_cover_selected].set_depth(-1)
                (cur_scale_x,cur_scale_y) = covers[index_cover_selected].get_scale()
                behavior = clutter.BehaviourScale(cur_scale_x,cur_scale_y,1,1,self.alpha)
                behavior.apply(covers[index_cover_selected])
                self.behaviours.append(behavior)
                path = clutter.Path("M "+str(covers[index_cover_selected].get_x())+" "+str(covers[index_cover_selected].get_y())+" L "+str(parent.get_width()/2-cover.get_width()*X_BIG_SPACE-cover.get_width()*X_SPACE)+" "+str(parent.get_height()/2+parent.get_height()*Y_SPACE))
                behavior = clutter.BehaviourPath(self.alpha,path)
                behavior.apply(covers[index_cover_selected])
                self.behaviours.append(behavior)
                behavior = clutter.BehaviourOpacity(255,OPACITY_OTHER,self.alpha)
                behavior.apply(covers[index_cover_selected])
                self.behaviours.append(behavior)
                        
                covers[index_cover_selected+1].set_depth(0)      
                (cur_scale_x,cur_scale_y) = covers[index_cover_selected+1].get_scale()
                behavior = clutter.BehaviourScale(cur_scale_x,cur_scale_y,SCALE_CENTER,SCALE_CENTER,self.alpha)
                behavior.apply(covers[index_cover_selected+1])
                self.behaviours.append(behavior)
                path = clutter.Path("M "+str(covers[index_cover_selected+1].get_x())+" "+str(covers[index_cover_selected+1].get_y())+" L "+str(parent.get_width()/2)+" "+str(parent.get_height()*Y_CENTRE))
                behavior = clutter.BehaviourPath(self.alpha,path)
                behavior.apply(covers[index_cover_selected+1])
                self.behaviours.append(behavior)
                behavior = clutter.BehaviourOpacity(OPACITY_OTHER,255,self.alpha)
                behavior.apply(covers[index_cover_selected+1])
                self.behaviours.append(behavior)
                
                for (index, cover) in enumerate(covers):
                    if index > index_cover_selected + 1:
                        if (index_cover_selected - index) % 2 == 1:
                            path = clutter.Path("M "+str(cover.get_x())+" "+str(cover.get_y())+" L "+str(cover.get_x()-cover.get_width()*X_SPACE)+" "+str(cover.get_y()-2*parent.get_height()*Y_SPACE))
                        else:
                            path = clutter.Path("M "+str(cover.get_x())+" "+str(cover.get_y())+" L "+str(cover.get_x()-cover.get_width()*X_SPACE)+" "+str(cover.get_y()+2*parent.get_height()*Y_SPACE))
                        cover.set_depth(index_cover_selected-index-2)
                        behavior = clutter.BehaviourPath(self.alpha,path)
                        behavior.apply(cover)
                        self.behaviours.append(behavior)
                        
                self.behaviours.append(behavior)        
                self.timeline.start() 
                parent.inc_index_cover_selected()

if __name__=="__main__":
    rhythmflow.rhythmflow()
        