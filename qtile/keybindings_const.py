from libqtile.confreader import ConfigError

from functions import PWA

from os.path import expanduser

HOME = expanduser("~")

# Define constants here
TERMINAL = "alacritty"

# Basic keys
MOD = "mod4"
ALT = "mod1"
ALTGR = "mod5"
SHIFT = "shift"
CONTROL = "control"
RETURN = "Return"
TAB = "Tab"
PRINT = "Print"
UP_A = "Up"
DOWN_A = "Down"
LEFT_A = "Left"
RIGHT_A = "Right"
M_BUTTON1 = "Button1"
M_BUTTON2 = "Button2"
M_BUTTON3 = "Button3"

# Move keys
LEFT   = "h"
RIGHT  = "l"
DOWN   = "j"
UP     = "k"

# Qtile shutdown/restart keys
RESTART           = "r"
SHUTDOWN          = "q"

# Qtile kill keys
KILL_CURRENT           = "w"
KILL_ALL               = "x"
KILL_ALL_MINUS_CURRENT = "c"





# Basic wm bindings

# All of these variables include the MOVEMENT_KEYS at the start

# The key which the WM will use to move the layouts
MOVEMENT_KEY   = MOD
KILL_KEY       = MOD

SWAP_KEY       = SHIFT
FLOATING_KEY   = SHIFT



# Floating layout
TOOGLE_FLOATING = "f"
TOOGLE_FULL     = "g"

# Groups key
# Move screen to next and previous group
NEXT     = "k"
PREVIOUS = "j"

# Kill Functions


# Rotates layouts

TOOGLE_LAYOUT = "Tab"

# Basic window manager movements





# Group movement keys:
GROUPS_KEY     = CONTROL
SWAP_GROUP_KEY = SHIFT

NEXT_GROUP = "period"
PREV_GROUP = "comma"


# ------------ Hardware Configs ------------
HARDWARE_KEYS = [
    # (Modifier, Key, Command)

    # Volume
    ([], "XF86AudioLowerVolume", "pactl set-sink-volume @DEFAULT_SINK@ -5%"),
    ([], "XF86AudioRaiseVolume", "pactl set-sink-volume @DEFAULT_SINK@ +5%"),
    ([], "XF86AudioMute", "pactl set-sink-mute @DEFAULT_SINK@ toggle"),
     
    # Brightness
    ([], "XF86MonBrightnessUp", "brightnessctl set +10%"),
    ([], "XF86MonBrightnessDown", "brightnessctl set 10%-"),
]


APPS = [
    ([MOD], RETURN, TERMINAL),
    
    ([MOD], "b", "firefox"),
    ([MOD], "c", "code"),
    ([MOD, ALT], "a", "pavucontrol"),

    # Media hotkeys
    ([MOD],      UP_A, "pulseaudio-ctl up 5"),
    ([MOD],      DOWN_A, "pulseaudio-ctl down 5"),
    
    # Screenshots
    ([],         PRINT, "flameshot gui --clipboard"),
    # Full screen screenshot
    ([ALT],      PRINT, "flameshot full --clipboar"),
    
]

##########################
# Your custom keys here  #
##########################

# CUSTOM_SPAWN_KEYS = [
#     # PWA keys
#     ([MOD, ALT], "s", PWA.spotify()),
#     ([MOD, ALT], "m", PWA.music()),
#     ([MOD, ALT], "t", PWA.calendar()),
#     ([MOD, ALT], "y", PWA.youtube()),
#     ([MOD, ALT], "l", PWA.notion()),
#     ([MOD, ALT], "h", PWA.habitica()),
# ]


SPAWN_KEYS = HARDWARE_KEYS + APPS