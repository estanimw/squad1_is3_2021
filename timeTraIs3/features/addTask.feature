Feature: addTask
  As an employee i want to add a task
  so that i can organize my schedule.

  Background:
    Given the following values for a task
      | name | description | starting_date | estimated_time | time_spent | state |
      | Implementar PSA Cloud Spring ERP para cliente | Coordinar con el cliente la implementacion de PSA Cloud Spring ERP y relevar sus necesidades. | 1624821493959 | 25 | 1 | Paused |
      | Implementar PSA Cloud Spring ERP para cliente | Coordinar con el cliente la ijdbahsijdhiasjdhoiashdoashdoiasdhaoishdoiasdhoiashdbjasoidbaijsgdiuajsbdijasgdiuasjbdnaksldbjaosjidgboaisjkdb akjsdgouasidbnolaisdnhoiasdmplementacion iugaSIUGSOIUgvaiusgaiUSVaiusvaiuSViausjbvaiuSGVuiasiuaSViausv iauSViuagsbuaBSasde PSA Cloud Spring ERP y relevar sus necesidades. | 1624821493959 | 25 | 1 | Paused |


  Scenario: Add a task with all fields
    Given a user wants to add a task
    When the user adds the task with all the values
    Then the task is saved

  Scenario: Add a task with a description longer than 140 characters
    Given a user wants to add a task
    Given the following warning
    | warning |
    | La tarea debe tener una descripción de menos de 140 caracteres. |
    When the user adds the task with a too long description
    Then an invalid description warning is shown

  Scenario: Add a task without all the required values
    Given a user wants to add the following task
    | name | description | starting_date | state |
    | Implementar PSA Cloud Spring ERP para cliente |  |  | Completed |
    When the user adds the task without all the required values
    Then the following warning is shown
    | warning |
    | La tarea debe tener todos los campos requeridos. |