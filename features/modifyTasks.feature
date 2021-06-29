Feature: Modify task attributes
  As an employee, I want to modify a task so I can change it details.

  Scenario: Modify task with valid values
    Given A user with the following task
      | name | description | starting_date | estimated_time | time_spent | state |
      | Task 1 | Some description for task 1 |1624590000000|20| 10 | In Progress |
    When that user modifies it to
      | name | description | starting_date | estimated_time | time_spent | state |
      | Task 1 | Some other description for task 1 |1624590000000|20| 20 | Completed |
    Then the task is modified

  Scenario: Modify task with invalid values
    Given A user with the following task
      | name | description | starting_date | estimated_time | time_spent | state |
      | Task 1 | Some description for task 1 |1624590000000|20| 10 | In Progress |
    When that user modifies it to
      | name | description | starting_date | estimated_time | time_spent | state |
      || Some other description for task 1 |1624590000000|20| 20 | In Progress |
    Then the following warning is shown
      | warning |
      | La tarea debe tener todos los campos requeridos.|
  Scenario: Modifying task state without spending enough time
    Given A user with the following task
      | name | description | starting_date | estimated_time | time_spent | state |
      | Task 1 | Some description for task 1 |1624590000000|20| 10 | In Progress |
    When that user wants to fininsh it
    Then the following warning should be shown
      | warning |
      |La tarea debe tener todos los campos requeridos.|
  Scenario: Modifying task state when is possible
    Given A user with the following task
      | name | description | starting_date | estimated_time | time_spent | state |
      | Task 1 | Some description for task 1 |1624590000000|20| 20 | In Progress |
    When that user wants to fininsh it
    Then the task is modified
    