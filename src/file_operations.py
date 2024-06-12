import os

# Imported properties
from properties import Paths

def remove_event(events: dict, key: int) -> None:
    """Function removing line from database with all user events.

    Args:
        events (dict): dictionary of all events.
        key (int): key of the event in dictionary
    """
    file_name: str = f'{os.path.join(os.path.dirname(__file__), '..') + Paths.EVENTS}'
    new_content: str = ''
    with open(file_name, 'r') as file:
        for event in events:
            if event != key:
                new_content += f'{events[event]}\n'
            else:
                print('skipping line')
    with open(file_name, 'w') as file:
        file.write(new_content)

def edit_event(events: dict, key: int, event_edit: str) -> None:
    """Function editing database with all user events.

    Args:
        events (dict): dictionary of all events
        key (int): key of the event in dictionary
        event_edit (str): string with which info will be replaced
    """
    event_edit = event_edit.replace('\n', ' /n|').replace('\r', ' /r|')
    file_name: str = f'{os.path.join(os.path.dirname(__file__), '..') + Paths.EVENTS}'
    new_content: str = ''
    with open(file_name, 'r') as file:
        for event in events:
            if event != key:
                new_content += f'{events[event]}\n'
            else:
                new_content += f'{event_edit}\n'
    with open(file_name, 'w') as file:
        file.write(new_content)

def add_event(events: dict, new_event: str) -> None:
    file_name: str = f'{os.path.join(os.path.dirname(__file__), '..') + Paths.EVENTS}'
    with open(file_name, 'a') as file:
        file.write(f'{new_event}\n')
