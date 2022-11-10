from libqtile.config import Click, Drag, Key
from libqtile.lazy import lazy

# Import the function that move the window to the next and prev group
from functions import Functions

from keybindings_const import *


class KeyBindings:

    keys = []

    def init_keys(self):
        self.__init_move_keys()
        self.__init_windows_keys()
        self.__init_shutdown_keys()
        self.__init_kill_keys()
        self.__init_spawn_keys()

        return self.keys


    def __init_move_keys(self):
        focus = [Key([MOD], LEFT, lazy.layout.left()),
                 Key([MOD], RIGHT, lazy.layout.right()),
                 Key([MOD], DOWN, lazy.layout.down()),
                 Key([MOD], UP, lazy.layout.up())]

        window = [Key([MOD, SHIFT], LEFT, lazy.layout.shuffle_left()),
                  Key([MOD, SHIFT], RIGHT, lazy.layout.shuffle_right()),
                  Key([MOD, SHIFT], DOWN, lazy.layout.shuffle_down()),
                  Key([MOD, SHIFT], UP, lazy.layout.shuffle_up())]

        grow = [Key([MOD, CONTROL], LEFT, lazy.layout.grow_left()),
                Key([MOD, CONTROL], RIGHT, lazy.layout.grow_right()),
                Key([MOD, CONTROL], DOWN, lazy.layout.grow_down()),
                Key([MOD, CONTROL], UP, lazy.layout.grow_up())]

        self.keys += focus
        self.keys += window
        self.keys += grow

    def __init_windows_keys(self):
        grow      = Key([MOD], GROW, lazy.layout.grow())
        shrink    = Key([MOD], SHRINK, lazy.layout.shrink())
        normalize = Key([MOD], NORMALIZE, lazy.layout.normalize())
        maximize  = Key([MOD], MAXIMIZE, lazy.layout.maximize())
        
        self.keys += [grow, shrink, normalize, maximize] 

    def __init_shutdown_keys(self):
        self.keys += [Key([MOD, CONTROL], SHUTDOWN, lazy.shutdown()),
                      Key([MOD, CONTROL], RESTART, lazy.reload_config())]
    
    def __init_kill_keys(self):
        self.keys += [Key([MOD], KILL_ALL_MINUS_CURRENT, Functions.kill_all_windows_minus_current()),
                      Key([MOD], KILL_ALL, Functions.kill_all_windows()),
                      Key([MOD], KILL_CURRENT, lazy.window.kill(), desc="Kill focused window")]

    def __init_spawn_keys(self):
        for spawn_key in SPAWN_KEYS:
            modifier, key, command = spawn_key
            keybinding = Key(modifier, key, lazy.spawn(command))
            self.keys.append(keybinding)

class Mouse:
    def init_mouse(self):
        return [Drag([MOD], M_BUTTON1, lazy.window.set_position_floating(), start=lazy.window.get_position()),
                Drag([MOD], M_BUTTON3, lazy.window.set_size_floating(), start=lazy.window.get_size()),
                Click([MOD], M_BUTTON2, lazy.window.bring_to_front())]