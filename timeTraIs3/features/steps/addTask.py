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