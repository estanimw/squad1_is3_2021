from timeTra.models import *


@when('the user adds the task with all the values')
def step_impl(context):
    task = Task(name=context.samples[0]['name'],
                       description=context.samples[0]['description'],
                       starting_date=context.samples[0]['starting_date'],
                       estimated_time=context.samples[0]['estimated_time'],
                       state=context.samples[0]['state'])
    context.task = task
    task.save()
#kcy

@then('the task is saved')
def step_impl(context):
    taskSet = Task.tasks.filter(id=context.task.id)
    taskSaved = taskSet.first()
    taskModel = context.samples[0]
    print(taskSaved.state)
    assert taskSaved.name == taskModel['name']
    assert taskSaved.description == taskModel['description']
    assert taskSaved.starting_date == int(taskModel['starting_date'])
    assert taskSaved.estimated_time == int(taskModel['estimated_time'])
    assert taskSaved.state == taskModel['state']
    assert taskSaved is not None
    taskSet.delete()




@when(u'the user adds the task with a too long description')
def step_impl(context):
    context.exception = ""
    task = Task(name=context.samples[0]['name'],
        description=context.samples[0]['description'],
        starting_date=context.samples[0]['starting_date'],
        estimated_time=context.samples[0]['estimated_time'])
    context.task = task
    print(task.description)



@given(u'a user wants to add the following task')
def step_impl(context):
    context.samples = context.table


@when(u'the user adds the task without all the required values')
def step_impl(context):
    context.exception = ""
    task = Task(name=context.samples[0]['name'],
        description=context.samples[0]['description'],
        starting_date=context.samples[0]['starting_date'])
    context.task = task





@then(u'the following warning is shown')
def step_impl(context):
    try:
        context.task.save()
    except Exception as e:
        context.exception = str(e)
    assert context.exception == context.table[0]['warning']