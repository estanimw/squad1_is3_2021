from timeTra.models import *

@given(u'a user')
def step_impl(context):
    pass


@when(u'he wants to visualize his tasks')
def step_impl(context):
    context.tasks = []
    for row in context.table:
        task = Task(name=row['name'],
                    description=row['description'],
                    starting_date=row['starting_date'],
                    estimated_time=row['estimated_time'],
                    time_spent=row['time_spent'],
                    state=row['state'])
        task.save()
        context.tasks.append(task)


@then(u'all his tasks are shown')
def step_impl(context):
    taskSet =Task.tasks.filter()
    for task in taskSet:
        print(type(taskSet))
        assert task in context.tasks
    assert len(taskSet) == len(context.tasks)