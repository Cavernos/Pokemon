from collections import defaultdict
from operator import attrgetter

from pygame.event import Event


class EventListener:
    listeners = defaultdict(list)

    @staticmethod
    def add_event_listener(event_type: int):
        def inner(func):
            EventListener.listeners[event_type].append(func)
        return inner

    @staticmethod
    def remove_event_listener(event_type: int, handler): 
        if handler in EventListener.listeners[event_type]:
            del EventListener.listeners[event_type]

    @staticmethod
    def handle(event: Event, selector=attrgetter('type')):
        for handler in EventListener.listeners[selector(event)]:
            handler(event)

