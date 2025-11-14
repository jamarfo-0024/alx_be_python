task = input("Enter your task: ")
priority = input("Priority(high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

if time_bound == "yes":
    print("This task is time-bound! Make sure you complete it on time.")

match priority:
    case "high":
        print(f"reminder: {task}, is a high priority task that requires immediate attention today!")
    case "medium":
        print(f"Note: {task}, is a medium priority task. Try to complete it soon")
    case "low":
        print(f"Note: {task}, is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered")
