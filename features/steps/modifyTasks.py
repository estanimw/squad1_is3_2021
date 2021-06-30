from timeTra.models import *

@given(u'A user with the following task')
def step_impl(context):
    task = Task(name=context.table[0]['name'],
                description=context.table[0]['description'],
                starting_date=context.table[0]['starting_date'],
                estimated_time=context.table[0]['estimated_time'],
                time_spent=context.table[0]['time_spent'],
                state=context.table[0]['state'])
    context.originalTask = task
    task.save()


@when(u'that user modifies it to')
def step_impl(context):
    task = context.originalTask
    context.modifiedTask = Task(name=context.table[0]['name'],
                                description=context.table[0]['description'],
                                starting_date=context.table[0]['starting_date'],
                                estimated_time=context.table[0]['estimated_time'],
                                time_spent=context.table[0]['time_spent'],
                                state=context.table[0]['state']) #id = None
    context.task = task.modifyTask(name=context.table[0]['name'],
                    description=context.table[0]['description'],
                    starting_date=context.table[0]['starting_date'],
                    estimated_time=context.table[0]['estimated_time'],
                    time_spent=context.table[0]['time_spent'],
                    state=context.table[0]['state'])




@then(u'the task is modified')
def step_impl(context):
    context.task.save()
    taskSet = Task.tasks.filter(id=context.originalTask.id)
    taskSaved = taskSet.first()
    assert context.originalTask == context.modifiedTask
    assert context.originalTask == taskSaved

@when(u'that user wants to fininsh it')
def step_impl(context):
    context.exception = ""
    try:
        context.task = context.originalTask.modifyTask(state = "Completed")
        context.modifiedTask = context.task
    except Exception as e:
        context.exception = str(e)

@then(u'the following warning should be shown')
def step_impl(context):
    print(Task.getAllTasks())
    assert context.exception == context.table[0]['warning']
    