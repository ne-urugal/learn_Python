#write-task

import json
from datetime import datetime
from uuid import uuid4


task_list = {}
def write_task_to_file(name, desc, days, priority):
    global task_list
    try:
        file_name = uuid4()
        task_list[file_name] = [{'Task name: ': name}, {'Task desc: ', desc}]
        task_dict = {
            'name': name,
            'desk': desc,
            'repeat_on': days,
            'priority': priority,
            'created_at': datetime.now().isoformat()
        }
        with open(f'tasks/{file_name}.json', 'w', encoding='utf-8') as file:
            json.dumps(task_dict, indent=4)
            json.dump(task_dict, file)
    except FileNotFoundError:
        print('Ooops!')

    return name, desc, days, priority