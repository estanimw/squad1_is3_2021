Feature: Visualize tasks
  As an employee, I want to visualize my tasks so that I can see what tasks I worked on

  Scenario: visualize tasks
    Given a user

    When he wants to visualize his tasks:
      | name | description | starting_date | estimated_time  | state |
      | Task 1 | Some description for task 1 |1624590000000|20 | Created |
      | Task 2 | Some description for task 1 |1624590000000|20 | Done |
      | Task 3 | Some description for task 1 |1624590000000|20 | Created |
      | Task 4 | Some description for task 1 |1624590000000|20 | Created |

    Then all his tasks are shown
