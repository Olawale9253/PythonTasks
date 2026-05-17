



task_list = []

id_count = 1

def count_task();

 return len(task_list)

def create_task(title, content):

    new_list = [id_count, title, content, id_count]

    task_list.append(new_list)

    id_count += 1

    return 0
