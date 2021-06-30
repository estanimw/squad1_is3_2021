Feature: Modify task attributes
  As an employee, I want to delete a task just because.

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