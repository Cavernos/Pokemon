from collections import defaultdict
from operator import attrgetter

from pygame.event import Event


class EventListener:
    listeners = defaultdict(list)

    @staticmethod
    def on(event_type: int):
        def inner(func):
            EventListener.add_event_listener(event_type, func)

        return inner

    @staticmethod
    def add_event_listener(event_type: int, func):
        EventListener.listeners[event_type].append(func)

    @staticmethod
    def remove_event_listener(event_type: int, handler=None):
        if event_type in EventListener.listeners and handler is None:
            del EventListener.listeners[event_type]
            return
        if handler in EventListener.listeners[event_type]:
            del EventListener.listeners[event_type]

    @staticmethod
    def handle(event: Event):
        for handler in EventListener.listeners[attrgetter('type')(event)]:
            handler(event)
