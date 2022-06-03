import gi
  
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
  
   
class LabelWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title ="Label Example")
          
        # Create Box
        hbox = Gtk.Box(spacing = 10)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, 
                    spacing = 10)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, 
                    spacing = 10)
        vbox_right.set_homogeneous(False)
   
        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)
          
        # Create label
        label = Gtk.Label("Normal label")
        vbox_left.pack_start(label, True, True, 0)
          
        # Create justified label
        # with multiple lines
        label = Gtk.Label("Example for "
                "Right-justified label.\n"
                "having multiple lines.")
        label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.pack_start(label, True, True, 0)
   
        label = Gtk.Label(
            "Example for a line-wrapped label."
   
        )
        label.set_line_wrap(True)
        vbox_right.pack_start(label, True, True, 0)
   
        label = Gtk.Label(
            "Example for a line-wrapped filled label. "
        )
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        vbox_right.pack_start(label, True, True, 0)
          
        # Create label markup
        label = Gtk.Label()
        label.set_markup(
            "To go to <b>Geeks</b> "
            "<small>For</small> <i>Geeks</i> "
            '<a href ="https://www.geeksforgeeks.org/" '
            'title ="">Click here</a>.'
        )
        label.set_line_wrap(True)
        vbox_left.pack_start(label, True, True, 0)
          
        # Create label mnemonic
        label = Gtk.Label.new_with_mnemonic(
            "_Press -> to click the right button to exit"
        )
        vbox_left.pack_start(label, True, True, 0)
        label.set_selectable(True)
          
        # Create Button
        button = Gtk.Button(label ="Exit")
        label.set_mnemonic_widget(button)
        vbox_right.pack_start(button, True, True, 0)
   
        self.add(hbox)
   
   
window = LabelWindow()
window.connect("destroy", Gtk.main_quit)
  
# Display the window.
window.show_all()
  
# Start the GTK + processing loop
Gtk.main()