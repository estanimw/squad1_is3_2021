Feature: addTask
  As an employee i want to add a task
  so that i can organize my schedule.

  Background:
    Given the following values for a task
      | name | description | starting_date | estimated_time | time_spent | state |
      | Implementar PSA Cloud Spring ERP para cliente | Coordinar con el cliente la implementacion de PSA Cloud Spring ERP y relevar sus necesidades. | 1624821493959 | 25 | 1 | Paused |


  Scenario: Add a task with all fields
    Given the following values for a task
      | name | description | starting_date | estimated_time | time_spent | state |
      | Implementar PSA Cloud Spring ERP para cliente | Coordinar con el cliente la implementacion de PSA Cloud Spring ERP y relevar sus necesidades. | 1624821493959 | 25 | 1 | Paused |
    Given a user wants to add a task
    When the user adds the task with all the values
    Then the task is saved


