from timeTra.models import *

@given(u'A user with the following tasks')
def step_impl(context):
    task_list = []
    for row in context.table:
        task = Task(name=row['name'],
                description=row['description'],
                starting_date=row['starting_date'],
                estimated_time=row['estimated_time'],
                state=row['state'])
        task.save()
        task_list.append(task)
    context.task_list = task_list


@when(u'that user deletes one')
def step_impl(context):
    context.exception = ''
    try:
        Task.delete(context.table[0]['id'])
    except Exception as e:
        context.exception = str(e)


@then(u'that task is deleted')
def step_impl(context):
    assert len(Task.getAllTasks()) == len(context.task_list)-1