import os

# Imported properties
from properties import Paths

def remove_event(events: dict, key: int) -> None:
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

def edit_event(events: dict, key: int, event_edit: str, edit_region: str) -> None:
    """Function editing database with all user events.

    Args:
        events (dict): dictionary of all events
        key (int): key of the event in dictionary
        event_edit (str): string with which info will be replaced
        edit_region (str): 
            - 0 : name
            - 1 : date
            - 2 : time
            - 3 : description
    """
    file_name: str = f'{os.path.join(os.path.dirname(__file__), '..') + Paths.EVENTS}'
    new_content: str = ''
    with open(file_name, 'r') as file:
        for event in events:
            if event != key:
                new_content += f'{events[event]}\n'
            else:
                event_to_edit = events[event].split(',')
                event_to_edit[edit_region] = event_edit
                new_content += f'{''.join(event_to_edit)}\n'
    with open(file_name, 'w') as file:
        file.write(new_content)
