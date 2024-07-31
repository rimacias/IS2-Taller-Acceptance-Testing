from behave import *
from util import Task, TodoList

# Define a To-Do List
todo_list = TodoList()


@given("the To-Do list is empty")
def step_given(context):
    global todo_list
    todo_list = TodoList()


@when("the user marks {string} task as completed")
def step_when(context, string):
    global todo_list
    task = todo_list.get_task(string)
    todo_list.mark_task_completed(task)


@then("the To-Do list should contain {string} task mark as completed")
def step_then(context, string):
    global todo_list
    assert len(todo_list.get_completed_tasks()) == 1
    assert todo_list.get_completed_tasks()[0].name == string


@given("the To-Do list with task {string} incompleted")
def step_given(context, string):
    global todo_list
    todo_list = TodoList()
    task = Task("Description", string)
    todo_list.add_task(task)


@when("the user adds a task {string} with description {string}")
def step_when(context, string, string2):
    global todo_list
    task = Task(string2, string)
    todo_list.add_task(task)


@then("the To-Do list contains one task, {string}")
def step_then(context, string):
    global todo_list
    assert len(todo_list.get_all_tasks()) == 1
    assert todo_list.get_all_tasks()[0].name == string


@given("the To-Do list with {string} task is in")
def step_given(context, string):
    global todo_list
    todo_list = TodoList()
    task = Task("Description", string)
    todo_list.add_task(task)


@when("the user deletes {string} task")
def step_when(context, string):
    global todo_list
    task = todo_list.get_task(string)
    todo_list.remove_task(task)


@then("the To-Do list should not contain the {string} task")
def step_then(context, string):
    global todo_list
    contains_task = False
    for task in todo_list.get_all_tasks():
        if task.name == string:
            contains_task = True
            break
    assert not contains_task


@given("the To-Do list filled with tasks")
def step_given(context):
    global todo_list
    todo_list = TodoList()
    task1 = Task("Description", "Task 1")
    task2 = Task("Description", "Task 2")
    task3 = Task("Description", "Task 3")
    todo_list.add_task(task1)
    todo_list.add_task(task2)
    todo_list.add_task(task3)


@when("the user clears the list")
def step_when(context):
    global todo_list
    todo_list.remove_completed_tasks()


@then("the task should be empty")
def step_then(context):
    global todo_list
    assert len(todo_list.get_completed_tasks()) == 0
