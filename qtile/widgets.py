from libqtile import bar, widget
from libqtile.config import Screen

from functions import PWA

# widget_defaults = dict(
#     font="sans",
#     fontsize=12,
#     padding=3,
# )
# extension_defaults = widget_defaults.copy()

class Widgets:
    def __init__(self):
        self.colors = [["#292d3e", "#292d3e"],   #0
                       ["#ffffff", "#ffffff"],   #1
                       ["#8d62a9", "#8d62a9"],   #2
                       ["#e1acff", "#e1acff"],   #3
                       ["#000000", "#000000"],   #4
                       ["#8b5681", "#8b5681"],   #5
                       ["#20b2aa", "#20b2aa"],   #6
                       ["#F39C12", "#F39C12"],   #7
                       ["#F7DC6F", "#F7DC6F"],   #8
                       ["#6495ed", "#6495ed"],   #9
                       ["#4c566a", "#4c566a"], ] #10

        self.font = "Noto"
        self.font_bold = "Noto Bold"

    def init_widgets_list(self):
        '''
        Function that returns the desired widgets in form of list
        '''
        widgets_list = [
            widget.Sep(
                linewidth=0,
                padding=6,
                foreground=self.colors[1],
                background=self.colors[0]
            ),
            widget.CurrentLayoutIcon(
                font=self.font,
                foreground=self.colors[0],
                background=self.colors[6],
                padding=0,
                scale=0.7
            ),
            widget.CurrentLayout(
                font=self.font,
                foreground=self.colors[0],
                background=self.colors[6],
                padding=5
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=self.colors[1],
                background=self.colors[0]
            ),
            widget.GroupBox(
                font=self.font_bold,
                margin_y=2,
                margin_x=0,
                padding_y=5,
                padding_x=3,
                borderwidth=3,
                active=self.colors[7],
                inactive=self.colors[10],
                this_current_screen_border=self.colors[5],
                foreground=self.colors[1],
                background=self.colors[0],
                disable_drag=True,
                rounded=True,
            ),
            widget.Sep(
                linewidth=0,
                padding=40,
                foreground=self.colors[1],
                background=self.colors[0]
            ),
            widget.WindowName(
                font=self.font,
                foreground=self.colors[3],
                background=self.colors[0],
                padding=0
            ),
            widget.Systray(
                background=self.colors[0],
                padding=5
            ),
            widget.KeyboardLayout(
                font=self.font,
                foreground=self.colors[4],
                background=self.colors[8],
                padding=5,
                configured_keyboards=['us', 'ru']
            ),
            # widget.Sep(
            #     linewidth=0,
            #     padding=10,
            #     foreground=self.colors[],
            #     background=self.colors[]
            # ),
            # widget.BatteryIcon(
            #     foreground=self.colors[],
            #     background=self.colors[],
            #     padding=5,
            # ),
            # widget.Battery(
            #     foreground=self.colors[],
            #     background=self.colors[],
            #     padding=5,
            # ),
            # widget.Sep(
            #     linewidth=0,
            #     padding=10,
            #     foreground=self.colors[],
            #     background=self.colors[]
            # ),
            # widget.Bluetooth(
            #     foreground=self.colors[],
            #     background=self.colors[],
            #     padding=5,
            # ),
            # widget.Sep(
            #     linewidth=0,
            #     padding=10,
            #     foreground=self.colors[],
            #     background=self.colors[]
            # ),
            widget.TextBox(
                text="  ",
                foreground=self.colors[4],
                background=self.colors[7],
                padding=0,
                mouse_callbacks={
                    "Button1": lambda qtile: qtile.cmd_spawn("pavucontrol")}
            ),
            widget.Volume(
                font=self.font,
                foreground=self.colors[4],
                background=self.colors[7],
                step=5,
                padding=5
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=self.colors[0],
                background=self.colors[5]
            ),
            widget.Clock(
                font=self.font,
                foreground=self.colors[4],
                background=self.colors[5],
                format="%B %d  [ %H:%M ]"
            ),
            widget.Sep(
                linewidth=0,
                padding=10,
                foreground=self.colors[0],
                background=self.colors[5]
            ),
        ]
        return widgets_list

    def init_screen(self):
        return [Screen(
                    top=bar.Bar(widgets=self.init_widgets_list(),
                    opacity=1.0,
                    size=24)), ]