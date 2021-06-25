Feature: addTask
  As an employee i want to add a task
  so that i can organize my schedule.

  Background:
    Given the following values for a task
      | name | description | starting_date | estimated_time |
      | Implementar PSA Cloud Spring ERP para cliente | Coordinar con el cliente la implementacion de PSA Cloud Spring ERP y relevar sus necesidades. | 18/06/2021 | 25 |


  Scenario: Add a task with all fields
    Given a user wants to add a task
    When the user adds the task with all the values
    Then the task is saved


