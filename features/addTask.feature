Feature: addTask
  As user I want to be able to create a task so that I can define with detail my toDo's


  Scenario: Add a task with all fields
    Given a user wants to add the following task
      | name | description | starting_date | estimated_time | state |
      | Implementar PSA Cloud Spring ERP para cliente | Coordinar con el cliente la implementacion de PSA Cloud Spring ERP y relevar sus necesidades. | 1624821493959 | 25 | Paused |
    When the user adds the task with all the values
    Then the task is saved

  Scenario: Add a task with a description longer than 140 characters
    Given a user wants to add the following task
      | name | description | starting_date | estimated_time | state |
      | Implementar PSA Cloud Spring ERP para cliente | Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et mag | 1624821493959 | 25 | Paused |
    When the user adds the task with a too long description
    Then the following warning is shown
      | warning |
      | La tarea debe tener una descripción de menos de 140 caracteres. |
  
  Scenario: Add a task without all the required values
    Given a user wants to add the following task
    | name | description | starting_date | state |
    | Implementar PSA Cloud Spring ERP para cliente |  |  | Completed |
    When the user adds the task without all the required values
    Then the following warning is shown
    | warning |
    | La tarea debe tener todos los campos requeridos. |
