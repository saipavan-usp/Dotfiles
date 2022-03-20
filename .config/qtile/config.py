from typing import List  # noqa: F401
from libqtile import hook, layout , qtile #, widget, bar, 
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
import os, subprocess
import logging
# from themes.catppuccin import colors

# logging.basicConfig(
#     filename="/home/saipavan/.local/share/qtile/qtile.log",  
#     filemode="a",
#     format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

mod = "mod4"
alt = "mod1"   
terminal = "kitty"
home = os.getenv("HOME")
wifi_interface = "wlp2s0"

# Hooks

@hook.subscribe.startup_once
def start_one():
    home = os.path.expanduser("~/.config/qtile/scripts/autostart_once.sh")
    subprocess.run([home])

@hook.subscribe.startup
def start_always():
    home = os.path.expanduser("~/.config/qtile/scripts/autostart_always.sh")
    subprocess.run([home])

@hook.subscribe.client_new
def dialogs(window):
    if(window.window.get_wm_type() == 'dialog'
        or window.window.get_wm_transient_for()):
        window.floating = True

# @hook.subscribe.layout_change
# def max_corners(layout, group):
#     if layout.info["name"] == "max":


# Key Bindings

keys = [
    # Essentials
    Key([mod, "shift"], "n", lazy.spawn("networkmanager-dmenu"), desc="Launch Network Manager"),
    Key([mod, "shift"], "w", lazy.spawn(f"sh {home}/Scripts/wallpaper"), desc="Launch Wallpaper Selector"),
    Key([mod, "shift"], "s", lazy.spawn(f"sh {home}/Scripts/sound-profiles"), desc="Fix Sound"),
    Key([mod, "shift"], "m", lazy.spawn(f"sh {home}/Scripts/monitors-list"), desc="Launch Monitor Selector"),
    Key([mod, "control"], "r", lazy.spawn(f"sh {home}/Scripts/redshift"), desc="Activate Redshift"),
    Key([mod, "shift"], "p", lazy.spawn(f"sh {home}/.config/polybar/launch.sh"), desc="Launch Polybar"),
    Key([alt], "space", lazy.spawn("rofi -show drun"), desc="Launch App Launcher"),

    # Shortcuts
    Key([mod], "F2", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "F3", lazy.spawn("thunar"), desc="Launch Thunar"),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),

    # Toggle between split and unsplit sides of stack.
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "End", lazy.shutdown(), desc="Shutdown Qtile"),
]

# Groups

group_names = [
    ("󰞷", {'layout': 'monadtall', 'matches': [Match(wm_class=[""])]}), #SYS
    ("󰖟", {'layout': 'monadtall', 'matches': [Match(wm_class=["firefox"])]}), #WEB
    ("󰝰", {'layout': 'bsp', 'matches': [Match(wm_class=["thunar"])]}), #FILE
    ("󰅴", {'layout': 'monadtall', 'matches': [Match(wm_class=["code", "gedit"])]}), #DEV
    ("󱔗", {'layout': 'stack', 'matches': [Match(wm_class=["okular", "libreoffice"])]}), #CHAT
    ("󰭹", {'layout': 'bsp', 'matches': [Match(wm_class=["telegram-desktop"])]}), #CHAT
    ("󰎆", {'layout': 'monadtall', 'matches': [Match(wm_class=["spotify"])]}), #MUS
    ("󰟞", {'layout': 'monadtall', 'matches': [Match(wm_class=["vlc"])]}), #MUS
            ]

groups = [Group(name, **kwargs) for name, kwargs in group_names]
 
for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

# Layouts

layout_theme = {
    "margin": 10,
    "border_width" : 0,
    }

layouts = [
    layout.Bsp(**layout_theme),
    layout.Zoomy(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=1,**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Matrix(**layout_theme),
    # layout.Columns(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
]

widget_defaults = dict(
    font="Material Design Icons",
    fontsize=16,
    padding=3,
)

extension_defaults = widget_defaults.copy()

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.toggle_floating())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
], **layout_theme)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"

# Bar

screens = [
    Screen(
        # top=bar.Bar(
        #     [
        #         widget.GroupBox(
        #             highlight_method="text",
        #             disable_drag = True,
        #             urgent_alert_method="text",
        #             urgent_text=colors["Red"],
        #             background = colors["Black_1"],
        #             active =colors["White"],
        #             inactive = colors["Gray_0"],
        #             foreground = colors["White"],
        #             rounded = True
        #         ),
        #         widget.CurrentLayoutIcon(
        #             scale=0.5,
        #             foreground = colors["White"],
        #             background = colors["Black_1"]
        #         ),

        #         widget.Spacer(length=bar.STRETCH),

        #         widget.Battery(
        #             charge_char = "+",
        #             discharge_char = "-",
        #             format = '{percent:2.0%}{char}',
        #             update_interval = 5,
        #             notify_below = 20,
        #         ),

        #         widget.TextBox(
        #             text="Vol:",
        #             foreground=colors["White"]
        #             ),
        #         widget.Volume(
        #             step=2
        #         ),
        #         widget.Sep(linewidth= 0, padding = 10, foreground = colors["White"], background = colors["Black_1"]),
        #         widget.Systray(background=colors["Black_1"]),
        #         widget.Sep(linewidth= 0, padding = 10, foreground = colors["White"], background = colors["Black_1"]),
        #         widget.Clock(
        #             format='%d %a %I:%M:%S',
        #             background=colors["Black_1"]
        #         ),
        #     ],
        #     30, 
        #     background=colors["Black_1"]
        # ),
    ),
]