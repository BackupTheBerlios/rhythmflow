import rb
import rhythmdb
from os import path, listdir
from urllib import url2pathname
import mimetypes
import test_embed
import time
import gobject

IMAGE_NAMES = ['cover', 'album', 'albumart', '.folder', 'folder']

class Rhythmflow(rb.Plugin):
    def __init__ (self):
        rb.Plugin.__init__ (self)
        
    def activate (self, shell):
        self.source = shell.get_property("selected_source")
        self.source.connect("status-changed", self.print_msg)
        self.tmp = 0
            
    def print_msg(self, s):
        self.tmp = self.tmp + 1  
        gobject.timeout_add_seconds(1,self.first_time_load_songs,self.tmp)


    def first_time_load_songs(self,tmp):
        if self.tmp == tmp:
            print "========== Mise a jour de Cover =========="
        return False
  
    def get_cover(self, db_entry=None):
        if db_entry:
            cover_dir = path.dirname(url2pathname(db_entry.get_playback_uri()).replace('file://', ''))
            if path.isdir(cover_dir):
                for f in listdir(cover_dir):
                    file_name = path.join(cover_dir, f)
                    mt = mimetypes.guess_type(file_name)[0]
                    if mt and mt.startswith('image/'):
                        if path.splitext(f)[0].lower() in IMAGE_NAMES:
                            return file_name

            # Find cover saved by artdisplay plugin
            song_info = self.get_song_info(db_entry)
            for rb_cover_path in ('~/.gnome2/rhythmbox/covers', '~/.cache/rhythmbox/covers/'):
                for file_type in ('jpg', 'png', 'jpeg', 'gif', 'svg'):
                    cover_file = path.join(path.expanduser(rb_cover_path),
                                           '%s - %s.%s' %
                                           (song_info['artist'],
                                            song_info['album'],
                                            file_type))
                    if path.isfile(cover_file):
                        return cover_file

            # No cover found
            return None
        # Not playing
        return None
    
    def get_song_info(self, db_entry=None):
        song_info = {}
        db = self.shell.get_property("db")
        if db_entry:
            song_info['title'] = db.entry_get(db_entry, rhythmdb.PROP_TITLE)
            song_info['artist'] = db.entry_get(db_entry, rhythmdb.PROP_ARTIST)
            song_info['album'] = db.entry_get(db_entry, rhythmdb.PROP_ALBUM)
        return song_info