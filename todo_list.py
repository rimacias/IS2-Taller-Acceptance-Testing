from util import Task, TodoList

menu = """BIENVENIDO A TU LISTA DE TAREAS
1. Ver lista de tareas
2. Agregar tarea
3. Marcar tarea como completada
4. Eliminar tarea
5. Eliminar todas las tareas completadas
6. Eliminar todas las tareas
7. Salir
"""

opcion = ""
todo_list = TodoList()
while opcion != "7":
    print(menu)
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("LISTA DE TAREAS")
        if not todo_list.tasks or len(todo_list.tasks) == 0:
            print("No hay tareas.")
        print(todo_list, "\n\n")
    elif opcion == "2":
        print("Agregar tarea")
        name = input("Nombre de la tarea: ")
        description = input("Descripción de la tarea: ")
        task = Task(description, name)
        todo_list.add_task(task)
    elif opcion == "3":
        print("MARCAR TAREA COMO COMPLETADA")
        print("Tareas incompletas:")
        i = 1
        incomplete_tasks = todo_list.get_incomplete_tasks()
        for task in incomplete_tasks:
            print(f"{i}. {task}")
            i += 1
        MSG = "Elige el número de la tarea a marcar como completada: "
        task_number = input(MSG)
        while (
            not task_number.isdigit()
            or int(task_number) < 1
            or int(task_number) > len(incomplete_tasks)
        ):
            task_number = input(
                "Elige el número de la tarea a marcar como completada: "
            )
        task = incomplete_tasks[int(task_number) - 1]
        todo_list.mark_task_completed(task)
        print("Tarea marcada como completada")
    elif opcion == "4":
        print("ELIMINAR TAREA")
        print("Todas las tareas:")
        i = 1
        for task in todo_list.tasks:
            print(f"{i}. {task}")
            i += 1
        task_number = input("Elige el número de la tarea a eliminar: ")
        while (
            not task_number.isdigit()
            or int(task_number) < 1
            or int(task_number) > len(todo_list.tasks)
        ):
            task_number = input("Elige el número de la tarea a eliminar: ")
        task = todo_list.tasks[int(task_number) - 1]
        todo_list.remove_task(task)
        print("Tarea eliminada")
    elif opcion == "5":
        print("ELIMINAR TODAS LAS TAREAS COMPLETADAS")
        completed_tasks = todo_list.get_completed_tasks()
        print("Se removerán las siguientes tareas:")
        print("\n".join([str(task) for task in completed_tasks]))
        confirm = input("¿Estás seguro? (s/n): ")
        if confirm == "s":
            for task in completed_tasks:
                todo_list.remove_task(task)
            print("Tareas eliminadas")
        else:
            print("Operación cancelada")
    elif opcion == "6":
        print("ELIMINAR TODAS LAS TAREAS")
        confirm = input("¿Estás seguro? (s/n): ")
        if confirm == "s":
            todo_list = TodoList()
            print("Todas las tareas eliminadas")
        else:
            print("Operación cancelada")
    elif opcion == "7":
        print("Adiós")
    else:
        print("Opción no válida")
