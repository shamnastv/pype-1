from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, window_title):
        Gtk.Window.__init__(self, title = window_title)


class HomeScreen(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

class AddContactScreen(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

class IncomingCallScreen(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)

class CallScreenBox(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.discButton = Gtk.Button(label = "Disconnect")
        self.discButton.connect("clicked",self.disconnectCall)
        self.add(self.discButton)

    def disconnectCall(self, widget):
        print "Call disconnect request"




def UX(window_title):
    window = MainWindow(window_title)
    window.connect("delete-event", Gtk.main_quit)
    #window.add(label)
    callScreen = CallScreenBox()
    
    window.add(callScreen)
    window.show_all()
    Gtk.main()
