new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006'] 

completed_tasks.append(new_tasks.pop()) # перенёс task_005 из new_tasks в completed_tasks в одно действие

new_tasks.remove('task_007') # удалил task_007 из new_tasks

print(new_tasks[-1]) # вывел последнюю задачу из new_tasks на экран
