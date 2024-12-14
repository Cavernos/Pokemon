from lib.events import EventListener, Event


class CutSceneManager:
    def __init__(self):
        self.cut_scenes_complete = []
        self.cut_scene = None
        self.cut_scene_running = False
        EventListener.add_event_listener(Event.CUT_SCENE_START, self.start)

    def start(self, event):
        if event.cut_scene.name not in self.cut_scenes_complete:
            self.cut_scene = event.cut_scene
            if not event.replayable:
                self.cut_scenes_complete.append(self.cut_scene.name)
            self.cut_scene_running = True

    def end(self):
        self.cut_scene = None
        self.cut_scene_running = False

    def update(self):
        if self.cut_scene_running:
            self.cut_scene_running = self.cut_scene.update()
        else:
            self.end()

    def render(self):
        if self.cut_scene_running:
            self.cut_scene.render()

