from timeTra.models import *


@given('the following values for a task')
def step_impl(context):
    context.samples = context.table


@given('a user wants to add a task')
def step_impl(context):
    pass


@when('the user adds the task with all the values')
def step_impl(context):
    task = Task(name=context.samples[0]['name'],
                       description=context.samples[0]['description'],
                       starting_date=context.samples[0]['starting_date'],
                       estimated_time=context.samples[0]['estimated_time'])
    context.task = task
    task.save()


@then('the task is saved')
def step_impl(context):
    taskSet = Task.tasks.filter(id=context.task.id)
    assert taskSet.first() is not None
    taskSet.delete()




@given(u'the following warning')
def step_impl(context):
    context.warning = context.table[0]['warning']


@when(u'the user adds the task with a too long description')
def step_impl(context):
    context.exception = ""
    task = Task(name=context.samples[1]['name'],
        description=context.samples[1]['description'],
        starting_date=context.samples[1]['starting_date'],
        estimated_time=context.samples[1]['estimated_time'])
    context.task = task
    print(task.description)


@then(u'an invalid description warning is shown')
def step_impl(context):
    try:
        context.task.save()
    except Exception as e:
        context.exception = str(e)
    assert context.exception == context.warning




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
    sourceFile = open('/Users/estanimw/demo.txt', 'w')
    print(task.state, file = sourceFile)
    sourceFile.close()




@then(u'the following warning is shown')
def step_impl(context):
    try:
        context.task.save()
    except Exception as e:
        context.exception = str(e)
    assert context.exception == context.table[0]['warning']