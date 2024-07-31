# language: en

Feature: Create a todo list program.

    Scenario: Adding a task "Buy Groceries" to the lists
        Given the To-Do list is empty
        When the user adds a task 'Buy groceries' with description 'Buy milk, eggs, and bread'
        Then the To-Do list contains one task, 'Buy groceries'

    Scenario: Mark "Buy Groceries" task as completed.
        Given the To-Do list with task "Buy Groceries" incompleted
        When the user marks "Buy Groceries" task as completed
        Then the To-Do list should contain "Buy Groceries" task mark as completed

    Scenario: Delete task "Buy Groceries"
        Given the To-Do list with "Buy Groceries" task is in
        When the user deletes "Buy Groceries" task
        Then the To-Do list should not contain the "Buy Groceries" task
    
    Scenario: Clear the To-Do list
        Given the To-Do list filled with tasks
        When the user clears the list
        Then the task should be empty
    