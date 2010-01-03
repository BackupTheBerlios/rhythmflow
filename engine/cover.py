'''

@author: Helios GILLES
'''

import clutter
import os

WIDTH_COVER = 250
HEIGHT_COVER = 250
PATH = "../covers/"

class cover(clutter.Group):
    def __init__(self,parent):
        self.parent = parent
        self.list_covers = self.list_covers()
        self.covers = self.init_covers()
        
    def list_covers(self):
        list = os.listdir(PATH)
        return list
    
    def init_covers(self):
        ret = []
        for cover in self.list_covers:
            ret.append(self.init_cover(PATH+cover))
        return ret
            
    def init_cover(self,file):
        cover = clutter.Texture()
        cover.set_from_file(file)
        cover.set_size(WIDTH_COVER,HEIGHT_COVER)
        cover.set_anchor_point(cover.get_width()/2, cover.get_height()/2)
        return cover