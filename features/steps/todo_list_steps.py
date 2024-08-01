# noqa: F405
from behave import *  # noqa: F403
from util import Task, TodoList



@given(u'the To-Do list is empty')
def step_impl(context):
    global todo_list
    todo_list = TodoList()


@when("the user adds a task 'Buy groceries' with description 'Buy milk, eggs, and bread'")
def step_impl(context):
    global todo_list
    todo_list.add_task(Task("Buy milk, eggs, and bread", "Buy groceries"))


@then("the To-Do list contains one task, 'Buy groceries' with description 'Buy milk, eggs, and bread'")
def step_impl(context):
    global todo_list
    assert len(todo_list.tasks) == 1
    assert todo_list.tasks[0].name == "Buy groceries"
    assert todo_list.tasks[0].description == "Buy milk, eggs, and bread"

@given("the To-Do list with task 'Buy Groceries' incompleted")
def step_impl(context):
    global todo_list
    todo_list = TodoList()
    todo_list.add_task(Task("Buy milk, eggs, and bread", "Buy groceries"))

@when("the user marks 'Buy Groceries' task as completed")
def step_impl(context):
    global todo_list
    todo_list.tasks[0].mark_completed()

@then("the To-Do list should contain 'Buy Groceries' task mark as completed")
def step_impl(context):
    global todo_list
    assert todo_list.get_task("Buy groceries").is_completed

@given("the To-Do list with 'Buy Groceries' task in")
def step_impl(context):
    global todo_list
    todo_list = TodoList()
    todo_list.add_task(Task("Buy milk, eggs, and bread", "Buy groceries"))

@when("the user deletes 'Buy Groceries' task")
def step_impl(context):
    global todo_list
    todo_list.remove_task("Buy groceries")

@then("the To-Do list should not contain the 'Buy Groceries' task")
def step_impl(context):
    global todo_list
    assert todo_list.get_task("Buy groceries") is None

@given("the To-Do list filled with tasks")
def step_impl(context):
    global todo_list
    todo_list = TodoList()
    todo_list.add_task(Task("Buy milk, eggs, and bread", "Buy groceries"))
    todo_list.add_task(Task("Math and Science", "Do homework"))
    todo_list.add_task(Task("Sweep and mop", "Clean house"))

@when("the user clears the list")
def step_impl(context):
    global todo_list
    todo_list.remove_all_tasks()

@then("the To-Do list should be empty")
def step_impl(context):
    global todo_list
    assert len(todo_list.tasks) == 0