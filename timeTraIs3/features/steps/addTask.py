from ...timeTra.models import *


'''
@given('the following values for a task')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the following values for a task')
'''

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



@then('the task is saved')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the task is saved')
