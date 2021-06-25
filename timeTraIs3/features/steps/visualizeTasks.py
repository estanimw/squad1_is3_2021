@given(u'a user')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a user')


@when(u'he wants to visualize his tasks')
def step_impl(context):
    raise NotImplementedError(u'STEP: When he wants to visualize his tasks')


@then(u'all his tasks are shown')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then all his tasks are shown')
