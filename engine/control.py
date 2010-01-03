'''

@author: Helios GILLES
'''

import clutter
import rhythmflow 

DEPTH_CONTROL = 1

PATH = "./img/control/"

class control:
    def __init__(self,parent):
        self.parent = parent
        self.controls = clutter.Group()
        self.play_pause = self.play_pause(self.parent)
        self.stop = self.stop(self.parent)
        self.rewind = self.rewind(self.parent)
        self.forward = self.forward(self.parent)
        self.timeline = clutter.Timeline(30)
        self.timeline.set_duration(200)
        self.alpha = clutter.Alpha(self.timeline,clutter.LINEAR)      
        self.behaviours = []
        
    def play_pause(self,parent):
        play_pause = clutter.Texture()
        play_pause.set_from_file(PATH+"control_play.png")
        play_pause.set_anchor_point(play_pause.get_width()/2,play_pause.get_height()/2)
        play_pause.set_position(play_pause.get_width(),play_pause.get_height())
        play_pause.set_depth(DEPTH_CONTROL)
        self.controls.add(play_pause)
        return play_pause
    
    def stop(self,parent):
        stop = clutter.Texture()
        stop.set_from_file(PATH+"control_stop.png")
        stop.set_anchor_point(stop.get_width()/2,stop.get_height()/2)
        stop.set_position(self.play_pause.get_x()+self.play_pause.get_width()+stop.get_width()/2,self.play_pause.get_y())
        stop.set_depth(DEPTH_CONTROL)
        self.controls.add(stop)
        return stop
    
    def rewind(self,parent):
        rewind = clutter.Texture()
        rewind.set_from_file(PATH+"control_rewind.png")
        rewind.set_anchor_point(rewind.get_width()/2,rewind.get_height()/2)
        rewind.set_position(self.stop.get_x()+self.stop.get_width()+rewind.get_width()/1.5,self.play_pause.get_y())
        rewind.set_depth(DEPTH_CONTROL)
        self.controls.add(rewind)
        return rewind
    
    def forward(self,parent):
        forward = clutter.Texture()
        forward.set_from_file(PATH+"control_forward.png")
        forward.set_anchor_point(forward.get_width()/2,forward.get_height()/2)
        forward.set_position(self.rewind.get_x()+self.rewind.get_width()+forward.get_width()/2,self.play_pause.get_y())
        forward.set_depth(DEPTH_CONTROL)
        self.controls.add(forward)
        return forward
    
if __name__=="__main__":
    rhythmflow.rhythmflow()