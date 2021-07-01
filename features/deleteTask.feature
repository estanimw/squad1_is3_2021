Feature: Modify task attributes
  As a user I want to be able to eliminate a task so that I can remove it from the task's list

  Scenario: Delete a task
    Given A user with the following tasks
      | name | description | starting_date | estimated_time  | state |
      | Task 1 | Some other description for task 1 | 1624590000000 | 20 | Completed |
      | Task 2 | Some description for task 2 | 12390000000 | 12 | In Progress |
    When that user deletes one
      | id |
      | 2 |
    Then that task is deleted

  Scenario: Delete a task that does not exist
    Given A user with the following tasks
      | name | description | starting_date | estimated_time | state |
      | Task 1 | Some other description for task 1 |1624590000000|20 | Completed |
    When that user deletes one
      | id |
      | 2 |
    Then the following warning is shown
      | warning |
      | La tarea a eliminar no existe.|