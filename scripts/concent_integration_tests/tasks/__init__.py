import copy

_TASK_SETTINGS = {
    'default': {
        'type': "Blender",
        'name': 'test task',
        'timeout': "0:10:00",
        "subtask_timeout": "0:09:50",
        "subtasks": 1,
        "bid": 1.0,
        "resources": [],
        "options": {
            "output_path": '',
            "format": "PNG",
            "resolution": [
                320,
                240
            ]
        }
    },
    '2_short': {
        'type': "Blender",
        'name': 'test task',
        'timeout': "0:04:00",
        "subtask_timeout": "0:01:30",
        "subtasks": 2,
        "bid": 1.0,
        "resources": [],
        "options": {
            "output_path": '',
            "format": "PNG",
            "resolution": [
                320,
                240
            ]
        }
    }
}


def get_settings(key: str):
    return copy.deepcopy(_TASK_SETTINGS[key])
