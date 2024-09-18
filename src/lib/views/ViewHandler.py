class ViewHandler:
    def __init__(self):
        self.curent_view = None

    def set_view(self, view):
        self.curent_view = view()

    def update(self):
        self.curent_view.update()

    def get_view(self):
        return self.curent_view
